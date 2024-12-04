import cv2
import numpy as np
import time
import torch
from PIL import Image, ImageDraw, ImageFont
from torchvision import transforms
from transformers import ViTForImageClassification, ViTImageProcessor

# Configuración del dispositivo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Cargar el modelo entrenado
model = ViTForImageClassification.from_pretrained(
    'google/vit-base-patch16-224-in21k',
    num_labels=7
)
model.load_state_dict(torch.load("vit_emotion_model.pth"))
model.eval()
model.to(device)

# Lista de emociones
CLASSES = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

# Procesador de imágenes
processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')

# Transformaciones de imagen
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Función para crear una caja translúcida con texto centrado horizontalmente
def draw_text_box(frame, text, position, font_size=24, box_alpha=0.5, font_path='/Library/Fonts/Arial.ttf'):
    if frame is None:
        print("Error: El frame es None")
        return frame
    
    # Convertir el frame de OpenCV a PIL
    try:
        img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    except Exception as e:
        print(f"Error al convertir el frame: {e}")
        return frame

    draw = ImageDraw.Draw(img_pil)
    
    # Intentar cargar la fuente, usar la predeterminada si no se encuentra
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Advertencia: No se pudo cargar la fuente. Usando fuente predeterminada.")
        font = ImageFont.load_default()

    # Obtener el tamaño del texto usando textbbox
    try:
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
    except Exception as e:
        print(f"Error al calcular el tamaño del texto: {e}")
        return frame
    
    # Calcular las coordenadas del cuadro de texto
    box_x1, box_y1 = position
    box_x2 = box_x1 + text_width + 20
    box_y2 = box_y1 + text_height + 20

    # Dibujar la caja translúcida
    box_color = (0, 0, 0, int(255 * box_alpha))  # Negro con transparencia
    try:
        box = Image.new('RGBA', (box_x2 - box_x1, box_y2 - box_y1), box_color)
        img_pil.paste(box, (box_x1, box_y1), box)
    except Exception as e:
        print(f"Error al dibujar el cuadro de texto: {e}")
        return frame
    
    # Dibujar el texto en blanco
    try:
        draw.text((box_x1 + 10, box_y1 + 10), text, font=font, fill=(255, 255, 255, 255))
    except Exception as e:
        print(f"Error al dibujar el texto: {e}")
        return frame

    # Convertir de vuelta la imagen PIL a OpenCV
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# Configuraciones iniciales
subtitle_text = "Where are you from?"  # El texto que aparecerá abajo
corner_text = "😬 Alegría"        # Texto con emoji en la esquina superior derecha

# Inicializar variables de subtítulos y contador
questions = ["¿Cómo te sientes el día de hoy?", "¿Cómo te ves en 10 años?", "¿Cuál ha sido tu mayor proyecto?"]
emotion_durations = {emotion: 0 for emotion in CLASSES}
current_question_idx = 0
start_time = time.time()
time_limit = 60  # Tiempo por pregunta en segundos

# Inicializar la captura de video
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Cargar el clasificador de caras (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

print("Presiona 'q' para salir o 's' para saltar la pregunta actual.")

while True:
    # Capturar un cuadro del video
    ret, frame = cap.read()
    if not ret:
        print("Error al capturar el video.")
        break

    # Convertir el cuadro a escala de grises para la detección de caras
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras en el cuadro
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    # Dimensiones del frame
    height, width, _ = frame.shape

    # Si se detectan caras, elegir la más grande
    emotion = "No face detected"
    if len(faces) > 0:
        largest_face = max(faces, key=lambda rect: rect[2] * rect[3])
        x, y, w, h = largest_face
        face = frame[y:y+h, x:x+w]
        face_tensor = transform(face).unsqueeze(0).to(device)
        with torch.no_grad():
            outputs = model(pixel_values=face_tensor)
            logits = outputs.logits
            predicted_class = logits.argmax(-1).item()
            emotion = CLASSES[predicted_class]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Calcular tiempo restante
    elapsed_time = time.time() - start_time
    remaining_time = max(0, time_limit - int(elapsed_time))

    # Actualizar duración de la emoción detectada
    if emotion in emotion_durations:
        emotion_durations[emotion] += 1

    # Mostrar subtítulo y contador
    subtitle_text = questions[current_question_idx]
    frame = draw_text_box(frame, subtitle_text, position=(50, height - 120), font_size=40)
    timer_text = f"{remaining_time // 60:02}:{remaining_time % 60:02}"
    frame = draw_text_box(frame, timer_text, position=(50, 20), font_size=24)

    # Mostrar emoción detectada en la esquina superior derecha
    frame = draw_text_box(frame, emotion, position=(width - 200, 20), font_size=24)

    # Reiniciar o avanzar al siguiente subtítulo
    if remaining_time == 0 or cv2.waitKey(1) & 0xFF == ord('s'):
        print(f"\nResultados para: {subtitle_text}")
        total_duration = sum(emotion_durations.values())
        for emotion, duration in emotion_durations.items():
            percentage = (duration / total_duration) * 100 if total_duration > 0 else 0
            print(f"{emotion}: {percentage:.2f}%")
        emotion_durations = {emotion: 0 for emotion in CLASSES}
        current_question_idx += 1
        start_time = time.time()

        if current_question_idx >= len(questions):
            print("Se han terminado las preguntas.")
            break

    # Mostrar el cuadro
    cv2.imshow("Detección de Emociones", frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
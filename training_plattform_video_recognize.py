import cv2
import torch
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

# Inicializar la captura de video
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Cargar el clasificador de caras (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

print("Presiona 'q' para salir.")

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

    for (x, y, w, h) in faces:
        # Recortar la región de la cara
        face = frame[y:y+h, x:x+w]

        # Preprocesar la cara
        face_tensor = transform(face).unsqueeze(0).to(device)

        # Hacer la predicción
        with torch.no_grad():
            outputs = model(pixel_values=face_tensor)
            logits = outputs.logits
            predicted_class = logits.argmax(-1).item()
            emotion = CLASSES[predicted_class]

        # Dibujar un rectángulo alrededor de la cara y mostrar la emoción
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Mostrar el cuadro con las emociones detectadas
    cv2.imshow("Detección de Emociones", frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
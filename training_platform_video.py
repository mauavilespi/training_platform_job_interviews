import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

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
camera = cv2.VideoCapture(1)  # Abrir la cámara

# Verifica si la cámara se abre correctamente
if not camera.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

try:
    while True:
        ret, frame = camera.read()  # Capturar el frame
        
        if not ret or frame is None:
            print("Error capturando el frame.")
            break
        
        # Dimensiones del frame
        try:
            height, width, _ = frame.shape
        except AttributeError as e:
            print(f"Error obteniendo las dimensiones del frame: {e}")
            break

        # Crear una fuente para calcular el tamaño del texto
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 48)
        
        # Añadir subtítulos en la parte inferior (texto mucho más grande y centrado)
        subtitle_bbox = ImageDraw.Draw(Image.new('RGB', (width, height))).textbbox((0, 0), subtitle_text, font=font)
        text_width = subtitle_bbox[2] - subtitle_bbox[0]
        subtitle_position = ((width - text_width) // 2, height - 120)  # Centrado horizontalmente
        frame = draw_text_box(frame, subtitle_text, position=subtitle_position, font_size=40)  # Tamaño de fuente mayor

        # Añadir el texto en la esquina superior derecha con un tamaño más grande
        frame = draw_text_box(frame, corner_text, position=(width - 200, 20), font_size=24)  # Tamaño de fuente mayor
        
        # Mostrar el frame con los textos
        cv2.imshow('Video', frame)
        
        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Liberar recursos
    camera.release()
    cv2.destroyAllWindows()
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from transformers import ViTForImageClassification, ViTImageProcessor
from tqdm import tqdm

# Configuración general
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
BATCH_SIZE = 16
EPOCHS = 5
LEARNING_RATE = 1e-4
NUM_LABELS = 7  # Cambiar si hay más o menos emociones

# Clases de emociones
CLASSES = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

# 1. Preparar el dataset
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Tamaño de entrada para ViT
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Cargar datos desde carpetas
train_dataset = datasets.ImageFolder(root='/Users/mauavilespi/Documents/TTR/Dataset/archive/train', transform=transform)
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)

# 2. Cargar modelo ViT preentrenado
model = ViTForImageClassification.from_pretrained(
    'google/vit-base-patch16-224-in21k',
    num_labels=NUM_LABELS  # Número de emociones
).to(device)

# 3. Configurar el optimizador y función de pérdida
optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
criterion = torch.nn.CrossEntropyLoss()

# 4. Entrenar el modelo
print("Iniciando entrenamiento...")
model.train()
for epoch in range(EPOCHS):
    epoch_loss = 0
    for images, labels in tqdm(train_loader, desc=f"Epoch {epoch+1}/{EPOCHS}"):
        images, labels = images.to(device), labels.to(device)

        # Forward
        optimizer.zero_grad()
        outputs = model(pixel_values=images)
        loss = criterion(outputs.logits, labels)

        # Backward y optimización
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    print(f"Epoch {epoch+1} finalizada. Pérdida promedio: {epoch_loss / len(train_loader)}")

# 5. Guardar el modelo entrenado
torch.save(model.state_dict(), "vit_emotion_model.pth")
print("Modelo guardado como 'vit_emotion_model.pth'.")

# 6. Cargar modelo para inferencia
model.eval()  # Cambiar a modo de evaluación
model.load_state_dict(torch.load("vit_emotion_model.pth"))

# 7. Inferencia en imágenes individuales
def predict_emotion(image_path):
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
    image = transforms.ToPILImage()(image_path)  # Asegúrate de cargar la imagen como tensor si es un batch

    inputs = processor(images=image, return_tensors="pt").to(device)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax(-1).item()
    return CLASSES[predicted_class]

# Ejemplo: predicción en una imagen
test_image = "/Users/mauavilespi/Documents/TTR/Dataset/archive/train/angry/im3978.png"  # Cambia esto
print(f"Emoción predicha: {predict_emotion(test_image)}")
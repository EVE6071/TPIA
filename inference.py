import tensorflow as tf
import cv2
from ultralytics import YOLO  # Assurez-vous d'avoir installé cette bibliothèque

def load_model(model_path='model.h5'):
    model = tf.keras.models.load_model(model_path)
    return model

def infer(model, input_data):
    predictions = model.predict(input_data)
    return predictions

def detect_faces(image_path):
    model = load_yolo_model()
    image = cv2.imread(image_path)
    results = model.predict(source=image_path)
    faces = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy)
            faces.append((x1, y1, x2, y2))
    return faces

def load_yolo_model():
    # Charger le modèle YOLOv8
    model = YOLO('yolov8n.pt')  # Vous pouvez remplacer 'yolov8n.pt' par le chemin de votre modèle YOLOv8 personnalisé
    return model

from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # depois você troca por modelo de placa

def detectar_placa(frame):
    resultados = model(frame)[0]

    for box in resultados.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        placa_img = frame[y1:y2, x1:x2]
        return placa_img, (x1, y1, x2, y2)

    return None, None

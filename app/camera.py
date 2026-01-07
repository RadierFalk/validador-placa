import cv2

def iniciar_camera(index=0):
    cam = cv2.VideoCapture(index)
    if not cam.isOpened():
        raise Exception("Não foi possível acessar a webcam")
    return cam

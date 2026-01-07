import cv2
import time

from detector import detectar_placa
from preprocess import preprocessar
from ocr import ler_placa
from validator import validar_placa
from access_control import processar_acesso

# =========================
# CONFIGURAÇÕES
# =========================
PROCESS_INTERVAL = 1.5   # segundos entre OCR
ACESSO_INTERVAL = 10     # cooldown por placa
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# =========================
cap = cv2.VideoCapture(0)

ultimo_processamento = 0
ultimo_acesso = 0
ultima_placa = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 🔥 Reduz resolução (ganho enorme de performance)
    frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))

    agora = time.time()

    placa_img = None
    box = None
    texto = None

    # =========================
    # PROCESSAMENTO CONTROLADO
    # =========================
    if agora - ultimo_processamento > PROCESS_INTERVAL:
        ultimo_processamento = agora

        placa_img, box = detectar_placa(frame)

        if placa_img is not None:
            proc = preprocessar(placa_img)
            texto = ler_placa(proc)

            if validar_placa(texto):
                # 🧠 evita reprocessar mesma placa
                if texto != ultima_placa:
                    if agora - ultimo_acesso > ACESSO_INTERVAL:
                        img_path = f"images/acessos/{texto}_{int(agora)}.jpg"
                        cv2.imwrite(img_path, frame)

                        processar_acesso(texto, img_path)

                        ultimo_acesso = agora
                        ultima_placa = texto

    # =========================
    # DESENHO NA TELA (LEVE)
    # =========================
    if box is not None and texto is not None:
        x1, y1, x2, y2 = box
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
        cv2.putText(
            frame,
            texto,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0,255,0),
            2
        )

    cv2.imshow("Controle de Acesso", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

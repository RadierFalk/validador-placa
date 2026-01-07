import easyocr

reader = easyocr.Reader(['pt'], gpu=False)

def ler_placa(img):
    resultados = reader.readtext(img)

    for _, texto, conf in resultados:
        if conf > 0.6:
            return texto.upper().replace(" ", "")

    return None

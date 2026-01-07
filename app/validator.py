import re

PADRAO_PLACA = r'^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$'

def validar_placa(texto):
    if texto is None:
        return False
    return bool(re.match(PADRAO_PLACA, texto))

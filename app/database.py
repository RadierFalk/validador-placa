import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("data/placas.db", check_same_thread=False)
cursor = conn.cursor()

def buscar_placa(placa):
    cursor.execute("SELECT * FROM placas WHERE placa=? AND ativa=1", (placa,))
    return cursor.fetchone()

def cadastrar_visitante(placa):
    validade = (datetime.now() + timedelta(days=1)).isoformat()
    cursor.execute(
        "INSERT OR IGNORE INTO placas VALUES (NULL, ?, ?, ?, ?, ?)",
        (placa, "VISITANTE", "VISITANTE", 0, validade)
    )
    conn.commit()

def registrar_acesso(placa, status, imagem):
    cursor.execute(
        "INSERT INTO acessos VALUES (NULL, ?, ?, ?, ?)",
        (placa, status, datetime.now().isoformat(), imagem)
    )
    conn.commit()

from database import buscar_placa, cadastrar_visitante, registrar_acesso

def processar_acesso(placa, imagem_path):
    registro = buscar_placa(placa)

    if registro:
        registrar_acesso(placa, "LIBERADO", imagem_path)
        print(f"✅ Acesso liberado: {placa}")
    else:
        cadastrar_visitante(placa)
        registrar_acesso(placa, "NEGADO", imagem_path)
        print(f"🚨 Visitante não autorizado: {placa}")

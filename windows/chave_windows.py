#
# testei no Windows 11 e não funcionou, mas pode funcionar em outras versões
# -*- coding: utf-8 -*-

import winreg  # Biblioteca específica do Windows

def obter_chave_windows():
    """
    Obtém a chave de produto do Windows do registro.
    """
    try:
        chave_raiz = winreg.HKEY_LOCAL_MACHINE
        chave_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
        chave = winreg.OpenKey(chave_raiz, chave_path)
        valor, tipo = winreg.QueryValueEx(chave, "DigitalProductId")
        winreg.CloseKey(chave)

        print(f"Comprimento do DigitalProductId: {len(valor)}")  # Adicione esta linha
        if len(valor) < 67: #verificar se é menor do que o tamanho minimo
            print("DigitalProductId tem um comprimento inesperado.")
            return None

        chave_produto = decodificar_chave_produto(valor)
        return chave_produto

    except Exception as e:
        print(f"Erro ao obter a chave do Windows: {e}")
        return None

def decodificar_chave_produto(produto_id):
    """
    Decodifica o 'DigitalProductId' para extrair a chave de produto.
    Essa função é simplificada e pode não funcionar em todas as versões do Windows.
    A decodificação completa é mais complexa.
    """
    offset = 52
    isvowels = "BCDFGHJKLMNPQRTVWXY"
    chave = ""
    produto_id_copy = list(produto_id[offset:offset+15])
    for i in range(14, -1, -1):
        indice = 0
        for j in range(14, -1, -1):
            indice = indice * 256
            indice = produto_id_copy[j] + indice
            produto_id_copy[j] = (indice // 24)
            indice = indice % 24
        chave = isvowels[indice] + chave
    chave_produto = chave[0:5] + "-" + chave[5:10] + "-" + chave[10:15]

    return chave_produto





# Exemplo de uso
chave = obter_chave_windows()
if chave:
    print(f"Chave do Windows: {chave}")
else:
    print("Não foi possível obter a chave do Windows.")
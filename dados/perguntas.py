import json
import os

CAMINHO_ARQUIVO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "perguntas.json",
)

NUMERO_DA_CATEGORIA = {"facil": 1, "media": 2, "dificil": 3}

def carregar_todas_as_perguntas():
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados["questoes"]

def obter_perguntas_por_categoria(categoria):
    todas = carregar_todas_as_perguntas()
    if categoria == "todas":
        return todas
    numero = NUMERO_DA_CATEGORIA[categoria]
    return [questao for questao in todas if questao["categoria"] == numero]

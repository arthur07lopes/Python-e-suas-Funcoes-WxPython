import json
import os

CAMINHO_ARQUIVO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "perguntas.json"
)

def carregar_questoes():
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados["questoes"]

def obter_questoes_por_categoria(categoria):
    todos = carregar_questoes()
    return [q for q in todos if q["categoria"] == categoria]

def obter_nome_categoria(categoria):
    nomes = {1: "Fáceis", 2: "Médias", 3: "Difíceis"}
    return nomes.get(categoria, "Desconhecida")

from pathlib import Path
import os

RAIZ_RECURSOS = Path(__file__).resolve().parent.parent
CAMINHO_PERGUNTAS = RAIZ_RECURSOS / "dados" / "questoes.json"
CAMINHO_DOCUMENTACAO = RAIZ_RECURSOS / "dados" / "documentacao.txt"

TITULO_APLICACAO = "Python e suas Funcoes - Quiz"
TOTAL_QUESTOES = 16 
TENTATIVAS_POR_QUESTAO = 3

QUANTIDADE_POR_DIFICULDADE = {
    "facil": 5,
    "media": 5,
    "dificil": 6,
}

PONTOS_POR_DIFICULDADE = {
    "facil": 3,
    "media": 6,
    "dificil":8,
}

MULTIPLICADOR_POR_TENTATIVA = {
    1: 1.0,
    2: 0.6,
    3: 0.3,
}

def diretorio_dados_usuario() -> Path:
    appdata = os.environ.get("APPDATA")
    if appdata:
        return Path(appdata) / "Python-e-suas-Funcoes"
    return Path.home() / ".python-e-suas-funcoes"

CAMINHO_HISTORICO = diretorio_dados_usuario() / "historico.json"

from dados.perguntas import obter_perguntas_por_categoria(categoria)
from logica.pontuacao import Pontuacao

MAXIMO_DE_TENTATIVAS = 3

class MotorQuiz:
    def __init__(self, categoria):
        self.perguntas = obter_perguntas_por_categoria(categoria)
        self.indice_pergunta_atual = 0
        self.tentativas_usadas = 0
        self.respostas_erradas_dadas = []
        self.pontuacao = Pontuacao()

    @property
    def pergunta_atual(self):
        return self.perguntas[self.indice_pergunta_atual]

    @property
    def total_de_perguntas(self):
        return len(self.perguntas)

    @property
    def tentativas_restantes(self):
        return MAXIMO_DE_TENTATIVAS - self.tentativas_usadas

    @property
    def acabou(self):
        return self.indice_pergunta_atual >= self.total_de_perguntas

    def responder(self, letra_escolhida):
        self.tentativas_usadas += 1
        pergunta = self.pergunta_atual

        if letra_escolhida == pergunta["resposta"]:
            self.pontuacao.registrar_resposta(
                pergunta, self.tentativas_usadas, self.respostas_erradas_dadas
            )
            return "acertou"
        self.respostas_erradas_dadas.append(pergunta["alternativas"][letra_escolhida])

        if self.tentativas_usadas >= MAXIMO_DE_TENTATIVAS:
            self.pontuacao.registrar_resposta(pergunta, None, self.respostas_erradas_dadas)
            return "errou_esgotou_tentativas"

        return "errou_tem_mais_tentativas"

    def avancar_para_proxima_pergunta(self):
        self.indice_pergunta_atual += 1
        self.tentativas_usadas = 0
        self.respostas_erradas_dadas = []

import random
from .dados.questoes import obter_questoes_por_categoria
from logica.pontuacao import Pontuacao

class MotorQuiz:
    def __init__(self, categoria):
        self.categoria = categoria
        self.questoes = obter_questoes_por_categoria(categoria)
        random.shuffle(self.questoes)
        self.indice_atual = 0
        self.pontuacao = Pontuacao()

    def questao_atual(self):
        if self.indice_atual < len(self.questoes):
            return self.questoes[self.indice_atual]
        return None

    def responder(self, letra_escolhida):
        questao = self.questao_atual()
        acertou = self.pontuacao.registrar_resposta(
            questao["questao"], letra_escolhida, questao["resposta"]
        )
        self.indice_atual += 1
        return acertou

    def acabou(self):
        return self.indice_atual >= len(self.questoes)

    def progresso(self):
        return self.indice_atual, len(self.questoes)

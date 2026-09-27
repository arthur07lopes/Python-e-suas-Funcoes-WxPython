# Classe para armazenar o status atual do quiz e das respostas do usuário (perguntas respondidas, pontuação atual, entre outros)

class StatusQuiz:
    def __init__(self, perguntas_totais):
        self.perguntas_respondidas = 0
        self.pontuacao_atual = 0
        self.perguntas_totais = perguntas_totais
        self.respostas_usuario = []

    def atualizar_status(self, pontuacao, resposta):
        """Atualiza o status do usuário com base numa nova resposta que ele deu, incrementando a pontuação e o número de perguntas respondidas e depois adicionando a resposta à lista. A resposta deve ser uma alternativa (a - d)."""
        self.perguntas_respondidas += 1
        self.pontuacao_atual += pontuacao
        self.respostas_usuario.append(resposta)

    def calcular_pontuacao(self, categoria):
        """Retorna a pontuação para um determinado acerto com base na categoria da pergunta. 1=fácil, 2=médio e 3=difícil"""
        if categoria == 1:
            return 3
        elif categoria == 2:
            return 6
        elif categoria == 3:
            return 8
        return 0

    def resetar_status(self):
        self.perguntas_respondidas = 0
        self.pontuacao_atual = 0
        self.respostas_usuario = []
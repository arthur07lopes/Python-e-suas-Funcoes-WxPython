class Pontuacao:
    def __init__(self):
        self.acertos = 0
        self.erros = 0
        self.respondidas = []

    def registrar_resposta(self, pergunta, resposta_usuario, correta):
        acertou = resposta_usuario == correta
        if acertou:
            self.acertos += 1
        else:
            self.erros += 1
        self.respondidas.append({
            "pergunta": pergunta,
            "resposta_usuario": resposta_usuario,
            "correta": correta,
            "acertou": acertou
        })
        return acertou

    def total(self):
        return self.acertos + self.erros

    def percentual_acerto(self):
        if self.total() == 0:
            return 0
        return round((self.acertos / self.total()) * 100, 1)

    def erros_para_revisao(self):
        return [r for r in self.respondidas if not r["acertou"]]

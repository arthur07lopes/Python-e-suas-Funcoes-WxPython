PONTOS_POR_CATEGORIA = {1: 10, 2: 20, 3: 30}
FRACAO_POR_TENTATIVA = {1: 1.0, 2: 0.6, 3: 0.3}

def calcular_pontos(categiria, tentativa_do_acerto):
    if tentativa_do_acerto is None:
        return 0
    return round(PONTOS_POR_CATEGORIA["categoria"] * FRACAO_POR_TENTATIVA[tentativa_do_acerto])


class Pontuacao:
    def __init__(self):
        self.total = 0
        self.acertos = 0
        self.erros = 0
        self.historico = []

    def registrar_resposta(self, pergunta, tentativa_do_acerto, respostas_erradas_dadas):
        pontos_ganhos = calcular_pontos(pergunta["categoria"], tentativa_do_acerto)
        acertou = tentativa_do_acerto is not None

        self.total += pontos_ganhos
        if acertou:
            self.acertos += 1
        else:
            self.erros += 1

        self.historico.append(
            {
                "id": pergunta["id"],
                "enunciado": pergunta["pergunta"],
                "acertou": acertou,
                "tentativa_do_acerto": tentativa_do_acerto,
                "pontos_ganhos": pontos_ganhos,
                "respostas_erradas_dadas": list(respostas_erradas_dadas),
                "resposta_correta_texto": pergunta["alternativas"][pergunta["resposta"]],
            }
        )

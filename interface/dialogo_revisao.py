import wx

from interface import tema


class DialogoRevisao(wx.Dialog):
    def __init__(self, pai, pergunta, respostas_erradas_dadas):
        super().__init__(
            pai,
            title="Tentativas esgotadas — revisão da resposta",
            size=(660, 500),
        )
        self.SetBackgroundColour(tema.BRANCO)
        self._montar_layout(pergunta, respostas_erradas_dadas)
        self.SetAffirmativeId(wx.ID_OK)
        self.SetEscapeId(wx.ID_OK)
        self.Centre()

    def _montar_texto(self, pergunta, respostas_erradas_dadas):
        letra_certa = pergunta["resposta"]
        resposta_certa = f"{letra_certa}) {pergunta['alternativas'][letra_certa]}"
        erradas = list(dict.fromkeys(respostas_erradas_dadas))

        linhas = [
            "Você usou as 3 tentativas e não acertou esta pergunta.",
            f"Pergunta:\n{pergunta['pergunta']}",
            f"Resposta correta: {resposta_certa}",
            "Alternativas que você marcou e estavam erradas: " + "; ".join(erradas),
            f"Explicação: {pergunta['explicacao']}",
        ]
        return "\n\n".join(linhas)

    def _montar_layout(self, pergunta, respostas_erradas_dadas):
        painel = wx.Panel(self)
        painel.SetBackgroundColour(tema.BRANCO)
        layout = wx.BoxSizer(wx.VERTICAL)

        rotulo = wx.StaticText(painel, label="Revisão da pergunta")
        rotulo.SetForegroundColour(tema.AZUL_PYTHON)

        self.caixa_revisao = wx.TextCtrl(
            painel,
            value=self._montar_texto(pergunta, respostas_erradas_dadas),
            style=wx.TE_MULTILINE | wx.TE_READONLY,
            size=(600, 340),
        )
        self.caixa_revisao.SetName("Revisão da pergunta")

        botao_continuar = wx.Button(painel, id=wx.ID_OK, label="&Continuar")
        botao_continuar.SetDefault()

        layout.Add(rotulo, flag=wx.ALL, border=12)
        layout.Add(self.caixa_revisao, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=12)
        layout.Add(botao_continuar, flag=wx.ALIGN_CENTER | wx.ALL, border=12)

        painel.SetSizer(layout)
        wx.CallAfter(self.caixa_revisao.SetFocus)

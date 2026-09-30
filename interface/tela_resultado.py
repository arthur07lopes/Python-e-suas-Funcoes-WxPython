import wx

from interface import tema


class TelaResultado(wx.Frame):
    def __init__(self, pontuacao):
        super().__init__(
            None,
            title="Python e suas Funções — Resultado Final",
            size=(700, 600),
        )
        self.pontuacao = pontuacao
        self.SetBackgroundColour(tema.BRANCO)
        self._montar_layout()
        self.Centre()

    def _montar_texto(self):
        linhas = [
            "Quiz concluído!",
            f"Pontuação total: {self.pontuacao.total} pontos. "
            f"Acertos: {self.pontuacao.acertos}. Erros: {self.pontuacao.erros}.",
            "Resumo pergunta a pergunta:",
        ]
        for posicao, item in enumerate(self.pontuacao.historico, start=1):
            enunciado = item["enunciado"].split("\n")[0]
            if item["acertou"]:
                linhas.append(
                    f"{posicao}. ACERTOU na tentativa {item['tentativa_do_acerto']}, "
                    f"+{item['pontos_ganhos']} pontos. {enunciado}"
                )
            else:
                linhas.append(
                    f"{posicao}. ERROU. {enunciado} "
                    f"Resposta correta: {item['resposta_correta_texto']}"
                )
        return "\n\n".join(linhas)

    def _montar_layout(self):
        painel = wx.Panel(self)
        painel.SetBackgroundColour(tema.BRANCO)
        layout = wx.BoxSizer(wx.VERTICAL)

        rotulo = wx.StaticText(painel, label="Resultado final")
        rotulo.SetForegroundColour(tema.AZUL_PYTHON)

        self.caixa_resultado = wx.TextCtrl(
            painel,
            value=self._montar_texto(),
            style=wx.TE_MULTILINE | wx.TE_READONLY,
            size=(640, 400),
        )
        self.caixa_resultado.SetName("Resultado final do quiz")

        self.botao_refazer = wx.Button(painel, label="&Refazer o quiz")
        self.botao_menu = wx.Button(painel, label="&Menu principal")
        self.botao_sair = wx.Button(painel, label="&Sair do programa")

        self.botao_refazer.Bind(wx.EVT_BUTTON, self.ao_clicar_refazer)
        self.botao_menu.Bind(wx.EVT_BUTTON, self.ao_clicar_menu)
        self.botao_sair.Bind(wx.EVT_BUTTON, self.ao_clicar_sair)

        layout.Add(rotulo, flag=wx.ALL, border=12)
        layout.Add(self.caixa_resultado, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=12)
        layout.Add(self.botao_refazer, flag=wx.ALIGN_CENTER | wx.TOP, border=10)
        layout.Add(self.botao_menu, flag=wx.ALIGN_CENTER | wx.TOP, border=6)
        layout.Add(self.botao_sair, flag=wx.ALIGN_CENTER | wx.ALL, border=6)

        painel.SetSizer(layout)
        wx.CallAfter(self.caixa_resultado.SetFocus)

    def ao_clicar_refazer(self, evento):
        from interface.tela_categorias import TelaCategorias

        TelaCategorias().Show()
        self.Close()

    def ao_clicar_menu(self, evento):
        from interface.tela_inicial import TelaInicial

        TelaInicial().Show()
        self.Close()

    def ao_clicar_sair(self, evento):
        self.Close()

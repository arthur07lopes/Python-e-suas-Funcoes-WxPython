import wx
from interface import tema

class TelaCategorias(wx.Frame):
    def __init__(self):
        super().__init__(
            None,
            title="Escolha a categoria das perguntas",
            size=(520, 420),
        )
        self.SetBackgroundColour(tema.BRANCO)
        self._montar_layout()
        self.Centre()

    def _montar_layout(self):
        painel = wx.Panel(self)
        painel.SetBackgroundColour(tema.BRANCO)
        layout = wx.BoxSizer(wx.VERTICAL)

        grupo = wx.StaticBoxSizer(wx.VERTICAL, painel, "Selecione a dificuldade")
        caixa = grupo.GetStaticBox()

        self.opcao_facil = wx.RadioButton(caixa, label="Fácil (5 perguntas)", style=wx.RB_GROUP)
        self.opcao_media = wx.RadioButton(caixa, label="Média (5 perguntas)")
        self.opcao_dificil wx.RadioButton(caixa, label="Difícil (6 perguntas)")
        self.opcao_todas = wx.RadioButton(caixa, label="Todas as categorias (16 perguntas)")
        self.opcao_facil.SetValue(True)

        for opcao in (self.opcao_facil, self.opcao_media, self.opcao_dificil, self.opcao_todas):
            grupo.Add(opcao, flag=wx.ALL, border=8)

        self.botao_confirmar = wx.Button(painel, label="&Confirmar e começar")
        self.botao_confirmar.Bind(wx.EVT_BUTTON, self.ao_confirmar)
        self.botao_confirmar.SetDefault()

        self.botao_voltar = wx.Button(painel, label="&Voltar ao menu.")
        self.botao_voltar.Bind(wx.EVT_BUTTON, self.ao_voltar)

        layout.Add(grupo, flag=wx.EXPAND | wx.ALL, border=16)
        layout.Add(self.botao_confirmar, flag=wx.ALIGN_CENTER | wx.TOP, border=8)
        layout.Add(self.botao_voltar, flag=wx.ALIGN_CENTER | wx.TOP, border=8)

        painel.SetSizer(layout)
        wx.CallAfter(self.opcao_facil.SetFocus)

    def _categoria_escolhida(self):
        if self.opcao_facil.GetValue():
            return "facil"
        if self.opcao_media.GetValue():
            return "media"
        if self.opcao_dificil.GetValue():
            return "dificil"
        return "todas"

    def ao_confirmar(self, evento):
        try:
            from interface.tela_quiz import TelaQuiz

            tela = TelaQuiz(self._categoria_escolhida())
        except (ImportError, FileNotFoundError) as erro:
            wx.MessageBox(
                f"Não foi possível iniciar o quiz. \n\nDetalhe: {erro}",
                "Erro ao iniciar o quiz",
                wx.OK | wx.ICON_ERROR,
                self,
            )
            return
        tela.Show()
        self.Close()

    def ao_voltar(self, evento):
        from interface.tela_inicial import TelaInicial

        TelaInicial().Show()
        self.Close()

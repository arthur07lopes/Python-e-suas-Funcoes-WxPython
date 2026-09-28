import wx

from interface import tema

class TelaInicial(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Python e suas Funções - Menu Principal", size=(520, 380))
        self.SetBackgroundColour(tema.BRANCO)
        self._montar_layout()
        self.Centre()

    def _montar_layout(self):
        painel = wx.Panel(self)
        painel.SetBackgroundColour(tema.BRANCO)
        layout = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(painel, label="Python e suas Funçoes")
        fonte = titulo.GetFont()
        fonte.SetPointSize(tema.FONTE_TITULO_TAMANHO)
        fonte.MakeBold()
        titulo.SetFont(fonte)
        titulo.SetForegroundColour(tema.AZUL_PYTHON)

        subtitulo = wx.StaticText(painel, label="Um quiz acessível para aprender funções em Python")
        subtitulo.SetForegroundColour(tema.CINZA_TEXT)

        self.botao_iniciar = wx.Button(painel, label="&Iniciar Quiz")
        self.botao_documentacao = wx.Button(painel, label="&Ver documentação sobre o Python")
        self.botao_sair = wx.Button(painel, label="&Sair")

        self.botao_iniciar.Bind(wx.EVT_BUTTON, self.ao_clicar_iniciar)
        self.botao_documentacao.Bind(wx.EVT_BUTTON, self.ao_clicar_documentacao)
        self.botao_sair.Bind(wx.EVT_BUTTON, self.ao_clicar_sair)

        layout.Add(titulo, flag=wx.ALIGN_CENTER | wx.TOP, border=20)
        layout.Add(subtitulo, flag=wx.ALIGN_CENTER | wx.TOP, border=12)
        layout.Add(self.botao_iniciar, flag=wx.ALIGN_CENTER | wx.TOP, border=30)
        layout.Add(self.botao_documentacao, flag=wx.ALIGN_CENTER | wx.TOP, border=12)
        layout.Add(self.botao_sair, flag=wx.ALIGN_CENTER | wx.TOP, border=12)

        painel.SetSizer(layout)
        wx.CallAfter(self.botao_iniciar.SetFocus)

    def ao_clicar_iniciar(self, evento):
        from interface.tela_categorias import TelaCategorias

        TelaCategorias.Show()
        self.Close()

    def ao_clicar_documentacao(self, evento):
        from interface.tela_documentacao import TelaDocumentacao

        TelaDocumentacao(self).Show()
        self.Hide()

    def ao_clicar_sair(self, evento):
        self.Show()
        self.Raise()
        wx.CallAfter(self.botao_documentacao.SetFocus)

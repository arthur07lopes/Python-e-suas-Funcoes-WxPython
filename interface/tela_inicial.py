import wx

from interface.tema import aplicar_tema_janela, aplicar_tema_botao, FONTE_TITULO    

class TelaInicial(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Python e suas Funções", size=(500, 400))
        aplicar_tema_janela(self)
        painel = wx.Panel(self)
        aplicar_tema_janela(painel)
        organizador = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(painel, label="Python e suas Funções")
        titulo.SetFont(FONTE_TITULO)
        organizador.Add(titulo, 0, wx.ALL | wx.CENTER, 20)

        self.botao_iniciar = wx.Button(painel, label="Iniciar Quiz")
        self.botao_documentacao = wx.Button(painel, label="Documentação")
        self.botao_sair = wx.Button(painel, label="Sair")

        for botao in (self.botao_iniciar, self.botao_documentacao, self.botao_sair):
            aplicar_tema_botao(botao)
            organizador.Add(botao, 0, wx.ALL | wx.CENTER, 10)
        
        painel.SetSizer(organizador)

        self.botao_iniciar.Bind(wx.EVT_BUTTON, self.ao_clicar_iniciar)
        self.botao_documentacao.Bind(wx.EVT_BUTTON, self.ao_clicar_documentacao)
        self.botao_sair.Bind(wx.EVT_BUTTON, self.ao_clicar_sair)

    def ao_clicar_iniciar(self, evento):
        from interface.quiz import TelaCategorias
        tela = TelaCategorias()
        tela.Show()
        tela.Close()

    def ao_clicar_documentacao(self, evento):
        from interface.tela_documentacao import TelaDocumentacao
        tela = TelaDocumentacao()
        tela.Show()

    def ao_clicar_sair(self, evento):
        self.Close()

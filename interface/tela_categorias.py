import wx
from interface.tema import aplicar_tema_janela, aplicar_tema_botao
from dados.perguntas import obter_nome_categoria

class TelaCategorias(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Escolha a categoria", size=(450, 350))
        aplicar_tema_janela(self)
        painel = wx.Panel(self)
        organizador = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(painel, label="&Escolha a dificuldade")
        organizador.Add(titulo, 0, wx.ALL | wx.CENTER, 15)

        for categoria in (1, 2, 3):
            botao = wx.Button(painel, label=obter_nome_categoria(categoria))
            aplicar_tema_botao(botao)
            botao.Bind(wx.EVT_BUTTON, lambda evento, c=categoria: self.iniciar_quiz(c))
            organizador.Add(botao, 0, wx.ALL | wx.EXPAND, 10)

        painel.SetSizer(organizador)

    def iniciar_quiz(self, categoria):
        from interface.tela_quiz import TelaQuiz
        tela = TelaQuiz(categoria)
        tela.Show()
        self.Close()

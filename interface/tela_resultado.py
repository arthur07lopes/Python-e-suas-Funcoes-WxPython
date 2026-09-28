import wx
from interface.tema import aplicar_tema_janela, aplicar_tema_botao

class TelaResultado(wx.Frame):
    def __init__(self, pontuacao):
        super().__init__(None, title="Resultado", size=(450, 350))
        aplicar_tema_janela(self)
        self.pontuacao = pontuacao
        painel = wx.Panel(self)
        organizador = wx.BoxSizer(wx.VERTICAL)

        texto_resultado = (
            f"Você acertou {pontuacao.acertos} de {pontuacao.total()} questoes "
            f"({pontuacao.percentual_acerto()}%.)"
        )
        rotulo = wx.StaticText(painel, label=texto_resultado)
        rotulo.Wrap(400)
        organizador.Add(rotulo, 0, wx.ALL | wx.CENTER, 20)

        botao_revisar = wx.Button(painel, label="&Revisar erros")
        aplicar_tema_botao(botao_revisar)
        botao_revisar.Bind(wx.EVT_BUTTON, self.ao_revisar)
        organizador.Add(botao_revisar, 0, wx.ALL | wx.EXPAND, 10)

        botao_menu = wx.Button(painel, label="&Voltar ao menu")
        aplicar_tema_botao(botao_menu)
        botao_menu.Bind(wx.EVT_BUTTON, self.ao_voltar_menu)
        organizador.Add(botao_menu, 0, wx.ALL | wx.EXPAND, 10)

        painel.SetSizer(organizador)

    def ao_revisar(self, event):
        from interface_quiz.dialogo_revisao import DialogoRevisao
        dialogo = DialogoRevisao(self, self.pontuacao.erros_para_revisao())
        dialogo.ShowModal()
        dialogo.Destroy()

    def ao_voltar_menu(self, event):
        from interface.tela_inicial import TelaInicial
        tela = TelaInicial()
        tela.Show()
        self.Close()

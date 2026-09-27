import wx
from interface.tema import aplicar_tema_janela

TEXTO_DOCUMENTACAO = """Este quiz testa seus conhecimentos em Python.

Escolha uma categoria de dificuldade e responda às perguntas.
No final você verá sua pontuação e pode revisar os erros."""

class TelaDocumentacao(wx.Frame):
    def __init__(self):
        super().__init__(None, title="&Documentação", size=(450, 350))
        aplicar_tema_janela(self)
        painel = wx.Panel(self)
        organizador = wx.BoxSizer(wx.VERTICAL)

        caixa_texto = wx.TextCtrl(
            painel, value=TEXTO_DOCUMENTACAO,
            style=wx.TE_MULTILINE | wx.TE_READONLY
        )
        organizador.Add(caixa_texto, 1, wx.ALL | wx.EXPAND, 15)

        botao_fechar = wx.Button(painel, label="&Fechar")
        botao_fechar.Bind(wx.EVT_BUTTON, lambda evento: self.Close())
        organizador.Add(botao_fechar, 0, wx.ALL | wx.CENTER, 10)

        painel.SetSizer(organizador)

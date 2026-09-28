import wx

from interface.tema import aplicar_tema_janela

class DialogoRevisao(wx.Dialog):
    def __init__(self, parent, erros):
        super().__init__(parent, title="Revisão de erros", size=(500, 400))
        aplicar_tema_janela(self)
        organizador = wx.BoxSizer(wx.VERTICAL)

        texto = ""
        for item in erros:
            texto += f"Pergunta: {item['questao']}\n"
            texto += f"Sua resposta: {item['resposta_usuario']}\n"
            texto += f"Resposta correta: {item['correta']}\n"

        if texto == "":
            texto = "Você não errou nenhuma questão. Parabéns! :D"

        caixa_texto = wxTextCtrl(
            self, value=texto, style=wx.TE_MULTILINE | wx.TE_READONLY
        )
        organizador.Add(caixa_texto, 1, wx.ALL | wx.EXPAND, 15)

        botao_fechar = wx.Button(self, label="&Fechar", id=wx.ID_OK)
        organizador.Add(botao_fechar, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(organizador)

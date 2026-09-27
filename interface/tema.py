import wx

COR_FUNDO = wx.Colour(255, 255, 255)
COR_TEXTO = wx.Colour(30, 30, 30)
COR_PRIMARIA = wx.Colour(48, 105, 152)
COR_SECUNDARIA = wx.Colour(255, 212, 59)
COR_ERRO = wx.Colour(200, 50, 50)
COR_SUCESSO = wx.Colour(46, 139, 87)

FONTE_TITULO = wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
FONTE_TEXTO = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

def aplicar_tema_janela(janela):
    janela.SetBackgroundColour(COR_FUNDO)
    janela.SetForegroundColour(COR_TEXTO)

def aplicar_tema_botao(botao, destaque=False):
    if destaque:
        botao.SetBackgroundColour(COR_PRIMARIA)
        botao.SetForegroundColour(wx.Colour(255, 255, 255))
    else:
        botao.SetBackgroundColour(COR_SECUNDARIA)
        botao.SetForegroundColour(COR_TEXTO)
    botao.SetFont(FONTE_TEXTO)

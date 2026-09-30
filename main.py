import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import wx

from interface.teça_inicial import TelaInicial

class AplicativoQuiz(wx.app):
  def OnInit(self):
    self.tela_inicial = TelaInicial()
    self.tela_inicial.Show()
    self.SetTopWindow(self.tela_inicial)
    return True

  def principal():
    app = AplicativoQuiz()
    app.MainLoop()

if __name__ == "__main__":
  principal()

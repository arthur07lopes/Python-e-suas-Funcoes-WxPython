import wx
from interface.tema import aplicar_tema_janela, aplicar_tema_botao
from logica.motor_quiz import MotorQuiz

class TelaQuiz(wx.Frame):
    def __init__(self, categoria):
       super().__init__(None, title="Quiz", size=(550,450))
       aplicar_tema_janela(self)
       self.motor = MotorQuiz(categoria)
       self.painel = wx.Panel(self)
       self.organizador = wx.BoxSizer(wx.VERTICAL)
       self.montar_questao()

    def montar_questao(self):
        self.organizador.Clear(True)
        questao = self.motor.questao_atual()

        if questao is None:
            self.mostrar_resultado()
            return

        respondida, total = self.motor.progresso()
        rotulo_progresso = wx.StaticText(
            self.painel, label=f"Pergunta {respondida + 1} de {total}"
        )
        self.organizador.Add(rotulo_progresso, 0, wx.ALL, 10)

        texto_questao = wx.StaticText(self.painel, label=questao["questao"])
        texto_questao.Wrap(480)
        self.organizador.Add(texto_questao, 0, wx.ALL, 10)

        self.grupo_opcoes = []
        primeira = True
        for letra, texto in questao["alternativas"].items():
            opcao = wx.RadioButton(
                self.painel, label=f"{letra.upper()}) {texto}", style=estilo
            )
            opcao.letra = letra
            self.grupo_opcoes.append(opcao)
            self.organizador.Add(opcao, 0, wx.ALL, 8)
            primeira = False

        botao_confirmar = wx.Button(self.painel, label="&Confirmar resposta")
        aplicar_tema_botao(botao_confirmar, destaque=True)
        botao_confirmar.Bind(wx.EVT_BUTTON, self.ao_clicar_confirmar)
        self.organizador.Add(botao_confirmar, 0, wx.ALL | wx.CENTER, 15)

        self.painel.Layout()

    def ao_confirmar(self, evento):
        letra_escolhida = None
        for opcao in self.grupo_opcoes:
            if opcao.GetValue():
                letra_escolhida = opcao.letra
        if letra_escolhida is None:
            wx.MessageBox("Escolha uma alternativa antes de confirmar.", "Aviso")
            return
        self.motor.responder(letra_escolhida)
        self.montar_questao()

    def mostrar_resultado(self):
        from interface.tela_resultado import TelaResultado
        tela = TelaResultado(self.motor.pontuacao)
        tela.Show()
        self.Close()

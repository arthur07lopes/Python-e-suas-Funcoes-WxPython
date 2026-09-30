import wx

from interface import tema
from logica.motor_quiz impotr MotorQuiz

LETRAS = ["a", "b", "d"]
NOME_DA_CATEGORIA = {1: "fácil", 2: "média", 3: "difícil"}

class TelaQuiz(wx.Frame):
    def __init__(self, categoria):
        motor = MotorQuiz(categoria)
        super().__init__(
            None,
            title="Python e suas Funções - Quiz",
            size=(980, 680),
        )
        self.motor = motor
        self.aguardando_proxima = False
        self.SetBackgroundColour(tema.BRANCO)
        self._montar_layout()
        self._exibir_pergunta_atual()
        self.Centre()

    def _montar_layout(self):
        self.painel = wx.Panel(self)
        self.painel.SetBackgroundColour(tema.BRANCO)
        layout = wx.BoxSizer(wx.VERTICAL)

        rotulo_pergunta = wx.StaticText(self.painel, label="Pergunta")
        rotulo_pergunta.SetForegroundColour(tema.AZUL_PYTHON)

        self.caixa_pergunta = wx.TextCtrl(
            self.painel,
            style=wx.TE_MULTILINE | wx.TE_READONLY,
            size=(840, 200),
        )
        self.caixa_pergunta.SetName("Pergunta")

        grupo = wx.StaticBoxSizer(wx.VERTICAL, self.painel, "Alternativas")
        caixa_alternativas = grupo.GetStaticBox()

        self.opcoes_radio = []
        for indice in range(len(LETRAS)):
            estilo = wx.RB_GROUP if indice == 0 else 0
            radio = wx.RadioButton(caixa_alternativas, label="", style=estilo)
            grupo.Add(radio, flag=wx.ALL, border=6)
            self.opcoes_radio.append(radio)

        self.botao_confirmar = wx.Button(self.painel, label="&Confirmar resposta")
        self.botao_confirmar.Bind(wx.EVT_BUTTON, self.ao_clicar_botao)
        self.botao_confirmar.SetDefault()

        layout.Add(rotulo_pergunta, flag=wx.LEFT | wx.TOP, border=16)
        layout.Add(self.caixa_pergunta, proportion=1, flag=wx.EXPAND | wx.ALL, border=16)
        layout.Add(grupo, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=16)
        layout.Add(self.botao_confirmar, flag=wx.ALIGN_CENTER | wx.ALL, border=16)
        
        self.painel.SetSizer(layout)

    def _texto_da_pergunta(self, mensagem=""):
        pergunta = self.motor.pergunta_atual
        numero = self.motor.indice_pergunta_atual + 1
        total = self.motor.total_de_perguntas
        categoria = NOME_DA_CATEGORIA[pergunta["categoria"]]
        tentativa = self.motor.tentativas_usadas + 1

        partes = []
        if mensagem:
            partes.append(mensagem)
        partes.append(
            f"Pergunta {numero} de {total}, dificuldade {categoria}.",
            f"Tentativa {tentativa} de 3."
        )
        partes.append(pergunta["pergunta"])
        return "\n\n".join(partes)

    def _exibir_pergunta_atual(self):
        pergunta = self.motor.pergunta_atual
        self.aguardando_proxima = False

        self.caixa_pergunta.SetValue(self._texto_da_pergunta())

        for letra, radio in zip(LETRAS, self.opcoes_radio):
            texto = f"{letra}") {pergunta['alternativas'][letra]}"
            radio.SetLabel(texto.replace("&", "&&"))
            radio.SetValue(False)
            radio.Enable()
        self.opcoes_radio[0].SetValue(True)

        self.botao_confirmar.SetLabel("&Confirmar resposta")
        self.painel.Layout()
        wx.CallAfter(self.caixa_pergunta.SetFocus)

    def ao_clicar_botao(self, evento):
        if self.aguardando_proxima:
            self._ir_para_proxima_pergunta_ou_resultado()
        else:
            self._confirmar_resposta()

    def _confirmar_resposta(self):
        indice = next(
            (i for i, radio in enumerate(self.opcoes_radio) if radio.GetValue()),
            0,
        )
        resultado = self.motor.responder(LETRAS[indice])

        if resultado == "acertou":
            self._tratar_acerto()
        elif resultado == "errou_tem_mais_tentativas":
            self._tratar_erro_com_tentativas_restantes()
        else:
            self._tratar_esgotamento_de_tentativas()

    def _tratar_acerto(self):
        ultimo = self.motor.pontuacao.historico[-1]
        eh_ultima = self.motor.indice_pergunta_atual + 1 >= self.motor.total_de_perguntas

        self.aguardando_proxima = True
        for radio in self.opcoes_radio:
            radio.Disable()

        self.caixa_pergunta.SetValue(
            f"Resposta correta! Você ganhou {ultimo['pontos_ganhos']} pontos. "
            f"Pontuação total: {self.motor.pontuacao.total} pontos."
        )
        self.botao_confirmar.SetLabel("&Ver resultado" if eh_ultima else "&Próxima pergunta")
        self.painel.Layout()
        wx.CallAfter(self.caixa_pergunta.SetFocus)

    def _tratar_erro_com_tentativas_restantes(self):
        restantes = self.motor.tentativas_restantes
        self.caixa_pergunta.SetValue(
            self._texto_da_pergunta(
                f"Resposta incorreta. Você ainda tem {restantes} tentativa(s)."
            )
        )
        wx.CallAfter(self.caixa_pergunta.SetFocus)

    def _tratar_esgotamento_de_tentativas(self):
        from interface.dialogo_revisao import DialogoRevisao

        dialogo = DialogoRevisao(
            self,
            self.motor.pergunta_atual,
            self.motor.respostas_erradas_dadas,
        )
        dialogo.ShowModal()
        dialogo.Destroy()
        self._ir_para_proxima_pergunta_ou_resultado()

    def _ir_para_proxima_pergunta_ou_resultado(self):
        self.motor.avancar_para_proxima_pergunta()
        if self.motor.acabou:
            from interface.tela_resultado import TelaResultado

            TelaResultado(self.motor.pontuacao).Show()
            self.Close()
        else:
            self._exibir_pergunta_atual()

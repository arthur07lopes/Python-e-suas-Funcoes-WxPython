import wx
from interface import tema

TEXTO_DOCUMENTACAO = """O que é o Python?

Python é uma linguagem de programação de alto nível, criada por Guido Van Rossum e 
lançada em 1991. Sua sintaxe é simples e legível, 
o que a torna uma das melhores linguagens para quem está começando a programar.

Onde o Python é aplicado?

Ciência de dados e inteligencia artificial, desenvolvimento 
web, automação de tarefas do dia a dia e também programas
com interface gráfica, como este prórpio quiz.

O que são Funções?

Uma função é um bloco de código com um nome, que pode ser
executado sempre que for preciso, sem reescrever o mesmo
código. Como por exemplo:

 def somar (a, b):
     return a + b
 resultado = somar(2,3)
 print(resultado)

A palavra def cria a função, return devolve o resultado, e
somar(2, 3) chama a função. O print é uma função que já vem
pronta no Python.

Como Funciona o Quiz?

São 16 perguntas: 5 fáceis, 5 médias e 6 difíceis. Cada pergunta tem 4 alternativas e você tem 3 tentativas. Acertar
de primeira vale a pontuacao inteira, acertar na segunda vale por 60 por cento e na terceira, 30 por cento. Se
as 3 tentativas acabarem, uma janela mostra a resposta correta e o motivo."""

class TelaDocumentacao(wx.Frame):
    def __init__(self, tela_anterior):
        super().__init__(
            None,
            title="Documentação - Sobre o Python",
            size=(640, 560),
        )
        self.tela_anterior = tela_anterior
        self.SetbackgroundColour(tema.BRANCO)
        self.montar_layout()
        self.Bind(wx.EVT_CLOSE, self.ao_fechar)
        self.Centre()

    def mostrar_layout(self):
        painel = wx.Panel(self)
        painel.SetBackgroundColour(tema.BRANCO)
        layout = wx.BoxSizer(wx.VERTICAL)

        rotulo = wx.StaticText(painel, label="Sobre o Python")
        rotulo.SetForegroundColour(tema.AZUL_PYTHON)

        self.caixa_texto = wx.TextCtril(
            painel,
            value=TEXTO_DOCUMENTACAO,
            style=wx.TE_MULTILINE | wx.TE_READONLY,
            size=(580, 380),
        )
        self.caixa_texto.SetName("Texto da documentação sobre o Python")

        self.botao_voltar = wx.Button(painel, label="&Voltar ao menu")
        self.botao_voltar.Bind(wx.EVT_BUTTON, self.ao_clicar_voltar)

        layout.Add(rotulo, flag=wx.ALL | wx.ALIGN_CENTER, border=12)
        layout.Add(self.caixa_texto, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=16)
        layout.Add(self.botao_voltar, flag=wx.ALL | wx.ALIGN_CENTER, border=14)

        painel.SetSizer(layout)
        wx.CallAfter(self.caixa_texto.SetFocus)

    def ao_clicar_voltar(self, evento):
        self.tela_anterior.voltar_a_exibir()
        self.Destroy()

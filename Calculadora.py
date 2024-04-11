# Importa tkinter
from tkinter import *
from tkinter import ttk
# cores
cor1 = "#1e1f1e"  # cor preta
cor2 = "#feffff"  # cor branca
cor3 = "#C1C1C1"  # cor azul carregado
cor4 = "#eceff1"  # cor cinza
cor5 = "#73A3C9"  # cor laranja
cor6 = "#DADBDA" # novo cinza
#Janelas tkinter
janela =Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)
#Frames
frame_tela = Frame(janela, width=335, height=50, bg=cor3 )
frame_tela.grid(row=0, column=0)
frame_quadro = Frame(janela, width=335, height=298)
frame_quadro.grid(row=1, column=0)
# Variavel
todos_valores = ''
#Label
valores_texto = StringVar()
# Função
def valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    # O valor na tela
    valores_texto.set(todos_valores)
# Função de calculo
def calcular():
    resultados = eval(todos_valores)
    valores_texto.set(int(resultados))
    valores_texto.set(str(resultados))
#Limpando tela
def limpando_tela():
    global todos_valores
    todos_valores =""
    valores_texto.set("")
app_label = Label(frame_tela, textvariable=valores_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '),bg=cor3,fg=cor1)
app_label.place(x=0, y=0)
#Botões
botão1 = Button(frame_quadro, command = limpando_tela, text="C", width=11, height=2,  bg=cor4 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botão1.place(x=0, y=0)
botão2 = Button(frame_quadro, command = lambda: valores('%'), text="%", width=5, height=2, bg=cor6 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botão2.place(x=118, y=0)
botão3 = Button(frame_quadro, command = lambda: valores('/'), text="/", width=5, height=2, bg=cor6, fg=cor1 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botão3.place(x=177, y=0)
#
botão4 = Button(frame_quadro, command = lambda: valores('7'), text="7", width=5, height=2, bg=cor4 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botão4.place(x=0, y=52)
botão5 = Button(frame_quadro, command = lambda: valores('8'), text="8", width=5, height=2, bg=cor4 ,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão5.place(x=59, y=52)
botão6 = Button(frame_quadro, command = lambda: valores('9'), text="9", width=5, height=2, bg=cor4 ,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão6.place(x=118, y=52)
botao7 = Button(frame_quadro, command = lambda: valores('*'), text="*", width=5, height=2, bg=cor6, fg=cor1 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botao7.place(x=177, y=52)
#
botão9 = Button(frame_quadro, command = lambda: valores('4'), text="4", width=5, height=2, bg=cor4 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botão9.place(x=0, y=104)
botão10 = Button(frame_quadro, command = lambda: valores('5'), text="5", width=5, height=2, bg=cor4 ,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão10.place(x=59, y=104)
botão11 = Button(frame_quadro, command = lambda: valores('6'), text="6", width=5, height=2, bg=cor4 ,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão11.place(x=118, y=104)
botao12 = Button(frame_quadro, command = lambda: valores('-'), text="-", width=5, height=2, bg=cor6, fg=cor1 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botao12.place(x=177, y=104)
#
botão14 = Button(frame_quadro, command = lambda: valores('1'), text="1", width=5, height=2, bg=cor4 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botão14.place(x=0, y=156)
botão15 = Button(frame_quadro, command = lambda: valores('2'), text="2", width=5, height=2, bg=cor4 ,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão15.place(x=59, y=156)
botão16 = Button(frame_quadro, command = lambda: valores('3'), text="3", width=5, height=2, bg=cor4 ,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão16.place(x=118, y=156)
botao17 = Button(frame_quadro, command = lambda: valores('+'), text="+", width=5, height=2, bg=cor6, fg=cor1 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botao17.place(x=177, y=156)
#
botão19 = Button(frame_quadro, command = lambda: valores('0'), text="0", width=11, height=2,  bg=cor4 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botão19.place(x=0, y=208)
botão20 = Button(frame_quadro, command = lambda: valores('.'), text=".", width=5, height=2, bg=cor4 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botão20.place(x=118, y=208)
botão21 = Button(frame_quadro, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor1 ,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
botão21.place(x=177, y=208)
janela.mainloop()





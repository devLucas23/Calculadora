import tkinter as tk
from tkinter import *
"""Essas linhas importam os módulos tkinter e *
Isso permite que você utilize as classes e funções do tkinter 
sem ter que digitar tkinter. antes de cada chamada."""

numero1 = ''
numero2 = ''
adicao = FALSE
subtracao = FALSE
multiplicacao = FALSE
divisao = FALSE
"""Essas variáveis são utilizadas para armazenar os números e
   os operadores selecionados durante o cálculo"""

root = Tk()
root.title('Calculadora')
root.geometry("408x355")
root.maxsize(408, 355)
root.minsize(408, 355)
root.configure(background='#282828')
"""Essas linhas criam a janela principal da 
   calculadora utilizando a classe Tk() do Tkinter
   O método title() define o título da janela como 'Calculadora'
   O método geometry() define o tamanho inicial da janela
   O método maxsize() e minsize() definem as dimensões máximas e mínimas da janela
   O método configure() define o fundo da janela como cinza escuro."""

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',
          bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)
"""Essas linhas criam um widget de entrada para exibir e 
   receber os números e resultados da calculadora
   """

def botao_click(num):
    e.insert(END, num)
"""Essa função é chamada quando um dos botões numéricos é clicado
Ela insere o número correspondente no final do widget de entrada"""

def botao_adiciona():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = e.get()
    e.delete(0, END)
"""Essa função é chamada quando o botão de adição é clicado
   Ela define a variável adicao como TRUE, armazena 
   o número atual no numero1 e limpa o widget de entrada"""

def botao_subrai():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_multiplica():
    global numero1
    global multiplicacao
    multiplicacao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_divide():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)
"""As outras funções botao_subrai(), botao_multiplica(), e botao_divide()
   são semelhantes à função botao_adiciona() mas para os operadores de 
   subtração, multiplicação e divisão, respectivamente"""

def botao_igual():
    global subtracao
    global divisao
    global multiplicacao
    global adicao
    numero2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adicao = FALSE
    if multiplicacao == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) // int(numero2))
        divisao = FALSE
"""Essa função é chamada quando o botão de igualdade é clicado
   Ela verifica qual operador foi selecionado 
   (com base nas variáveis booleanas) e realiza o cálculo
   apropriado com os números numero1 e numero2 o resultado 
   é inserido no widget de entrada (Entry) e as variáveis
   booleanas são redefinidas como FALSE"""

def botao_limpa():
    e.delete(0, END)
"""Essa função é chamada quando o botão de limpar (C) é clicado
   Ela limpa o widget de entrada (Entry), removendo qualquer número ou resultado atual"""

def botao_num(num, row, column):
    botao = Button(root,
                   text=num,
                   padx=40,
                   pady=20,
                   command=lambda: botao_click(num),
                   fg='#FFFFFF',
                   activebackground='#240046',
                   activeforeground='#FFFFFF',
                   bg='#282828',
                   relief=FLAT,
                   font=('futura', 12, 'bold'))
    botao.grid(row=row, column=column)
"""Essa função é usada para criar e posicionar os botões numéricos na calculadora"""

def botao_operador(op, command, row, column):
    operador = Button(root,
                      text=op,
                      padx=40,
                      pady=20,
                      command=command,
                      fg='#FFFFFF',
                      activebackground='#240046',
                      activeforeground='#FFFFFF',
                      bg='#320064',
                      relief=FLAT,
                      font=('futura', 12, 'bold'))
    operador.grid(row=row, column=column)
"""Essa função é usada para criar e posicionar os botões de operadores na calculadora"""

botao_operador('÷', botao_divide, 0, 4)
# primeira fileira
botao_num(1, 1, 1)
botao_num(2, 1, 2)
botao_num(3, 1, 3)
botao_operador('×', botao_multiplica, 1, 4)
# segunda fileira
botao_num(4, 2, 1)
botao_num(5, 2, 2)
botao_num(6, 2, 3)
botao_operador(' -', botao_subrai, 2, 4)
# terceira fileira
botao_num(7, 3, 1)
botao_num(8, 3, 2)
botao_num(9, 3, 3)
botao_operador('+', botao_adiciona, 3, 4)
# quarta fileira
zero = Button(root,
              text='0',
              padx=91,
              pady=20,
              command=lambda: botao_click(0),
              fg='#FFFFFF',
              activebackground='#240046',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
zero.grid(row=4, column=1, columnspan=2)
botao_operador('C', botao_limpa, 4, 4)
botao_operador('=', botao_igual, 4, 3)
"""Essas linhas criam e posicionam os botões da calculadora"""
root.mainloop()
#Essa linha inicia o loop principal da janela
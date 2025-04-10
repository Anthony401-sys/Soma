#coding:utf-8

import tkinter as tk
import PalhetaCores as PC
from tkinter import messagebox

def TruncadorStringNumerica(Resultado, Ncasas):	
	if Resultado.find('.')==-1: #Retorna -1 se nao houver ponto
		return Resultado
	div = Resultado.split(".")
	ParteInteira = div[0]
	ParteFrac = div[1]
	if ParteFrac=='0': 
		return ParteInteira
	else:
		return ParteInteira+"."+ParteFrac[:Ncasas]		 
		
	'''
	Resultado=Resultado.split(".")
	ParteInteira = Resultado[0]	
	ParteFrac = Resultado[1] 
	FlagInt = False
	if ParteFrac=='0': 
		FlagInt = True
	strg = ''
	if FlagInt:
		strg = ParteInteira
	else: 
		strg = ParteInteira+"."+ParteFrac[0:Ncasas]	
	return(strg)	 
	'''
 
def _command_SetButton(): 
	valor = RadioButtonVar.get()
	if valor ==1: 
		tk.messagebox.showinfo("Modo Calc", "Saida com expressao")#Titulo, informacao
	else:
		tk.messagebox.showinfo("Modo Calc", "Saida simples")#Titulo, informacao	
#	tk.messagebox.showinfo("Modo Calc", "Saida simples")#Titulo, informacao
#	print("valor = ", RadioButtonVar.get())
	

def _command_limpar():
	valor_visor2.set("0")
	strg1 = str(valor_visor1.get())
	valor_visor1.set("ants = " + str(strg1))

def _command_tecla(evento):#Evento é string
	strg = valor_visor2.get()
	if strg == "Calculadora ligada":
		valor_visor2.set("")
	valor_visor2.set(valor_visor2.get()+evento)

#Funcao para o botao =
def _command_calcular():
	Ncasas = 3
	strg = valor_visor2.get()
	resultado = str(eval(strg))
	strg+="="
	SaidaTruncada=TruncadorStringNumerica(resultado, Ncasas)
	strg+=str(SaidaTruncada)
	if RadioButtonVar.get()==1: 
		valor_visor2.set(str(SaidaTruncada))
		strg2 = str(SaidaTruncada) + "=" + strg
		strg2.split("=")
		valor_visor1.set(str(strg2[1]))
	else: 	
		valor_visor2.set(strg)
	strg2 = strg +"="+SaidaTruncada
	strg2 = strg2.split("=")
	P_visor = strg2[1]
	valor_visor1.set(P_visor)

janela = tk.Tk()
janela.title("Calc parte 2")
janela.geometry("240x500") #Comprimento e altura em pixels da janela

#Criacao do frame visor
frame_visor=tk.Frame(janela, width = 240, height = 200, bg=PC.CorCinzaClaro )#Criei o widget
					#bg = background - cor de fundo. 
frame_visor.grid(row = 0, column =0) #Insere o frame usando grid

valor_visor2= tk.StringVar() #Variavel para entrar no visor 
valor_visor2.set("Calculadora ligada")
visor_label2 = tk.Label(frame_visor, textvariable= valor_visor2, width = 28, height = 2, padx = 7)
visor_label2.place(x=0, y=0) 

valor_visor1 = tk.StringVar()
valor_visor1.set("")
visor_label1 = tk.Label(frame_visor, textvariable= valor_visor1, width = 28, height = 2, padx = 7)
visor_label1.place(x=0, y=50)

#Introducao do radiobutton
RadioButtonVar = tk.IntVar()
RB1=tk.Radiobutton(frame_visor, text = "Modo 1", variable = RadioButtonVar, value = 1, command=_command_SetButton)
RB1.place(x=0, y=0)
RB2=tk.Radiobutton(frame_visor, text = "Modo 2", variable = RadioButtonVar, value = 2, command=_command_SetButton)
RB2.place(x=0, y=50)

#Criacao do frame botoes
frame_botoes = tk.Frame(janela, width = 240, height = 300, bg = PC.CorCinzaEscuro)
frame_botoes.grid(row = 1, column =0)

#Inclusao dos botoes
#Linha 1
Botao_11 = tk.Button(frame_botoes, text = "Limpar", width = 11, height = 2, command=_command_limpar)
Botao_11.place(x=0, y=0) #Posicao do botao 11 em pixels
Botao_12 = tk.Button(frame_botoes, text = "mod", width = 4, height = 2, command=lambda:_command_tecla("%"))
Botao_12.place(x=116, y=0) #Posicao do botao 11 em pixels
Botao_13 = tk.Button(frame_botoes, text = "div", width = 4, height = 2, bg = PC.CorLaranja, command=lambda:_command_tecla("/"))
Botao_13.place(x=176, y=0) #Posicao do botao 11 em pixels

#Linha 2
Botao_21=tk.Button(frame_botoes, text = '7', width = 4, height= 2, command=lambda:_command_tecla("7"))
Botao_21.place(x=0, y=52)
Botao_22=tk.Button(frame_botoes, text = '8', width = 4, height= 2, command=lambda:_command_tecla("8")).place(x=60, y=52)
Botao_23=tk.Button(frame_botoes, text = '9', width = 4, height= 2, command=lambda:_command_tecla("9")).place(x=120, y=52)
Botao_24=tk.Button(frame_botoes, text = '*', width = 4, height= 2, bg = PC.CorLaranja, command=lambda:_command_tecla("*")).place(x=180, y=52)

#Linha 3
Botao_31=tk.Button(frame_botoes, text = '4', width = 4, height= 2, command=lambda:_command_tecla("4"))
Botao_31.place(x=0, y=52*2)
Botao_32=tk.Button(frame_botoes, text = '5', width = 4, height= 2, command=lambda:_command_tecla("5")).place(x=60, y=52*2)
Botao_33=tk.Button(frame_botoes, text = '6', width = 4, height= 2, command=lambda:_command_tecla("6")).place(x=120, y=52*2)
Botao_34=tk.Button(frame_botoes, text = '-', width = 4, height= 2, bg = PC.CorLaranja, command=lambda:_command_tecla("-")).place(x=180, y=52*2)

#Linha 4
Botao_41=tk.Button(frame_botoes, text = '1', width = 4, height= 2,command=lambda:_command_tecla("1"))
Botao_41.place(x=0, y=52*3)
Botao_42=tk.Button(frame_botoes, text = '2', width = 4, height= 2,command=lambda:_command_tecla("2")).place(x=60, y=52*3)
Botao_43=tk.Button(frame_botoes, text = '3', width = 4, height= 2,command=lambda:_command_tecla("3")).place(x=120, y=52*3)
Botao_44=tk.Button(frame_botoes, text = '+', width = 4, height= 2, bg = PC.CorLaranja,command=lambda:_command_tecla("+")).place(x=180, y=52*3)

#Linha 5
Botao_51=tk.Button(frame_botoes, text = '0', width = 4, height= 2,command=lambda:_command_tecla("0"))
Botao_51.place(x=0, y=52*4)
Botao_52=tk.Button(frame_botoes, text = '00', width = 4, height= 2,command=lambda:_command_tecla("00")).place(x=60, y=52*4)
Botao_53=tk.Button(frame_botoes, text = '.', width = 4, height= 2,command=lambda:_command_tecla(".")).place(x=120, y=52*4)
Botao_54=tk.Button(frame_botoes, text = '^', width = 4, height= 2, bg = PC.CorLaranja,command=lambda:_command_tecla("**")).place(x=180, y=52*4)

#Linha 6
Botao_61=tk.Button(frame_botoes, text = '=', width = 25, height= 1, command=_command_calcular)
Botao_61.place(x=5, y=52*5)


janela.mainloop()



















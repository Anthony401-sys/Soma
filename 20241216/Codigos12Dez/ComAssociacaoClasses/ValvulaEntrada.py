#coding: utf-8

'''
Controlador de entrada de agua
'''

class ValvulaEntradaAgua(object):
	def __init__(self): 
		self.EstadoValvulaEntrada = "Fechado"
		print("\tValvula de entrada instalada")
	
	def Abrir_ValvulaEntrada(self): 
		self.EstadoValvulaEntrada ="Aberto"

	def Fechar_ValvulaEntrada(self): 
		self.EstadoValvulaEntrada ="Fechado"
		
	def get_estado_valvula_entrada(self):
		return 	self.EstadoValvulaEntrada
			

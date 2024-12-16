#coding: utf-8

class ControleAcionamento(object): 
	def __init__(self): 
		print("\tInstalado o controle de acionamento")
		self.contador1= 0
		self.contador2= 0
	
	def AcionarAlavanca(self, opcao): 
		if opcao == '1':
			self.contador1+=1
		else: 
			self.contador2+=1
	
	def get_acionamentos_feitos(self): 
		print("Numero de xixis: ", self.contador1)
		print("Numero de cocôs: ", self.contador1)				

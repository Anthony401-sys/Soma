#coding: utf-8
def CompreensaoLista1():
	nomes = ['Larissa', "Rafael", "Marcos", "Joao"]
	Strg_apr = " Aprovado"
	nomes_aprovados = []
	for nome in nomes: 
		saida = nome+Strg_apr
		nomes_aprovados.append(saida)
	print(nomes_aprovados)	
	nomes2 = ["Ana", "Carla", "Rotundo", "Henrique"]
	Strg_repr = " Reprovado"
	nomes_reprovados = [nome+Strg_repr for nome in nomes2]
	print(nomes_reprovados)

def aprovar_pessoa(nome): 
	strg = " Aprovado"
	return nome+strg


def CompreensaoLista2(): 
	nomes = ['Larissa', "Rafael", "Marcos", "Joao"]
	nomes2 = ["Ana", "Carla", "Rotundo", "Henrique"]
	def reprovar_pessoa(nome): 
		strg = " Reprovado"
		return nome+strg

	nomes_apr = [aprovar_pessoa(nome) for nome in nomes]
	nomes_rep = [reprovar_pessoa(nome) for nome in nomes2]
	print("Aprovados: ") 
	print(nomes_apr) 	
	print("Reprovados: ")
	print(nomes_rep)

def CompreensaoLista3(): 
	'''
	nomes = ['Larissa', "Rafael", "Marcos", "Joao"]
	nomes2 = [aprovar_pessoa(nome) for nome in nomes if (nome!='Rafael')]
	print(nomes2)
	lista1 = [1,5,15,19]
	lista2 = (0,2,18)
	numeros = [i for i in range(20) if i not in (lista1+list(lista2))]
	print(numeros)
	'''
	def eh_par(num):
		if (num%2==0):
			return True
		else:
			return False
	num2 = [i for i in range(20) if eh_par(i)]
	print(num2)
	'''
	for i in range(20): 
		print(i%2, end = " ")
	print()
	for i in range(20): 	
		print(i%3, end=" ")
	print()		
	'''	
	
if __name__=="__main__": 
	CompreensaoLista3()
	#CompreensaoLista2()
	#CompreensaoLista1()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

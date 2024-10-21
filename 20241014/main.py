#coding: utf=8

def scr0():
	vA = [] # Vetor vazio e de tamanho 0
	vB = [ None ] * 5 # Vetor vazio de tamanho 5
	vC = [1 , 3.4 , "A" , " IFSC ", 3.4 ] #vetor de
		# tamanho 4 e com tipos diferentes
	print ( vA ) # Imprime o vetor vA
	print ( vB ) # Imprime o vetor vB
	print ( vC ) # Imprime o vetor vC
	print("Numero de vezes que aparece 3.4:", vC.count(3.4))
	print("Posição de 3.4: ",vC.index(3.4))

def scr1(): #Tuplas e listas
	Lista1 = ["Rampa", "Descida", 11.34]
	Tupla1 = (1 , 3.4 , "A" , " IFSC " ) #tupla de
	print(Lista1)
	Lista1[1]="Subida"
	print("Lista 1 modificada", end = " ") 
	print(Lista1)	
	print ( Tupla1 ) # Imprime a tupla tB	
	Tupla1[1] = 2.09
	print("Tupla 1 modificada", end = " ") 
	print ( Tupla1 ) # Imprime a tupla tB	

def SaidaFuncao():
	a = 2.4
	b = 3.5
	return [a,b]

def Comando_in_paraBuscas():
	frutas = ['maçã', 'abacate', 'açaí', 'pêra']
	print('maçã' in frutas)
	print('cajá' not in frutas)#mesmo que print(’cajá’ not in frutas)
	fruta_teste = "abacate"
	if (fruta_teste not in frutas):
		frutas.append(fruta_teste)	
		print(f"{fruta_teste} adicionado ao vetor")
	else: 
		print(f"{fruta_teste} já está no vetor")	
	print(frutas)
	
def Comando_in_percorrimento():
	vC = [1 , 3.4 , 'A' , " IFSC " ]
	for i in vC :
		print ( type(i) )	

def Comando_Enumerate():
	moedas = ["BRL", "USD", "EUR"]
	for i, moeda in enumerate(moedas):
		print(i, moeda)	
	for saida in enumerate(moedas): 
		print(saida)				

if __name__=="__main__":
	Comando_Enumerate()
	#Comando_in_percorrimento()
	#Comando_in_paraBuscas()
	#scr0()	
	#scr1()
	#saida = SaidaFuncao()
	#print(saida)

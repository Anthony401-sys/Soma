'''
lista = [1,2,3,4,5]
n1,n2, *n, n3 = lista
print(n1,n2, n, n3)
'''
def explo_funcao(*args): #Empacota os valores.
	print(args)
	#Imprime os valores empacotados.
	print(*args)
	#Imprime os valores desempacotados.
	#Calculo da media:
	media = 0
	for i in range(len(args)): 
		media+=args[i]
	print("Media = ", media/len(args))	

def Troca_de_variaveis(a,b): 
	print("a = ", a)
	print("b = ", b)
	#a,b = b,a
	temp = b
	b = a
	a = temp
	
	
	print("a = ", a)
	print("b = ", b)
	

if __name__=="__main__": 
	#explo_funcao(1,2,3,4,5,10)
	Troca_de_variaveis(2,5) 
	




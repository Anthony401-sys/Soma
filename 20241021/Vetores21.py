#coding:utf-8


def script01(): 
	vC = [1 , 3.4 , 'A' , " IFSC " ]
	print(vC)
	input("Pressione enter para continuar")
	print("Inserção de 56 na posicao 0")
	vC.insert(0,56)
	print(vC)
	input("Pressione enter para continuar")
	print("Insercao de B na posicao 3") 
	vC.insert(3,'B')
	print(vC)
	input("Insercao no final do vetor de 11")
	vC.append(11)
	print(vC)
	return vC

def script01_limpo(): 
	vC = [1 , 3.4 , 'A' , " IFSC " ]
	#print(vC)
	#input("Pressione enter para continuar")
	#print("Inserção de 56 na posicao 0")
	vC.insert(0,56)
	#print(vC)
	#input("Pressione enter para continuar")
	#print("Insercao de B na posicao 3") 
	vC.insert(3,'B')
	#print(vC)
	#input("Insercao no final do vetor de 11")
	vC.append(11)
	vC.append("A")
	#print(vC)
	return vC

def script02(vetA): 
	print("Vetor recebido: ", vetA)
	print("Remocao do valor, ", vetA[2])
	valor = 1.4
	if valor in vetA: 
		vetA.remove(valor)
	else:
		print(f"Valor {valor} não está no vetor.")	
	print("Escolha a remoção do A:")
	escolha = input("Pressione 1 para remover a primeira ocorrencia, outra tecla para todas.")
	if (escolha == '1'): 
		vetA.remove("A")
	else: 
		while "A" in vetA: 
			vetA.remove('A')	
	print("Vetor final: ", vetA)
	
def script03_Remocao_Posicao(vetB):
	vetB_copia = vetB.copy()
	print("Vetor recebido: ", vetB)
	print("Remocao por del")
	posicao_inicial = 1
	posicao_final = 3
	del vetB[posicao_inicial:posicao_final]
	print(f"Vetor com posição [{posicao_inicial}:{posicao_final}] removida: ", vetB)
	print("Remocao por pop: ")
	
def script04(): #Concatenacao
	valores = list(range(1,11))
	anos = list(range(2020,2060,10))
	lista_concatenada = valores+anos
	print(valores)
	valores.extend(anos)
	print(valores)	
	print(lista_concatenada)

def script05(): #Ordenacao
	mercado = ['ouro', "bitcoin", 'titulos' ]
	
	print(mercado)
	mercado.sort()
	print(mercado)	
	moedas = ['ouro', 'bitcoin', 'titulos', 'Dólar', 'Real']
	moedas_original= moedas.copy()
	moedas.sort(key = str.casefold)
	print(moedas)
	
if __name__ == "__main__": 
	#vet = script01_limpo()		
	#script02(vet)
	#script03_Remocao_Posicao(vet)
	#script04()
	script05()




	
	
	
	
	
	
	
	
	

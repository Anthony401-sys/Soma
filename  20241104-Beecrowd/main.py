#coding: utf-8


def Beecrowd2540():
	while True:
		try: 
			n = int(input())
		except EOFError as err:
			break
		aprovacao = (2/3)*n
		votos = map(int, input().split())	
		soma = 0
		for voto in votos: 	
			soma+=voto
		#print(soma)
		if (soma>=aprovacao):
			print("impeachment")
		else:
			print("acusacao arquivada ")	

def Beecrowd1021Prep():
	notas = [100, 50, 20, 10, 5, 2]
	moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
	Valor_Entrada = float(input())
	print(Valor_Entrada)	
	Parte_Inteira_Valor_Entrada = int(Valor_Entrada)
	Parte_Decimal_Valor_Entrada = Valor_Entrada-Parte_Inteira_Valor_Entrada
	print(Parte_Inteira_Valor_Entrada)
	print(Parte_Decimal_Valor_Entrada)	
	print("Problema: A parte decimal fica com residuo de memoria na conversao de base")
	print("2 para base 10")

def Beecrowd1021(): 
	notas = [100, 50, 20, 10, 5, 2]
	moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
	QdeNotas = [0]*len(notas) #Faz vetor com quant de notas
	QdeMoedas = [0]*len(moedas) #Faz vetor com quant de notas
	Valor_Entrada = input().split('.')
	#print(Valor_Entrada)
	ParteInteira = int(Valor_Entrada[0])
	ParteDecimal = int(Valor_Entrada[1])
	#Separaçao das notas
	ValorInt = ParteInteira
	for i in range(len(notas)): 
		while(ValorInt>=notas[i]):
			QdeNotas[i]+=1
			ValorInt-=notas[i]
	print("NOTAS:")
	for i in range(len(notas)):
		strg = "{0:d} nota(s) de R$ {1:.2f}".format(QdeNotas[i],notas[i] )
		print(strg)
	#Separaçao das moedas
	Original_moedas = moedas.copy()#Faco uma copias dos valores originais
	#Passando as moedas para valores inteiros
	for i in range(len(moedas)):
		moedas[i]*=100
		moedas[i]= int(moedas[i])
	#print("Parte Decimal", ParteDecimal)
	#print(moedas)
	ValorInteiro=ParteDecimal+ValorInt*100#Pode ter sobra de 1 real nas notas
	for i in range(len(moedas)):
		while(ValorInteiro>=moedas[i]): #o vetor moedas foi multiplicado por 100
			QdeMoedas[i]+=1
			ValorInteiro-=moedas[i]
	print("MOEDAS:")		 
	for i in range(len(notas)):
		strg = "{0:d} moeda(s) de R$ {1:.2f}".format(QdeMoedas[i],Original_moedas[i])
		print(strg)
		
def Beecrowd1021_SegundaSolucao():
	quantia = float(input()) * 1000
	notas = [100000, 50000, 20000, 10000, 5000, 2000]
	moedas = [1000, 500, 250, 100, 50, 10]
	print("NOTAS:")
	for i in notas:
		print("{0:d} nota(s) de R$ {1:.2f}".format(int((quantia) // i), (i / 1000)))
		quantia %= i
	print("MOEDAS:")
	for j in moedas:
		print("{} moeda(s) de R$ {}".format(int(quantia // j), format(j / 1000, ".2f")))
		quantia %= j
		
	
if __name__=="__main__": 
	#Beecrowd2540()
	#Beecrowd1021Prep()
	Beecrowd1021()
	Beecrowd1021_SegundaSolucao()
























	

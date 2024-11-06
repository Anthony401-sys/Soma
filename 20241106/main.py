#coding: utf-8

def CriaMatriz(NumLinhas, NumColunas): 
	matrizA = [None]*NumLinhas
	for i in range(NumLinhas): 
		matrizA[i] = [None]*NumColunas
	return matrizA

def ImprimirMatriz(M): 
	VerificaMatriz = EhMatriz(M)
	if (VerificaMatriz != False): 
		NumLinhas, NumColunas = VerificaMatriz
	else: 
		print("Nao foi recebida uma matriz em PreencheMatrizPorColunas(M)")
	for i in range(NumLinhas): 
		for j in range(NumColunas): 
			print(M[i][j], end = " ")
		print()	

def EhMatriz(M): 	
	if type(M) == list: 
		nlinhas = len(M)
		if type(M[0]) == list: 
			ncols = len(M[0])
			return nlinhas, ncols
		else: 
			print("Vetor de 1 dimensao")	
			return False
	else: 
		print("Entrada não é vetor")
		return False	


def PreencheMatrizPorColunas(M): 
	VerificaMatriz = EhMatriz(M)
	if (VerificaMatriz != False): 
		NumLinhas, NumColunas = VerificaMatriz
	else: 
		print("Nao foi recebida uma matriz em PreencheMatrizPorColunas(M)")
	print("Passagem por EhMatriz() feita")		
	for i in range(NumLinhas): 
		for j in range(NumColunas): 
			M[i][j]=j*NumLinhas+i+1
	return M		

def PreencheMatrizPorLinhas(M): 
	NumLinhas = len(M)
	NumColunas = len(M[0])
	print("NumLinhas = ", NumLinhas)
	for i in range(NumLinhas): 
		for j in range(NumColunas): 
			M[i][j]=i*NumColunas+j+1
	return M		


def CompreensaoDeMatrizes(NumLinhas,NumColunas): 
	print("Percorrimento por linha")
	A = [[i*NumColunas+j+1 for j in range(NumColunas)] for i in range(NumLinhas)]
	return A
	
		

if __name__ == "__main__": 
	NumLinhas = 4
	NumColunas = 3
	#A=CriaMatriz(NumLinhas,NumColunas)			
	#PreencheMatrizPorLinhas(A)	
	#PreencheMatrizPorColunas(A)
	#A = [[i for i in range(1,9)] for j in range (5)]
	#ImprimirMatriz(A)
	#A = [i for i in range(5)]
	#print(A)	
	A = CompreensaoDeMatrizes(NumLinhas, NumColunas)	
	ImprimirMatriz(A)
	#Compreensao de Matrizes gera uma matriz do zero.
	#Nao precisa receber matriz pronta. 















	

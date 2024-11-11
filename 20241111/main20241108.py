#coding: utf-8
import random as rn

def ConstroiVetor(): 
	print(rn.randint(0,11))
	aleat01 = rn.random()	
	if (aleat01<0.5): 
		print("S")
	else: 
		print("M")	
	for i in range(144): 	
		print("{0:.1f}".format(rn.randint(-4,9)+rn.random()))

def Beecrowd1182_Metodo1(): 
	#Leitura de dados 
	coluna = int(input())	
	operacao = input()
	Ndados = 12 #Valor fixo
	Soma = 0
	#Leitura dos dados em vetor
	for i in range(Ndados**2): 	
		ent = float(input())	
		if i%12==coluna: 			
			Soma+= ent	
	if operacao =='S': 
		strg = "{0:.1f}".format(Soma)
		print(strg)
	else: 
		strg = "{0:.1f}".format(Soma/Ndados)					
		print(strg)

def Beecrowd1182_Metodo2():
	c = int ( input ())
	o = input ()	
	mat = [ None ] * 12 # Cria uma matriz 12 x12
	for i in range (0 , 12):
		mat[i] = [None]*12
	for i in range (0 , 12):
		for j in range (0 , 12):
			mat[i][j] = float(input())
	soma = 0
	for i in range(0,12): 
		soma+=mat[i][c]
		print(mat[i][c])
	print()	
	if o =="S": 
		print ( "%.1f" % soma )
	else: 
		print ( "%.1f" % (soma/12) )		

def Beecrowd1183_Matriz():
	#Criacao da matriz
	DimMat = 12
	Mat = [None]*DimMat
	for i in range(DimMat):
		Mat[i]=[float]*DimMat
	#Leitura de dados: 
	Operacao = input()
	for i in range(DimMat):
		for j in range(DimMat): 
			ent = float(input())			
			Mat[i][j] = ent #Guarda a matriz inteira
	Soma = 0
	Qde = 0
	for i in range(DimMat):
		for j in range(DimMat): 
			if i<j: 
				Soma+=Mat[i][j]
				Qde+=1
	if Operacao =='S': 
		strg = "{0:.1f}".format(Soma)
		print(strg)
	else: 
		strg = "{0:.1f}".format(Soma/Qde)					
		print(strg)

def Beecrowd1183_Matriz():
	#Criacao da matriz
	DimMat = 12
	Mat = [None]*DimMat
	for i in range(DimMat):
		Mat[i]=[float]*DimMat
	#Leitura de dados: 
	Operacao = input()
	for i in range(DimMat):
		for j in range(DimMat): 
			ent = float(input())			
			Mat[i][j] = ent #Guarda a matriz inteira
	Soma = 0
	Qde = 0
	for i in range(DimMat):
		for j in range(DimMat): 
			if i>j: 
				Soma+=Mat[i][j]
				Qde+=1
	if Operacao =='S': 
		strg = "{0:.1f}".format(Soma)
		print(strg)
	else: 
		strg = "{0:.1f}".format(Soma/Qde)					
		print(strg)

def Beecrowd1184_Matriz():
	#Criacao da matriz
	DimMat = 12
	Mat = [None]*DimMat
	for i in range(DimMat):
		Mat[i]=[float]*DimMat
	#Leitura de dados: 
	Operacao = input()
	for i in range(DimMat):
		for j in range(DimMat): 
			ent = float(input())			
			Mat[i][j] = ent #Guarda a matriz inteira
	Soma = 0
	Qde = 0
	for i in range(DimMat):
		for j in range(DimMat): 
			if i>j: 
				Soma+=Mat[i][j]
				Qde+=1
	if Operacao =='S': 
		strg = "{0:.1f}".format(Soma)
		print(strg)
	else: 
		strg = "{0:.1f}".format(Soma/Qde)					
		print(strg)

def Beecrowd1185_Matriz():
	#Criacao da matriz
	DimMat = 12
	Mat = [None]*DimMat
	for i in range(DimMat):
		Mat[i]=[float]*DimMat
	#Leitura de dados: 
	Operacao = input()
	for i in range(DimMat):
		for j in range(DimMat): 
			ent = float(input())			
			Mat[i][j] = ent #Guarda a matriz inteira
	Soma = 0
	Qde = 0
	for i in range(DimMat):
		for j in range(DimMat): 
			if ((i+j)<(DimMat-1)): 
				Soma+=Mat[i][j]
				Qde+=1
	if Operacao =='S': 
		strg = "{0:.1f}".format(Soma)
		print(strg)
	else: 
		strg = "{0:.1f}".format(Soma/Qde)					
		print(strg)

def Beecrowd1186_Matriz():
	#Criacao da matriz
	DimMat = 12
	Mat = [None]*DimMat
	for i in range(DimMat):
		Mat[i]=[float]*DimMat
	#Leitura de dados: 
	Operacao = input()
	for i in range(DimMat):
		for j in range(DimMat): 
			ent = float(input())			
			Mat[i][j] = ent #Guarda a matriz inteira
	Soma = 0
	Qde = 0
	for i in range(DimMat):
		for j in range(DimMat): 
			AbaixoDiagSecundaria = ((i+j)>(DimMat-1))
			AcimaDiagSecundaria = ((i+j)>(DimMat-1))
			if AbaixoDiagSecundaria: 
				Soma+=Mat[i][j]
				Qde+=1
	if Operacao =='S': 
		strg = "{0:.1f}".format(Soma)
		print(strg)
	else: 
		strg = "{0:.1f}".format(Soma/Qde)					
		print(strg)

def Beecrowd1187_Matriz():
	#Criacao da matriz
	DimMat = 12
	Mat = [None]*DimMat
	for i in range(DimMat):
		Mat[i]=[float]*DimMat
	#Leitura de dados: 
	Operacao = input()
	for i in range(DimMat):
		for j in range(DimMat): 
			ent = float(input())			
			Mat[i][j] = ent #Guarda a matriz inteira
	Soma = 0
	Qde = 0
	for i in range(DimMat):
		for j in range(DimMat): 
			if (((i+j)<(DimMat-1))and(i<j)): 
				Soma+=Mat[i][j]
				Qde+=1
	if Operacao =='S': 
		strg = "{0:.1f}".format(Soma)
		print(strg)
	else: 
		strg = "{0:.1f}".format(Soma/Qde)					


def Beecrowd1188_Matriz():
	#Criacao da matriz
	DimMat = 12
	Mat = [None]*DimMat
	for i in range(DimMat):
		Mat[i]=[float]*DimMat
	#Leitura de dados: 
	Operacao = input()
	for i in range(DimMat):
		for j in range(DimMat): 
			ent = float(input())			
			Mat[i][j] = ent #Guarda a matriz inteira
	Soma = 0
	Qde = 0
	for i in range(DimMat):
		for j in range(DimMat): 
			if (((i+j)>(DimMat-1))and(i>j)): 
				Soma+=Mat[i][j]
				Qde+=1
	if Operacao =='S': 
		strg = "{0:.1f}".format(Soma)
		print(strg)
	else: 
		strg = "{0:.1f}".format(Soma/Qde)					
	
def Beecrowd1189_Matriz():
	#Criacao da matriz
	DimMat = 12
	Mat = [None]*DimMat
	for i in range(DimMat):
		Mat[i]=[float]*DimMat
	#Leitura de dados: 
	Operacao = input()
	for i in range(DimMat):
		for j in range(DimMat): 
			ent = float(input())			
			Mat[i][j] = ent #Guarda a matriz inteira
	Soma = 0
	Qde = 0
	for i in range(DimMat):
		for j in range(DimMat): 
			AbaixoDiagSecundaria = ((i+j)>(DimMat-1))
			AcimaDiagSecundaria = ((i+j)<(DimMat-1))
			AbaixoDiagPrincipal = (i>j)
			AcimaDiagPrincipal= (i<j)
			if (AcimaDiagSecundaria and AbaixoDiagPrincipal): 
				Soma+=Mat[i][j]
				Qde+=1
	if Operacao =='S': 
		strg = "{0:.1f}".format(Soma)
		print(strg)
	else: 
		strg = "{0:.1f}".format(Soma/Qde)					
		print(strg)
		
if __name__=="__main__": 
	#ConstroiVetor()
	Beecrowd1182_Metodo1() 		
	#Beecrowd1182_Metodo2() 
	#Beecrowd1183_Matriz()			
	


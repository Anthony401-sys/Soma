#coding: utf-8
import os, shutil

def VerificacaoArquivos(): 
	#Caminho_pasta = os.getcwd()
	#Arquivos_pasta = os.listdir()
	'''
	print(Caminho_pasta)
	print(Arquivos_pasta)
	'''
	#Abertura dos arquivos na pasta Textos: 
	Pasta_atual = os.chdir("Textos")
	#print(os.getcwd())	
	Arquivos_pasta_Textos = os.listdir()
	Arquivos_pasta_Textos.remove('pg67979.txt')
		
	print("Arquivos na pasta Textos: ")
	for i, nome in enumerate(Arquivos_pasta_Textos):
		print(i, nome)	
	'''
	print("Arquivos na pasta Textos so com livros: ")
	for i, nome in enumerate(Arquivos_pasta_Textos):
		print(i, nome)
	'''	
	return 	Arquivos_pasta_Textos
		
def Abertura_arquivos(ListaArquivos):	
	Caminho_Pasta_Atual = os.getcwd()
	Arquivos_pasta_Textos=ListaArquivos
	print("L30", len(Arquivos_pasta_Textos))
	print("Arquivos na pasta Textos: ")
	for i, nome in enumerate(Arquivos_pasta_Textos):
		print(i, nome)
	ReferenciaArquivos = []#Recebe o instanciamento dos arquivos
	for i in range(len(Arquivos_pasta_Textos)): 
		Arquivo = open(Arquivos_pasta_Textos[i], 'r', encoding = "utf-8")
		ReferenciaArquivos.append(Arquivo)
	
	Livro = ReferenciaArquivos[0].readlines()
	print(Livro)
		
		
	
	
		



if __name__=="__main__": 
	ListaArquivos = VerificacaoArquivos()	
	#print(ListaArquivos)
	Abertura_arquivos(ListaArquivos)
	

#coding: utf-8

from ClassePasta import *
from ClasseArquivoPastaSuspensa import *
import time as t

def CriarPasta(QdeArquivos=5): 	
	Pasta1 = Pasta() #Crio a pasta
	Pasta1.CriarPastaVazia()	
	for _ in range(QdeArquivos):		
		Pasta1.Receber_arquivo()
	Pasta1.get_chaves_arquivos_pasta()
	return Pasta1				
		 	
def CriarArquivo(): 
	Arq1 = ArquivoPastaSuspensa("amarelo", "Pesquisa",NumMaxPastas=20)		
	return Arq1

def Mostrar_pastas(Pastas):
	for i, j in enumerate(Pastas):
		print(f'Pasta {i} com conteudo {j.conteudo} ')
		for c, k in j.documento.items():
			print(f'\t chave {c} e valor {k} ')

if __name__ == "__main__": 
	Arquivo1 = CriarPasta()
	Arq_de_Pastas = []
	NumPastasCriadas = 2
	for _ in range(NumPastasCriadas):
		PastaSuspensa = CriarPasta()
		Arquivo1.Pastas.append(PastaSuspensa)
		t.sleep(1.2)
		print('Mudança de pastas')
	Mostrar_pastas(Arq_de_Pastas)
	print()
	Arquivo1.GravarArqEmPastaSuspensa()


	#Arq = CriarArquivo()	

	'''	
	Pasta1 = CriarPasta()
	Pasta2 = CriarPasta()
	Arq.ReceberPasta(Pasta1)
	Arq.ReceberPasta(Pasta2)
	Arq.get_pastas()
	'''
	'''
	#Verificar o erro: 
	
	for i in range(3): 
		PastaSuspensa = CriarPasta()
		Arq.ReceberPasta(PastaSuspensa)
	Arq.get_pastas()		 
	'''
	
	
	'''
	PastasMat = []
	for i in range(3): 
		Pasta = CriarPasta()
		PastasMat.append(Pasta)
	'''
	
	
	'''
	Pasta1 = Pasta() #Crio a pasta
	Pasta1.CriarPastaVazia()
	Pasta1.get_idPasta()
	for _ in range(3): 
		Pasta1.Receber_arquivo()	
	
	Pasta1.get_chaves_arquivos_pasta()	
	Pasta1.Remover_arquivo()
	print("Verificacao de remocao: ")
	Pasta1.get_chaves_arquivos_pasta()		
	'''

		

import time as t
import datetime as dt
class Pasta(object):
    def __init__(self):
        self.id = ''
        self.conteudo = ''
        self.doc = {}
        self.estado = 0
    def CriarPastaVazia(self):
        self.id = input('Identificacao da pasta: ')
        self.conteudo = input("Entre com conteúdo da pasta: ")
        self.estado = 0 #significa que a pasta está vazia.
        self.id = str(int(t.time())) #Dá o momento unix.

    def Receber_arquivo(self):
        nome = input("Entre com o nome do arquivo: ")
        endereco = dt.datetime.now()
        if self.doc.get(nome)==None:        
            self.doc[nome] = endereco
            self.estado = 1 
        else:
            print("Doc contido na pasta. ")   
    def Remover_arquivo(self):
        Arq = input('Entre com a chave do arquivo a remover: ')
        doc_removido = None
        if self.doc.get(Arq)!= None :
            doc_removido = doc.pop(Arq)
        else:
            print(f"Documento {Arq} nao encontrado")
        return doc_removido    
    
    def get_idPasta(self):
        print("id = ", self.id)
        print("conteúdo = ", self.conteudo)

    def get_chavesArquivosNaPasta(self):
        if self.estado == 1:
            print("Relacao dos arquivos na pasta: ", self.id)
            for chave, valor in self.doc.items():
                print('\t', chave)
        else:
            print("Pasta está vazia")

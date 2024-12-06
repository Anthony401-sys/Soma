#import ClassePasta as CP
from ClassePasta import *
    
if __name__ == "__main__":
    Pasta1 = Pasta()
    Pasta1.CriarPastaVazia()
    Pasta1.get_idPasta()
    for _ in range(3):
        Pasta1.Receber_arquivo()

    Pasta1.get_chavesArquivosNaPasta()
    Pasta1.Receber_arquivo()
    print("Verificacao de remocao: ")
    Pasta1.get_chavesArquivosNaPasta()
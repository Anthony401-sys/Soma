def forma_1leitura():
    vet = input().split()#primeira forma de leitura.
    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
        vet[i] = int(vet[i])
   # print(vet)

def forma_2leitura():
    vet = list(map(int, input().split()))#segunda forma de leitura.
    #print(vet)
    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
        #vet[i] = 3*vet[i]
        vet[i]*=3
        print(vet[1], end = ' ')
    #print()

import array as ar #Forma otimizada!
def forma_3leitura_array():
    vet = ar.array('i',map(int, input().split()))
    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
        #vet[i] = 3*vet[i]
        vet[i]*=3
        print(vet[i], end = ' ')
    print()

if __name__ == '__main__':
    #vetor()
    #forma_2leitura()
    forma_3leitura_array()
import array as ar #Forma otimizada!
def forma_3leitura_array():
    vet = ar.array('i', map(int, input().split()))
    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
        #vet[i] = 3*vet[i]
        vet[i]*=3
        print(vet[i], end = ' ')
    print()
if __name__ == '__main__':
    forma_3leitura_array()
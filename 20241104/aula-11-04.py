def beecrowd2540():
    while True: 
        try:
            n = int(input())
        except EOFError as err:
            break
        aprovação = (2/3)*n
        votos = map(int, input().split())
        soma = 0
        for voto in votos:
            soma+=voto 
        print(soma)
        if (aprovação>=soma):
            print('impeachment')
        else:
            print('acusação arquivada')

def beecrowd1021():
    n = input().split('.')
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    Qdenotas = [0]*len(notas) #faz um vetor com quantidade de notas
    Qdemoedas = [0]*len(moedas)
    print(n)
    Parteinteira = int(n[0])
    Partedecimal = int(n[1])

    valorinteiro = Parteinteira
    for i in range(len(notas)):
        while(valorinteiro>=notas[i]):
            Qdenotas[i]+=1
            valorinteiro-=notas[i]
    print('NOTAS:')
    for i in range(len(notas)):
        strg = f'{Qdenotas[i]} de R${notas[i]:.2f}'
        print(strg)
    #separa as moedas
    Original_moedas = moedas.copy() #copia os valores originais.
    #moedas float para inteiros.
    for i in range(len(moedas)):
        moedas[i] = moedas[i]*100 #0.01 * 100 = 1, ou seja, um numero inteiro.
        moedas[i] = int(moedas[i])
    valorinteiro=Partedecimal+valorinteiro*100
    print('MOEDAS:')
    for i in range(len(moedas)):
        while(valorinteiro>= moedas[i]):
            Qdemoedas[i]+=1
            valorinteiro-=moedas[i]
    for i in range(len(notas)):
        strg = f'{Qdemoedas[i]} de R${Original_moedas[i]:.2f}'
        print(strg)
if __name__ =='__main__':
    #beecrowd2540()
    beecrowd1021()
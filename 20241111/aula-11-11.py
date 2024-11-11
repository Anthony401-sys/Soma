def Dic1():
    
    diario_notas = {'Ana Julia': 5, 'Igor': 7}
    notas = diario_notas['Ana Julia']
    print(notas)
    
def Dic3():
    pessoa = dict(nome="Carol", idade = 18, altura = 1.8)
    print('Dicionario de entrada')
    for elemento in pessoa.items():
        #print(elemento)
        print(elemento[0], elemento[1])
    print('Retornando dados em tupla')
    for chave,valor in pessoa.items():
        print('Chave: ', chave, ' Valor: ', valor)

def Dic4():
    Preco = {}
    Preco ['maçã'] = 6
    Preco ['quiabo'] = 4
    Preco ['manga'] = 10
    Preco ['tomate'] = 2
    Preco ['pepino'] = 5
    Preco ['damasco'] = 9
    print(Preco)
    Preco2 = Preco.copy()
    Preco2 ['quiabo'] = 5
    print(Preco2)

def Dic5():
    dic = {2*i:i**2 for i in range(5)}
    print(dic)
    frutas = ['maçã', 'pera', 'manga', 'cereja', 'rucula']
    precos = ['12', '11','10', '4', '7']
    Nfrutas = len(frutas)
    Nprecos = len(precos)
     
if __name__ == '__main__':
    Dic5()
    #Dic4()
    #Dic3()
    #Dic1()
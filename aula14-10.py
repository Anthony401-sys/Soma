def sr0():
    vA = []
    vB = [ None ] * 5
    vC = [ 1 , 3.4, "A", "IFSC" ] #Vetor de tamanho 4 e com tipos diferentes.
    print( vA )
    print( vB )
    print( vC )
    print('Número de vezes que aparece 3.4: ', vC.count(3.4))
    print('Posição de 3.4: ', vC.index(3.4))
#if __name__=='__main__':
   # sr0()
def scr1():
    Lista1 = ['Rampa', 'Descida', 11.34]
    Tupla1 = [1, 3.4, 'A', 'IFSC' ]
    print(Lista1)
    Lista1[1]='Subida'
    print('Lista 1 modificada', end ='')
    print(Lista1)
    print(Tupla1)

def Saida_funcao():
    a = 2.4
    b = 3.5
    return [a,b]

if __name__=='__main__':
   #scr1()
   saida = Saida_funcao()
   print(saida)

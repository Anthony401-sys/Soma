
#vC = [1, 3.4, 'A', ' IFSC ' ]
#for i in vC:
    #print( i )
def CIn():
    vC = [1, 3.4, 'A', ' IFSC ']
    for i in range (0,len(vC)): #Dá o tamanho do vetor.
        print( vC [ i ]) #transcorre a lista(range, e o i define a ordem(1,2,3,4,...))

def MOEDA():
    moedas = ['BRL', 'USD', 'EUR']
    for i, moeda in enumerate(moedas):
        print(i, moeda)
if __name__=='__main__':
    #CIn()
    moedas=MOEDA()
    print(moedas)


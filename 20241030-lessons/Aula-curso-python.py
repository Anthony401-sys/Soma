'''def aprova_pessoa (nome):
    return nome +'Aprovado'
nomes =    ['Larissa', 'Marcos', 'João']'''
#print(nomes)
'''for i in range(len(nome)):
    nomes[i] = aprovar_pessoa(nomes[i])
print(nomes)'''

'''situacao = list(map(aprova_pessoa, nomes))
print(situacao)
print(nomes)'''

'''pinturas = [
['Picasso', 'Les demoiselles', 1907],
['Monet', "Lagoa dos lirios d'água", 1899],
['Renoir',"Duas irmãs", 1881] ,
['Tarcila', 'Abaporu', 1928] ]
def antiguidade(quadro):
    if quadro[2]<1900:
        return True
    else:
        return False
print("Filter")
print(list(filter(antiguidade, pinturas)))
print("Aplicação de Map")
print(list(map(antiguidade, pinturas)))'''

'''numeros = [2,2,3,4,5,6,6,6,6,6,6,7,5,8] #O número 2 aparece duplicado
set_numeros = set(numeros) #Pode alterar a ordenação original.
print(set_numeros)
frutas = {'maca', 'uva', 'banana', 'maca', 'morango'}
print(frutas)'''

#Métodos de sets:
a = {2,2,5,8}
b = {2,2,3,9}
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.union(b))
print(a.intersection(b))
print(set.pop(a))

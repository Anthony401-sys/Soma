profi = ['bombeiro', 'nadador', 'salva-vidas', 'farmaceutico']

try:
    for i in range(4):
        print(profi[i])
except IndexError as erro:
    print("HOUVE UM ERRO DE INDICE")
    print(erro)
else:
    print('programa não passou com erro.')
print('L7')


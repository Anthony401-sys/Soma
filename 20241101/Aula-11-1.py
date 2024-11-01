def prog3():
    print("Digite alguns inteiros, cada um seguido de enter, digite somente enter para sair.")

    soma = 0
    contador = 0
    while True:
        try:
            linha = input("Digite um inteiro.")
            if linha == '':
                break
            else:
                int_number = int(linha)
                soma+=int_number
                contador+=1
        except ValueError as Vr:
            pass
    print('Quantidade de numeros digitados', contador)
    print(f'Soma = {soma} e media = {soma/contador}')

def prog4():
    print("Digite alguns inteiros, cada um seguido de enter, digite somente enter para sair.")

    soma = 0
    contador = 0
    while True:
        try:
            linha = input("Digite um inteiro.")
            if linha == '':
                break
            else:
                int_number = int(linha)
                soma=int_number+soma
                contador+=1
        except ValueError as Vr:
            print('Conversão Impossivel!')
            print('Resposta: ', Vr)
            while True:
                print('É para digitar inteiro')
                print('Tente novamente')
                try:
                    linha2 = input()
                    int_number2 = int(linha2)
                except:
                    pass
                else:
                    int_number = int_number2
                    soma += int_number
                    break

def prog5():
    print("Digite alguns inteiros, cada um seguido de enter, digite somente enter para sair.")

    soma = 0
    contador = 0
    while True:
            try:
                linha = input("Digite um inteiro.")
                if linha == '':
                    break
                else:
                    int_number = int(linha)
                    soma=int_number+soma
                    contador+=1
            except ValueError as Vr:
                print('Conversão Impossivel!')
                print('Resposta: ', Vr)
                while True:
                    print('É para digitar inteiro')
                    print('Tente novamente')
                    try:
                        linha2 = input()
                        int_number2 = int(linha2)
                    except:
                        pass
                    else:
                        int_number = int_number2
                        soma += int_number
                        break

    '''if (contador):
        print('Quantidade de numeros digitados', contador)
        print(f'Soma = {soma} e media = {soma/contador}')

    else:
        print('Não ha dado para calcular')'''
    try:
        print(f'Soma = {soma} e media = {soma/contador}')
    except ZeroDivisionError as Zd:
        print('Não ha dado para calcular.')

if __name__ == '__main__':
    #prog3()
    #prog4()
    prog5()
    pass

2540 beecrowd
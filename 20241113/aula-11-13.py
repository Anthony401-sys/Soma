'''
abertura de arquivo por redirecionamento
Contar palavras 
Guarda em arquivo
'''

def dicionario():
    Dict = {}
    tamanho_min = 4
    caracteresextra = "'"
    caracteresbasicos = '\/():,.;-"!? '
    caracteresremover = caracteresbasicos + caracteresextra
    Nome_proprio = ['harry', 'hagrid', 'hermione', 'valdemort', 'dumbledore', 'snape']
    while True:
        try:
            Linha = input().split()
            if Linha != '':
                for i in range(len(Linha)):
                    # Remover caracteres extras e converter para minúsculas
                    Palavra = Linha[i].strip(caracteresremover).lower()
                    if Palavra not in Nome_proprio:    
                        if (len(Palavra)) >= tamanho_min:
                            if Palavra not in Nome_proprio:    
                                k = Dict.get(Palavra)
                                if k is None:
                                    Dict[Palavra] = 1
                                else:
                                    Dict[Palavra] += 1
        except EOFError as error:
            break
    # Imprimir as palavras e suas contagens
    for chave, valor in Dict.items():
        print(chave, valor)

if __name__ == '__main__':
    dicionario()

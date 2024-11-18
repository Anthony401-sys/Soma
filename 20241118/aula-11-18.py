def Demo_max():
    vet = [-4, 12, 43, 0]
    nome = 'Xenia'
    dic = {'Igor':18, "Xenia": 112, 'Ana Julia':16, "Rafael":21}
    print(f'O maior valor do vetor é: {max(vet)}')
    print(f"A letra mais adiantada do {nome} é: {max(nome)}")
    print(f"Metrica no dicionario: {max(dic)}")

def MediaAluno(p1, p2, p3, p4, Nome = None, Idade = None):
    media = (p1+p2+p3+p4)/4
    if Nome!=None:
        print("A média do aluno", Nome," é ", media)
    if Idade!=None:
        print("A idade do aluno é", Idade)
    return media
media = MediaAluno(2,5,7,8, Nome = "Claudio Peixoto", Idade = 19)

def exibir_preco(nome, preco, custo = 12, valor = 14):
    print(f"{nome} possui o preço {preco}")
    print(f"Faturamento = {valor} e custo = {custo}")

def exibir_preco2(nome, preco,*,custo = {custo}):
    print(f"{nome} possui o preço {preco}")
    print(f"Faturamento = {valor} e custo = {custo}")

def exibir_preco3(*,nome, preco,custo = {custo}):
    print(f"{nome} possui o preço {preco}")
    print(f"Faturamento = {valor} e custo = {custo}")



def Empacotamento():
    lista = [1, 2, 3, 4, 5, 6]
    n1, n2, n3, *n, n5 = lista
    print(n1, n2, n3, n, n5)
if __name__ == '__main__':
    Empacotamento()
    #Demo_max()
    #media
    #exibir_preco(nome, preco, custo = 12, valor = 14):
    #exibir_preco2(nome, preco,*,custo = {custo}):
    #exibir_preco3(*,nome = 'Ana', preco = 12, custo = {custo})

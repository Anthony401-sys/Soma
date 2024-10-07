def ComissãoSalario():
    nome = input('Entre com o nome do vendedor: ')
    Salariofixo = float(input('Informe o salário: '))
    Vendas = float(input('Informe o total de vendas: '))
    Comissão = 0.15*Vendas
    TotalReceber = Salariofixo + Comissão
    return nome, Salariofixo,Comissão, Vendas, TotalReceber

if __name__=='__main__':
    nome, Salariofixo, Comissão, Vendas, TotalReceber = ComissãoSalario()
    strg = '{0} obteve R$ {1:.2f} e vai receber R$ {2:.2f}'.format(nome, Comissão, TotalReceber)
    print(strg)


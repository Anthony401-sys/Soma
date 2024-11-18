#coding: utf-8

def Demo_max(): 
	vet = [-4,12,0,3]
	nome = "xenia"
	dic = {'Igor':18,"Xenia": 13, 'Ana Julia': 16, "Rafael":21}
	print(f"O maior valor do vetor é: {max(vet)}")
	print(f"A letra mais adiantada de {nome} é {max(nome)}")
	print(f"Metrica no dicionario: {max(dic)}")

def MediaAluno(p1, p2, p3, p4, Nome = "Augusto", Idade = None):
	media = (p1+p2+p3+p4)/4
	if Nome!=None:
		print("A média do aluno", Nome," é ", media)
	if Idade!=None:
		print("A idade do aluno é", Idade)
	return media

def exibir_preco(nome, preco, custo = 12, valor = 14):
	print(f"{nome} possui o preço {preco}")
	print(f"Faturamento = {valor} e custo = {custo}")

def exibir_preco2(nome, preco,*, custo, valor): #Operador *
	print(f"{nome} possui o preço {preco}")
	print(f"Faturamento = {valor} e custo = {custo}")

def exibir_preco3(*,nome, preco, custo, valor): #Operador *
	print(f"{nome} possui o preço {preco}")
	print(f"Faturamento = {valor} e custo = {custo}")

	
if __name__=="__main__": 
	exibir_preco3(nome = 'batata', preco = 5.5, valor = 16, custo = 14 )
	#exibir_preco2('batata', 5.5, 16, custo = 14 )
	#exibir_preco('batata', 5.5, valor = 16, custo = 14 )
	#Demo_max()	
	#media = MediaAluno(2,5,7,8, Nome = "Flavia", Idade = 19)
	#print("Media = ", media)

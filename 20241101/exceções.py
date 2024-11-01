#coding: utf-8
def Prog3():
	print("Digite alguns inteiros, cada um seguido de enter, digite somente enter para sair." )

	soma = 0
	contador = 0
	while True: 
		try: 
			linha = input("Digite um inteiro: ")
			if linha == "": #Usuario so digitou enter
				break
			else: #Linha nao vazia
				numero_int = int(linha)
				soma=soma+numero_int
				contador+=1
		except ValueError as VErr:	
			pass		
	print("Quantidade de numeros digitados: ", contador)
	print(f"Soma = {soma} e Media = {soma/contador}")			

def Prog5():
	print("Digite alguns inteiros, cada um seguido de enter, digite somente enter para sair." )

	soma = 0
	contador = 0
	while True: 
		try: 
			linha = input("Digite um inteiro: ")
			if linha == "": #Usuario so digitou enter
				break
			else: #Linha nao vazia
				numero_int = int(linha)
				soma=soma+numero_int
				contador+=1
		except ValueError as VErr:	
			print("Conversao impossivel")
			print("Resposta: ", VErr)
			while True: 
				print("É para digitar inteiro")
				print("Digite novamente")
				try: 
					linha2 = input()
					numero_int2 = int(linha2)
				except: 
					pass
				else:
					numero_int = numero_int2 
					soma=soma+numero_int
					contador+=1					
					break		
	print(f"Soma = {soma} e Media = {soma/contador}")			

def Prog6():
	print("Digite alguns inteiros, cada um seguido de enter, digite somente enter para sair." )
	soma = 0
	contador = 0
	while True: 
		try: 
			linha = input("Digite um inteiro: ")
			if linha == "": #Usuario so digitou enter
				break
			else: #Linha nao vazia
				numero_int = int(linha)
				soma=soma+numero_int
				contador+=1
		except ValueError as VErr:	
			print("Conversao impossivel")
			print("Resposta: ", VErr)
			while True: 
				print("É para digitar inteiro")
				print("Digite novamente")
				try: 
					linha2 = input()
					numero_int2 = int(linha2)
				except: 
					pass
				else:
					numero_int = numero_int2 
					soma=soma+numero_int
					contador+=1						
					break
	'''				
	#Uso de if						
	if (contador): #O contador é diferente de zero
		print(f"Soma = {soma} e Media = {soma/contador}")
	else: 					
		print("Não ha dado para calcular")
	'''
	#uso de try-except
	try: 
		print(f"Soma = {soma} e Media = {soma/contador}")
	except ZeroDivisionError: 
		print("Não ha dado para calcular")		

def Prog7():
	soma = 0
	contador = 0
	while True: 
		try: 
			linha = input()
			if linha == "": #Usuario so digitou enter
				break
			else: #Linha nao vazia
				numero_int = int(linha)
				soma=soma+numero_int
				contador+=1
		except 	EOFError:
			print("Encontrado final do arquivo")
			break	
		except ValueError as VErr:	
			print("Conversao impossivel")
			print("Resposta: ", VErr)
			while True: 
				print("É para digitar inteiro")
				print("Digite novamente")
				try: 
					linha2 = input()
					numero_int2 = int(linha2)
				except: 
					pass
				else:
					numero_int = numero_int2 
					soma=soma+numero_int
					contador+=1						
					break
	'''				
	#Uso de if						
	if (contador): #O contador é diferente de zero
		print(f"Soma = {soma} e Media = {soma/contador}")
	else: 					
		print("Não ha dado para calcular")
	'''
	#uso de try-except
	try: 
		print(f"Soma = {soma} e Media = {soma/contador}")
	except ZeroDivisionError: 
		print("Não ha dado para calcular")		
	

if __name__=="__main__": 
	Prog7()
	#Prog6()
	#Prog5()
	#Prog3()		
	pass

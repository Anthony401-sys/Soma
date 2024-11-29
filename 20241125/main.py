#coding: utf-8

def FatorialRecursivo(n):
	if n==1: #Caso base
		return 1
	else: #Caso recursivo
		temp = n*FatorialRecursivo(n-1)
		#print(temp)
		return temp #Multiplica o número pelo seu antecessor.

def FatorialIterativo(n): 
	NumFatorial = 1
	for i in range(1,n):
		NumFatorial*=(i+1) 
	return NumFatorial	


def FibonacciIterativo(n):
	inicial = 0
	final = 1	
	for i in range(n-1): 
		inicial, final = final, inicial+final
	return final

def FibonacciRecursivo(n): 
	if n<2:
		return n
	return FibonacciRecursivo(n-1)+FibonacciRecursivo(n-2)	

import time as t
if __name__=="__main__": 	
	
	n = 38	
	t1 = t.time()	
	print(f"O termo {n} da sequencia de Fibonacci é {FibonacciIterativo(n)}.")
	t2 = t.time()
	print(f"O termo {n} da sequencia de Fibonacci é {FibonacciRecursivo(n)}.")
	t3 = t.time()
	print("Tempos: ")
	print("Fibo Iterativo: ", t2-t1)
	print("Fibo Recursivo: ", t3-t2)
	
	'''
	n=30
	t1 = t.time()	
	print(f"Fatorial de {n} é {FatorialIterativo(n)}")
	t2 = t.time()	
	print(f"Fatorial de {n} é {FatorialRecursivo(n)}")
	t3 = t.time()	
	print("Tempos: ")
	print("Fat Iterativo: ", t2-t1)
	print("Fat Recursivo: ", t3-t2)
	'''
	
	
	
	

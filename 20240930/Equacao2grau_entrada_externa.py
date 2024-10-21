#coding:utf-8 
import math as m
import random as rd

def Equacao2grau(a,b,c):
	print("Script para resolver equacao 2 grau")
	Coeficiente_a = a
	Coeficiente_b = b
	Coeficiente_c = c
	Delta = abs(m.pow(Coeficiente_b,2)-4*Coeficiente_a*Coeficiente_c)
	x1 = (-Coeficiente_b-m.pow(Delta, 0.5))/(2*Coeficiente_a)
	x2 = (-Coeficiente_b+m.pow(Delta, 0.5))/(2*Coeficiente_a)	
	return x1,x2

for i in range(50):
	print("Equacao ", i+1) 
	a = rd.randint(1,15)
	b = rd.randint(1,15)
	c= rd.randint(1,15)
	Sol1, Sol2 = Equacao2grau(a,b,c)
	print("Primeira solução: ", Sol1, "Segunda solução", Sol2)
	print()

'''
a = int(input("Entre com o coeficiente a da equação: "))
b = int(input("Entre com o coeficiente b da equação: "))
c = int(input("Entre com o coeficiente c da equação: "))

Sol1, Sol2 = Equacao2grau(a,b,c)
print("Primeira solução: ", Sol1)
print("Segunda solução: ", Sol2)
'''


#Equacao2grau()


#coding:utf-8 
import math as m

print("Script para resolver equacao 2 grau")
Coeficiente_a = int(input("Entre com o coeficiente a da equação: "))
Coeficiente_b = int(input("Entre com o coeficiente b da equação: "))
Coeficiente_c = int(input("Entre com o coeficiente c da equação: "))

Delta = m.pow(Coeficiente_b,2)-4*Coeficiente_a*Coeficiente_c

x1 = (-Coeficiente_b-m.pow(Delta, 0.5))/(2*Coeficiente_a)
x2 = (-Coeficiente_b+m.pow(Delta, 0.5))/(2*Coeficiente_a)

print("Primeira solução: ", x1)
print("Segunda solução: ", x2)



#coding:utf-8 
import math as m
#Revisao de entrada e saida de dados. 

a=1
b=4
c=3
'''
Delta = b*b-4*a*c
x1 = (-b-m.sqrt(Delta))/(2*a)
x2 = (-b+m.sqrt(Delta))/(2*a)
'''
'''
Delta = b**2-4*a*c
x1 = (-b-Delta**0.5)/(2*a)
x2 = (-b+Delta**0.5)/(2*a)
'''
Delta = m.pow(b, 2)-4*a*c
x1 = (-b-m.pow(Delta, 0.5))/(2*a)
x2 = (-b+m.pow(Delta, 0.5))/(2*a)

print("Primeira solução: ", x1)
print("Segunda solução: ", x2)



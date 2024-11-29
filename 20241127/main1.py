#coding: utf-8
import os, shutil

print(os.getcwd())
print(os.listdir())
try: 	
	os.mkdir("Teste")
except 	FileExistsError: 
	print("Arquivo ja existia")
	

Caminho1 = os.getcwd()+os.sep+"main1.py" #os.sep é a barra de separacao.
os.chdir("Teste")
Caminho2 = os.getcwd()+"/main1.py"
print("Caminho 1",Caminho1) 
print("Caminho 2",Caminho2) 
shutil.copy(Caminho1, Caminho2)
import time 
print("Dormindo")
time.sleep(6)
print("Acordei")
os.chdir("..")
Caminho3 = os.getcwd()+"/Teste"
shutil.rmtree(Caminho3)


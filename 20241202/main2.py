#-*- coding:utf-8 -*-
from datetime import date
import datetime as dt
import time 


def bissexto(ano): 
	if ( ( ((ano%100)!= 0) and ((ano % 4) == 0) ) or ((ano % 400) == 0)):
		return True
	else: 
		return False 
		
def timeconvert(UnixTimeInicial): 	
	NdiasAnoBissexto = 366
	NdiaAno = 365
	ano = 1970	#Inicio da contagem da hora unix. 
	Dia =UnixTimeInicial-10800	#10800 equivale a zero hora de 01/01/1970 em Brasilia
	
	
	Segundo = Dia%60
	Dia-=Segundo
	Dia/=60				#Resultado em minutos	
	Minuto=Dia%60
	Dia-=Minuto
	Dia/=60				#Resultado em horas. 
	Hora = Dia%24
	Dia-=Hora
	Dia/=24				#Resultado em dias. 
	
	while True:
		if(bissexto(ano)): 
			if(Dia<366):#Está no ano corrente
				break
			else: 
				Dia-=366
				ano+=1
		else: 
			if(Dia<365):#Está no ano corrente
				break
			else: 
				Dia-=365
				ano+=1
		
	if(bissexto(ano)): #Verifica se o ano encontrado é bissexto. 
		fev = 29
	else: 
		fev = 28		
			
	Meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
		"Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	DiasMes = [31,fev, 31,30,31,30,31,31,30,31,30,31]
	Mes = 0
	for i in range(12):
		if(DiasMes[i]<Dia): 
			Dia-=DiasMes[i]			
		else: 
			Mes = i
			break
	Dia+=1	#Contagem dos dias inicia em 1 e não em zero. 
	Dia = int(Dia)
	Hora = int(Hora)
	Minuto = int(Minuto)
	Segundo = int(Segundo)
	return [Dia,Meses[Mes], ano, Hora, Minuto, Segundo]
	
def UnixTimeConverter(Momento):	
	if len(Momento)<3:
		print("São necessárias pelo menos 3 entradas: Ano, mes, dia.")
		exit(1)
	if len(Momento)==3:	
		DataHoraPython = dt.datetime(Momento[0], Momento[1], Momento[2])#Ano mes dia 
	elif len(Momento)==4:	
		DataHoraPython = dt.datetime(Momento[0], Momento[1], Momento[2], Momento[3])#Ano mes dia hora
	elif len(Momento)==5:	
		DataHoraPython = dt.datetime(Momento[0], Momento[1], Momento[2], Momento[3], Momento[4])#Ano mes dia hora min
	else:
		DataHoraPython = dt.datetime(Momento[0], Momento[1], Momento[2], Momento[3], Momento[4], Momento[5]) 
		 	 
	#Impressao da data/hora do python
	print("Data-hora python",DataHoraPython)
	#print(type(DataHoraPython))
	#print(DataHoraPython.day,DataHoraPython.minute )
	MomentoUnix = int(time.mktime(DataHoraPython.timetuple()))
	return MomentoUnix




if __name__=="__main__":
	print("Digite ano, mes, dia, hora, min, seg:")#Hora, min e seg sao facultativos.
	Momento = list(map(int, input().split()))
	MomentoUnix = UnixTimeConverter(Momento)#Retorna data no formato timestamp
	print(MomentoUnix)
	Data_Hora = timeconvert(MomentoUnix) #Retorna lista com data hora. 
	print(Data_Hora)
	
	
	
	


#coding: utf-8
import CaixaAcoplada as CA
1
if __name__=="__main__":
	Vaso = CA.CaixaAcoplada()
	Vaso.IniciarUtilizacao()
	print("Nivel atual de água: ",Vaso.get_nivel_agua())
	Vaso.EncherCaixaAcoplada()
	print("Nivel atual de água: ",Vaso.get_nivel_agua())	
	while True:
		Vaso.AcionarDescarga()
		print("Nivel atual de água: ",Vaso.get_nivel_agua())
		print("Deseja enviar para a manutenção?")
		print("Digite 1 para sim, outra tecla para não")
		Resposta = input()
		if Resposta == '1':
			Vaso.EnviarCaixaManutencao()
			break
		Vaso.AcionarDescarga()

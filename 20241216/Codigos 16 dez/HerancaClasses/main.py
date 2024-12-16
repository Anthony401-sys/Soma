#coding: utf-8
import classes as c

if __name__=="__main__": 
	A = c.Camera("Sony", "24s")
	A.tirar_foto() 
	B = c.CameraCelular('Canon', '64mp', 4)
	B.Aplicar_filtro("Azul")
	B.tirar_foto() 


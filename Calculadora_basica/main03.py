import tkinter as tk
import Temas as Ta

janela = tk.Tk()
janela.title("Calc Base")
janela.geometry("240x320")
frame_visor = tk.Frame(janela, width = 240, height= 50, bg = Ta.Cor_visor)
frame_visor.grid(row = 0, column = 0) #Insere o frame usando o grid.
valor_visor = tk.StringVar()
valor_visor.set("Calculador ligou!")
visor_label = tk.Label(frame_visor, textvariable = valor_visor, width = 16, height = 2, padx = 7)
visor_label.place(x=5, y=3)

frame_botoes = tk.Frame(janela, width = 240, height = 270, bg = Ta.Cor_visor)
frame_botoes.grid(row = 1, column = 0)
botao1 = tk.Button(frame_botoes, text = "AC", width = 10, height = 2, bg = Ta.Cor_cinzaclaro)
botao1.place(x=0, y=0)
botao2 = tk.Button(frame_botoes, text = "mod", width = 5, height = 2, bg = Ta.Cor_cinzaclaro)
botao2.place(x=106, y=0)
botao3 = tk.Button(frame_botoes, text = "", width = 5, height = 2, bg = Ta.Cor_laranja)
botao3.place(x=171, y=0)

botaon1 = tk.Button(frame_botoes, text = "7", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaon1.place(x=0, y=52)
botaon1 = tk.Button(frame_botoes, text = "8", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaon1.place(x=60, y=52)
botaon2 = tk.Button(frame_botoes, text = "9", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaon2.place(x=120, y=52)
botaon3 = tk.Button(frame_botoes, text = "x", width = 4, height = 2, bg = Ta.Cor_laranja)
botaon3.place(x=180, y=52)

botaol1 = tk.Button(frame_botoes, text = "4", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaol1.place(x=0, y=52*2)
botaol1 = tk.Button(frame_botoes, text = "5", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaol1.place(x=60, y=52*2)
botaol2 = tk.Button(frame_botoes, text = "6", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaol2.place(x=120, y=52*2)
botaol3 = tk.Button(frame_botoes, text = "-", width = 4, height = 2, bg = Ta.Cor_laranja)
botaol3.place(x=180, y=52*2)

botaom1 = tk.Button(frame_botoes, text = "1", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaom1.place(x=0, y=52*3)
botaom2 = tk.Button(frame_botoes, text = "2", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaom2.place(x=60, y=52*3)
botaom3 = tk.Button(frame_botoes, text = "3", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaom3.place(x=120, y=52*3)
botaom3 = tk.Button(frame_botoes, text = "+", width = 4, height = 2, bg = Ta.Cor_laranja)
botaom3.place(x=180, y=52*3)

botaok1 = tk.Button(frame_botoes, text = "0", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaok1.place(x=0, y=52*4)
botaok2 = tk.Button(frame_botoes, text = "00", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaok2.place(x=60, y=52*4)
botaok3 = tk.Button(frame_botoes, text = ".", width = 4, height = 2, bg = Ta.Cor_cinzaescuro)
botaok3.place(x=120, y=52*4)
botaok3 = tk.Button(frame_botoes, text = "^", width = 4, height = 2, bg = Ta.Cor_laranja)
botaok3.place(x=180, y=52*4)

botao_espaço = tk.Button(frame_botoes, text = "=", width = 30, height = 2, bg = Ta.Cor_cinzaclaro)
botao_espaço.place(x=0, y=52*5)


janela.mainloop()
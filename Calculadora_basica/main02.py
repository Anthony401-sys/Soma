import tkinter as tk
import Temas as Ta

janela = tk.Tk()
janela.title("Calc Base")
janela.geometry("240x320")
frame_visor = tk.Frame(janela, width = 240, height= 50, bg = Ta.Cor_visor)
frame_visor.grid(row = 0, column = 0) #Insere o frame usando o grid.

janela.mainloop()
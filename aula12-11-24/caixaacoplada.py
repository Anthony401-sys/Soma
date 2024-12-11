import time as t
class Caixa_acoplada(object):
    def __init__ (self):
        self.NivelAgua = 0
        self.NivelMax = 5
        self.NivelMin = 0.5
        self.Estado = 0
        self.Vazao = 0.5 #Vazao = 0.5 litros p.segundo.
        self.Vazao_Saida = 0.9 
    def Encher_Caixa(self):
        print("Caixa enchendo, volume inicial = ", self.NivelAgua)
        while(self.NivelAgua<=self.NivelMax):
            self.NivelAgua += self.Vazao
            t.sleep(0.5)
            print("Nivel de agua = ", self.NivelAgua)
        self.Estado = 1
    def Esvaziar_Caixa(self):
        print("Caixa esvaziando, volume inicial = ", self.NivelAgua)
        while(self.NivelAgua>=self.NivelMin):
            self.NivelAgua-=self.Vazao_Saida
            t.sleep(0.5)
            print("Nivel de agua = ", self.NivelAgua)
        self.Estado = 0

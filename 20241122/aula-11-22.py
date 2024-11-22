def explo_funcao(*args, **kwargs):
    print(args)
    print("Número de argumentos nomeados:", len(kwargs))
    print("Chaves encontradas:", end = '')
    for chave in kwargs.keys():
        print(chave, end = ' ')
        print()
    sbr = kwargs.get('sobrenome')
    if sbr !=None:
        print("Sobrenome do usuário: ",sbr)
    try:
        peso=kwargs['peso']
    except KeyError:
        pass
    
def antes():
    print("Antes da função")
def depois():
    print("Depois da função")
def parabenizar():
    print("Parabens")

def meu_decorator(funcao): #Envia a referencia da função
    def envelope():
        antes()
        funcao() #Agora não é referencia, executa a função
        depois()    
    return envelope #Retorna somente a referencia da função.
                    #A função meu_decorator recebe e devolve uma referência a função
import time

def MedeTempo():
    def envelope(*args):
        tempoinicial = time.perf_counter()
        resultado = func(*args)
        tempofinal = time.perf_counter()
        Delta_tempo = tempofinal - tempoinicial
        strg = "Tempo gasto por {0}: {1:.5f}".format(func.__name__, Delta_tempo)
        print(strg)
        return resultado
    return envelope
def tempo_laco():
    for _ in range(int(1e06)):
        pass

if __name__ == '__main__':
    tempo_laco()
    resultado = MedeTempo(tempo_laco)
    resultado()
    #resultado=meu_decorator(parabenizar)
    #resultado()

    '''lista = [1,2,3] #lista
    lista2 = (10,20,30) #tupla
    num = 78
    explo_funcao(lista,lista2,num,nome="Caio",sobrenome="Martins",idade=19)'''
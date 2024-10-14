def C_in():
    frutas = ['maçã', 'manga', 'seringuela', 'azeitona']
    print('maçã' in frutas)
    print('tomate' not in frutas)
    Fruta = 'laranja'
    if Fruta:
        frutas.append(Fruta)
        print(f'{Fruta} adicionado ao vetor')
    else:
        print(f'{Fruta} já está no vetor')    
    print(Fruta)
if __name__=='__main__':
    C_in()
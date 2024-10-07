
def Eq2(a,b,c):
    Delta = (b**2-4*a*c)
    if Delta>0:
        # há duas raízes reais distintas.
        x1 = (-b-pow(Delta, 0.5))/(2*a)
        x2 = (-b+pow(Delta,0.5))/(2*a)
        return x1, x2
    elif (Delta ==0):
        print('Há raiz única, Delta = ', Delta)
        return None
    
    if __name__=='__main__':
        x1, x2 = Eq2(1,4,3)
        print('')
    
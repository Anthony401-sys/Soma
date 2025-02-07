#coding: utf-8
a = 5 
b = 95 

div = str(a/b).split('.')
ParteInteira = div[0]
ParteFrac = div[1] 
FlagInt = False
if ParteFrac=='0': 
	FlagInt = True
print(FlagInt)
strg = ''
if FlagInt:
	strg = ParteInteira
else: 
	strg = ParteInteira+"."+ParteFrac[0:3]	
print(strg)	 
	
'''
print(div)
divInt = a//b
print(divInt)
strg1 = int(str(div-divInt).split('.')[1])
print("L10", strg1)
strg1 = f"{divInt}"+'.'#+f"{strg1:.3f}"
print("DivInt: ", strg1)
'''
#parteDec = 89/9-89//9
#strg = str(strg1)+str(parteDec)
'''
sol = eval(strg)
print(sol)
print(type(sol))
resp = ''
print(isinstance(sol, float))
if isinstance(sol, float): 
	resp = f"{sol:.3f}"
print(resp)	
'''

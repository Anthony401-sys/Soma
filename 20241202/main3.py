#-*- coding:utf-8 -*-
import json
#Dicionario nativo de python, ou outra estrutura
comp1 = {"marca":"Dell",
"preço":7000
}
comp2 = {"marca":"Pichau",
"preço":8000
}
VetComp = [comp1,comp2]

nome_arquivo = "Comp.json"
Arq1 = open(nome_arquivo, "w", encoding = "utf-8")
#Gravacao dos dados
json.dump(VetComp, Arq1)
Arq1.close()
print(VetComp)

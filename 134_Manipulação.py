#MANIPULAÇÃO BÁSICA DE DICIONÁRIOS
dic = {"nome": "Matheus", "idade": 30}

dic ["profissão"] = "Programador"
print(dic)

dic["nome"]="Matheus Battisti"
print(dic)

valor_excluido = dic.pop("idade")
print(valor_excluido)
print(dic)

del dic["nome"]
print(dic)

dic.clear()
print(dic)


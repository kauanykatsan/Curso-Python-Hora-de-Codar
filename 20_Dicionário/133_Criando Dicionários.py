#DIcionarios em Python são estruturas de dados que armazenam pares chave-valor
#devem ser unicas e de tipo imutavel

dic = {"nome": "Matheus", "idade": 30}

dic2 = dict(cidade = "São Paulo", estado = "SP", populacao = 472817)

print(dic)

print(dic2)

dic_vazia = {}
print(dic_vazia)

pares = [("a", 1), ("b", 2), ("c", 3)]

dic_tuplas = dict(pares)

print(dic_tuplas)

#OPERAÇÕES BÁSICAS EM TUPLAS

#incluem indexação, fatiamento, concetenação e repetição, semelhantes ás listas

tupla =(1, 2, 3, 4)


#Erro
#tupla[0] = 10


print(tupla[0])
tupla_nova = tupla + (5,6,7)   #Adicionais mais elementos 
print(tupla_nova)


ocorrencias=tupla.count(3)
print(ocorrencias)

print(tupla_nova.index(7))


#------------------------------------------------

print(tupla_nova[3])
subtupla = tupla_nova[2:5]
print(subtupla)

tupla= (10,20)


#CONCATENAÇÃO -UNIÃO/JUNÇÃO
tupla_maior = tupla_nova + tupla
print(tupla_maior)


#REPETE TODOS OS NUMEROS 3X
tupla_repetida = tupla_nova * 3
print(tupla_repetida)

tupla = [1,2,3]
repetir_tupla = tupla * 4
aumentar_tupla= repetir_tupla + [4,5]
print(aumentar_tupla)


#DESEMPACOTAMENTO DE TUPLAS
#O desempacotamento permite etribuir os valores de uma tupla diretamente a variaveis individuais

tupla_teste=("a", "b", "c")
um, dois, tres = tupla_teste
print(um, dois, tres)

#erro = ha mais valores na tupla
# teste, testando = tupla_teste

a, *extras = tupla_repetida
print(a)
print(extras)

tuplas = [(1, 14), (22, 12), (44, 45)]
for x, y in tuplas:
    print("Coordenadas x e y : ", x,y)

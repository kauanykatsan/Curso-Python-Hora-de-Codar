#A imutabildade das tuplas significa que seus elementos não podem ser alterados após a criação

tupla = (1, 2, 3, 4)


#Erro
#tupla[0] = 10


print(tupla[0])
tupla_nova = tupla + (5,6,7)   #Adicionais mais elementos 
print(tupla_nova)


ocorrencias=tupla.count(3)
print(ocorrencias)

print(tupla_nova.index(7))

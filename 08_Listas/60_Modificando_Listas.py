#Continuando Lstas Alinhadas
matriz = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]

print(matriz)
print(matriz[0])

#Primeiro index = lista
#Segundo index = elemento
print(matriz[1][2])

nova_linha = [10,11,12]
matriz.append(nova_linha) #append adiciona um elemtno no final da lista
print(matriz)


#Aula 60
print(matriz[2][0])
matriz[0][1] = 99

print(matriz)
matriz.pop(1)#remover um item da lista
print(matriz)


matriz[0].append(123)
print(matriz)


#Acessando sublinhas, podemos usar os metodos de listas normais 

matriz.append([4,4,4])
print(matriz)

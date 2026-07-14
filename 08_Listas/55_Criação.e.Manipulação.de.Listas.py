#Listas podem ser criadas com elementos iniciasi ou vazias, prontas para receber valores porteriormente
#A função len() retorna o número total de elementos de uma lista, sendo útil para verificar o tamanho dinamicamente
#Operadores como in e not in verificam se um valor especifico está presente na lista 

lista_vazia = []  
print(lista_vazia)
print(len(lista_vazia)) #conta quantos elementos existem 

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1)

print(len(lista1))

lista_concatenada = lista1 + lista2
print(lista_concatenada)

lista_repetida = lista1 *3
print(lista_repetida)


#Verficar se um elemento esta ou não na lista (in not in)
print( 2 in lista1)
print( 5 in lista2)
print(7 not in lista1)
print(10 in lista2)

#Modificar valores da lista 
lista1[0] = 10
print(lista1)

#indice na lista começa de 0 a 9 (lo el)
print(lista1[2])

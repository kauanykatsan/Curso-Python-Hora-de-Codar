#COMPARAÇÃO ENTRE CONJUNTOS E OUTRAS ESTRUTURAS
#conjuntos (set) são mais rápidos para operações de busca de comparação, mas não mantem a ordem dos elementos 


lista = [1,2,3,4,4]

conj1=set(lista)

print(conj1)

#INTERSECCAO DE 2 LISTAS
lista2 = [4,5,6,7,8,9]
print(list(set(lista) & set(lista2)))

tupla = (1,2,3)

conj2 = set(tupla)

print(conj2)

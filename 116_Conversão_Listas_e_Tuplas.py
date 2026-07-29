#CONVERSAO ENTRE LISTAS E TUPLAS

#A função tuple() converte listas ou outro iteráveis em tuplas, preservando a ordem dos elementos
#A função list() converte tuplas em listas, permitindo modificaçõesnos elementos posteriormente


lista = [1 ,5, 6, 7]
tupla = tuple(lista)

print(tupla)

lista_da_tupla = list(tupla)
print(lista_da_tupla)


#STRING PARA LISTAS OU TUPLAS

texto = "Python"
tupla_texto=tuple(texto)
lista_texto = list(texto)

#STRINGS -> vão ser divididas pelas letras
print(tupla_texto)
print(lista_texto)

#Tuple e list não modificam o dado original


##DIFERENÇAS PRÁTICAS ENTRE LISTAS E TUPLAS
#imutabilidade: Tuplas são imutáveis, enquanto listas podem ser modificadas  após a criação
#Desempenho: Tupls geralmente tem melhor desempenpenho, senod mais rápidas para criação e iteraçõa
#Uso ideal:Listas são melhores para coleções dinâmicaa e manipulação, como append e remove, que não estão disponíveis em tuplas

l = [1, 2, 3]
t = (1, 2, 3)

#t[0] = 1

l[0] = 2

import timeit

tempo_lista = timeit.timeit("[1, 2, 3, 4, 5]", number=100000)
tempo_tupla = timeit.timeit("(1, 2, 3, 4, 5)", number=100000)

print(f"Tempo lista: {tempo_lista} e Tempo tupla: {tempo_tupla}")
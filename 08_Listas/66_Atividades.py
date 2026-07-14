# Exercício 1:
# Enunciado: Crie uma lista com os números de 1 a 10. Use append() para adicionar o número 11
# e insert() para adicionar o número 0 no início da lista. Exiba a lista resultante.
# Descrição: O programa deve criar uma lista inicial, usar métodos para adicionar elementos no
# início e no final, e exibir a lista modificada.

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.append(11)
numeros.insert(0, 0)  #primeiro 0 = posição  segundo 0 =valor que será inserido 

print(numeros)

# Exercício 2:
# Enunciado: Escreva um programa que receba uma lista de nomes e conte quantas vezes um nome
# específico aparece na lista usando count().
# Descrição: O programa deve receber uma lista de nomes e um nome de busca, calcular quantas
# vezes o nome aparece na lista usando count() e exibir o resultado.

nomes = ["Kauany" , "Julye", "Sarah", "Thais", "Kauany", "Kauany"]
buscar_nome = "Kauany"
contagem = nomes.count(buscar_nome)

print(f"O nome {buscar_nome} foi encontrado {contagem} vezes")

# Exercício 3:
# Enunciado: Desenvolva um programa que organize uma lista de números em ordem crescente e
# depois inverta essa lista. Exiba os resultados em ambas as etapas.
# Descrição: O programa deve usar sort() para ordenar a lista e reverse() para inverter a
# ordem, exibindo os resultados após cada operação.
numeros = [ 5, 8, 9, 6, 4, 16, 20]
numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

# Exercício 4:
# Enunciado: Crie uma lista aninhada que representa uma matriz 3x3. Acesse e modifique o valor
# do elemento da segunda linha, terceira coluna. Exiba a matriz antes e depois da modificação.
# Descrição: O programa deve criar uma lista aninhada para representar a matriz, modificar
# um valor específico usando índices e exibir as duas versões da matriz.
matriz= [ 
    [1,2,3],
    [4,5,6],
    [8,5,4]
]
print(matriz)
matriz[1][2]=50
print(matriz)

# Exercício 5:
# Enunciado: Escreva um programa que receba uma lista de números e exiba o menor valor, o
# maior valor, o número total de elementos e a soma de todos os valores.
# Descrição: O programa deve usar as funções len(), min(), max() e sum() para calcular os
# resultados e exibi-los de forma organizada.

numeros_5 = [2, 5, 8, 7, 9, 50, 17, 5]

print("Menor valor:", min(numeros_5))
print("Maior valor:", max(numeros_5))
print("Quantidade:", len(numeros_5))
print("Soma:", sum(numeros_5))


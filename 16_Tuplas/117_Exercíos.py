# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Crie uma tupla que armazene os nomes de 5 cidades. Imprima cada nome individualmente
# utilizando um loop.
# Descrição: O programa deve criar uma tupla com 5 nomes de cidades e usar um loop `for` para exibir
# cada cidade.

cidades = ["Chapecó", "Florianópolis", "Xanxere", "Xaxim", "Blumenau"]
for cidade in cidades:
    print("Cidades: {cidade}")

# Exercício 2:
# Enunciado: Defina uma função que receba dois números como parâmetros e retorne uma tupla contendo
# a soma, a diferença e o produto dos números. Mostre como acessar cada valor retornado separadamente.
# Descrição: A função deve calcular e retornar os valores como uma tupla. O programa deve usar
# desempacotamento para acessar os valores.

def operacoes(n1,n2):
    return n1+n2, n1-n2, n1 *n2
resultado = operacoes(10, 7)
print(f"Soma: {resultado[0]}, Subtração: {resultado[1]}, Multiplição: {resultado[2]}")


# Exercício 3:
# Enunciado: Converta a lista `[10, 20, 30, 40, 50]` em uma tupla. Em seguida, exiba o maior e o
# menor valor da tupla.
# Descrição: O programa deve usar a função `tuple()` para a conversão e as funções `max()` e `min()`
# para encontrar os valores máximo e mínimo.

lista = [10, 20, 30, 40, 50]
tupla = tuple(lista)

print(f"O maior valor é: {max(tupla)} e menor: {min(tupla)}")

# Exercício 4:
# Enunciado: Crie um programa que itere sobre uma tupla de números e calcule a soma apenas dos
# números pares presentes nela.
# Descrição: O programa deve iterar sobre a tupla, verificar se cada número é par e somar os pares.

numeros = [1,2,3,4,5,6,7,8,9,10,11,12]

soma_pares =0
for numero in numeros:
    if numero % 2 ==0:
        soma_pares += numero

print(f"A soma é: {soma_pares}")


# Exercício 5:
# Enunciado: Escreva um programa que compare o desempenho de listas e tuplas na iteração de
# 1 milhão de elementos, exibindo o tempo de execução de cada uma.
# Descrição: O programa deve usar a biblioteca `timeit` para medir o tempo de execução de um loop
# iterando sobre uma lista e uma tupla.

lista = list(range(1_000_000))
tupla = tuple(range(1_000_000))


import timeit  #USADO PARA MEDIR TEMPO 
tempo_lista = timeit.timeit(stmt="for x in lista: pass", setup="lista = list(range(1000))", number= 1)
tempo_tupla = timeit.timeit(stmt="for x in tupla: pass", setup="tupla = tuple(range(1000))", number= 1)
          
# timeit.timeit usada para medir o tempo de execução de pequenos trechos de código


print(f"Tempo de execução lista {tempo_lista: .5f} segundo")
print(f"Tempo de execução tupla {tempo_tupla: .5f} segundo")

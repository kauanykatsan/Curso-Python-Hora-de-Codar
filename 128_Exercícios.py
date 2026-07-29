# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Crie um conjunto que armazene os números de 1 a 5. Em seguida, verifique se o número 3 
# está presente no conjunto e imprima o resultado.
# Descrição: O programa deve criar um conjunto com os números de 1 a 5, verificar a presença do número 
# 3 usando o operador `in` e exibir o resultado.

numeros = {1,2,3,4,5}
print(f"O número 3 esta no conjunto? {"Sim" if 3 in numeros else "Não"}")

# Exercício 2:
# Enunciado: Defina dois conjuntos de palavras representando conjuntos de interesses diferentes. 
# Realize operações de união, interseção e diferença entre eles, exibindo os resultados.
# Descrição: O programa deve criar dois conjuntos de palavras e usar operações matemáticas para 
# calcular união, interseção e diferença.

conj1 =  {"Pyton", "Java", "C+"}
conj2 = {"Engenharia da Computaçõa", "Sistemas de informações", "Ciencias da Caomputação"}

print(f"Uniao {conj1 | conj2}")
print(f"Interseção {conj1 & conj2}")
print(f"Diferença { conj1 - conj2}")

# Exercício 3:
# Enunciado: Utilize `frozenset` para criar um conjunto imutável com os números de 1 a 5. 
# Tente adicionar um elemento ao conjunto e exiba a mensagem de erro gerada.
# Descrição: O programa deve criar um `frozenset`, tentar adicionar um elemento e capturar 
# o erro gerado.

imutavel = [1,2,3,4,5]
try:
    imutavel.add(6)
except AttributeError:
    print("Ocorreu um erro no programa")

# Exercício 4:
# Enunciado: Crie um programa que itere sobre dois conjuntos e encontre a diferença simétrica 
# entre eles. Imprima os elementos exclusivos de cada conjunto.
# Descrição: O programa deve calcular a diferença simétrica entre dois conjuntos usando o operador 
# `^` e exibir os resultados.

conj_a = {1, 2, 3, 4}
conj_b = {4, 5, 6, 7}

diferenca = conj_a ^ conj_b

print(diferenca)

# Exercício 5:
# Enunciado: Converta uma lista de nomes com duplicatas em um conjunto para remover os duplicados. 
# Em seguida, adicione um novo nome ao conjunto e imprima o resultado.
# Descrição: O programa deve converter uma lista em um conjunto, remover duplicatas automaticamente, 
# adicionar um novo nome e exibir o resultado.

nomes= ["Ana", "Joana", "Mariana", "Ana"]

c_nomes = set(nomes)

c_nomes.add("Andreia")

print(c_nomes)
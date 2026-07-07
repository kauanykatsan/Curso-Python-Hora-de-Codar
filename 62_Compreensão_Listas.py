#Criação de listas de forma compacta
#lista com quadrados de numeros
'''
quadrados = [x**2 for x in range (1, 11)]

print(quadrados)

#Combinar listas
nomes = ["Alice", "Julia", "Wesley"]
idades = [18, 25, 17]

combinacao = [f"{nome} tem {idade} anos" for nome, idade in zip (nomes, idades)]
print(combinacao)


#Lista de caracteres de uma string
letras = [letra for letra in "Python"]
print(letras)

#Strings e listas = acesso por indice, metodo len, percorrer com for
'''




alunos = ["Kauany", "Thais", "Sarah"]
faculdade = ["Ciências da Computação", "Sistemas de informações", "Engenharia da Computação"]

combinar = [f"A aluna {alunos} está matriculada no curso de {faculdade}!" for alunos, faculdade in zip (alunos, faculdade)]
print(combinar)

#Aula 43
#O metodo Join() concatena uma sequencia de strings, colocando um delmitador especifico entre cada elemento
#A sequencia pode ser uma lista, tupla ou qualquer iterável contendo strings, e os elementos são unidos em uma punica string
#É util para reverter processos de split() ou construir uma string formatadas a partir de coleções de dados
# uma string é uma sequência de caracteres (letras, números e símbolos) usada para armazenar e manipular textos


palavras = ["Python", "é", "incrivel"]
print(" ".join(palavras))

print(",".join(palavras))

numeros = [1, 2, 3]


#Map -> vai percorrer uma lista e modificr eles
print(" ".join(map(str,numeros)))


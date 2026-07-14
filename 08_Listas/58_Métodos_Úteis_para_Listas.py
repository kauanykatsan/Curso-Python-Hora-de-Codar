#O método conut(valor) retorna o número de ocorrências de um valor na lista, útil para analisar dados repetidos
#O método Index(valor) retona o indice da primeira ocorrência de um valor específico; se o valor não existir, ocorre um erro
#Clear() remove todos os elementos da lista, útil para reiniciar dados sem criar uma nova lista

frutas = ["maça", "banana", "laranja", "morango", "banana"]

print(frutas.count("banana"))  #Count conta 
print(frutas.count("maça"))
print(frutas.count("kiwi"))


print(frutas.index("banana"))


frutas.clear()

print(frutas)

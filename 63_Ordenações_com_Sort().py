#Ordenação de ista

numeros = [1, 10 ,5 ,6, 8, 2]

numeros.sort()
print(numeros)


numeros.sort(reverse=True)
print(numeros)


#Utilizando key 
palavras = ["teste", "testando","mais um teste"]
palavras.sort(key=len)
print(palavras)

palavras.sort(key=len, reverse = True)
print(palavras)


#Sorted -> não muda o dado original
numeros_2 = sorted(numeros)
print(numeros)
print(numeros_2)

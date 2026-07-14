#In verifica se um valor está resente em uma sequência, como listas, strings ou tuplas
#NOT IN verifica se um vlor não está presente na sequência, retornando o inverso de im 

frutas = ["maça", "banana", "laranja"]

print("maça" in frutas) # se tem
print("abacate" not in frutas)  #se não tem


frase = "Pythone é muito legal"
print("Python" in frase)
print("Java" in frase)

#Dicionarios = lista de chave e valor
pessoa = {"nome": "Matheus", "idade":33}

#Chave
print("nome" in pessoa)
#Valor
print("Matheus" in pessoa.values())

#Tupla = Lista imutavel
numeros =(1,2,3,4,5)
print(1 in numeros)
print(10 in numeros)

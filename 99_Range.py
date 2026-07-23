#Gera uma sequencia de numero, facilitando iteracoes controladas em loops for 

#RANGE
for i in range(5):
    print(f"i = a {i}")
for i in range(3, 16, 3):
    print(f"i = {i}")
for i in range(10, 0, -1):
    print(f"i = {i}")


numeros = [10,20,30,40]

for i in range (len(numeros)):
    print(f"i = {i}, acessando array {numeros[i]}")
#O loop for é usado para iterar sobre sequencias como listas, strings, tuplas, dicionarios e conjuntos de forma eficiente
#Amplamente utilizado em manipulacao de colecoes e processamentos de dados 

#FOR
frutas = ["maça","banana","limão"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

    #i => frutas[i]

for i, fruta in enumerate(frutas):
    print(f"Fruta: {fruta} referente ao indice {i}")


for numero in range (1, 6):
    print(numero)

for fruta in frutas:
    if "a" in fruta:
        print(f"Fruta {fruta} tem a letra 'a'")

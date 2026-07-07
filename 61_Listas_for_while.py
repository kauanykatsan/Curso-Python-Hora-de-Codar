matriz = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
print(matriz)


lista_nova=[1,2,3,4,5]
#for in
for numero in lista_nova:
    print("O número da vez é", numero)

#enumerate
#i =>pode ser chamado de qualquer coisa (i, j, m, n )

for i, linha in enumerate(matriz):
    print(f"Linha{i+1}: {linha}")

for linha in matriz:
    print(linha)
    for numero in linha:
        print("Valor: ", numero)

i = 0
while i < len(lista_nova):
    print("Npumero: ", lista_nova[i])
    i += 1
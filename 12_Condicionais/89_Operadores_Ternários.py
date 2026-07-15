#Oferecem uma maneira de escrever condições simples. reduzindo o uso de estruturas if-else:
idade = 20
resultado = "Maior de idade" if idade >=18 else"Menor de idade"
print(resultado)

if idade >=18:
    resultado = "Maior de idade"
else:
    resultado ="Menor de idade"

numero = 8
paridade = "É par" if numero % 2 ==0 else "Não é par"
print(paridade)

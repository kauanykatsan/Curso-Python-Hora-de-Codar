#if-else é usada para tratar dois cenários possíveis
#sempre garenta que ambos os blocos de código estejam devidamente identados para evitar erros

numero = 11
if numero % 2==0:
    print("é par")
else:
    print("é impar")


idade = 15
if idade >=18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

valor = int(input("Digite um número positivo: "))


if valor > 0:
    print(f"O valor {valor} é positivo")

else:
    print("O numero digitado é negativo! Tente novamente.")

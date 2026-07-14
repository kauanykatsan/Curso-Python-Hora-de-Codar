#APLICAÇÃO DE OPERADORES EM CONDIÇÕES E CÁLCULOS

entrada = input("Digite um número: ")

numeros = [1,2,3,4,5]

if int(entrada) in numeros:
    print("Você acertou!")

idade = 25
renda = 6000

if idade < 30 and renda > 5000:
    print("Você ganha bem!")


frase = "PHP e Python são lingugens de programação"
if "Python" in frase and "PHP" in frase:
    print("O texto fala sobre Pythone e PHP")

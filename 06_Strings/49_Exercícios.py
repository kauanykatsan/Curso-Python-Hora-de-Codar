#Exercício 1
#Crie uma String com a frase "Python é incrivel", substitua a palavra "incrivel" por "fantástico" e exiba o resultado


texto = "Python é incrivel"
print(texto.replace("incrivel", "fantástico"))

#Exercicio 2
#Escreva um programa que receba o nome completo de um usuário, divida o nome em parte e exiba o primeiro e o último nome separadamente 
nome_completo = input("Digite seu nome completo: ")
partes = nome_completo.split()

primeiro_nome = partes[0]
segundo_nome = partes[1]
print("Primeiro nome:", primeiro_nome)
print("Segundo nome: ", segundo_nome)


#Exercício 3 
#Desenvolva um programa que solicite uma lista de itens separadamente por vírgula e os exiba em uma única string, com os itens separados por ponto e vírgula
itens = input("Digite uma lista de itens separados por vírgulas: ")

lista = itens.split(",")
resultado = ";".join(lista)

print("Itens formatados: ", resultado)


#Exercício 4
#Crie uma string multilinha com uma mensagem de boas-vindas que inclua variáveis como o nome de usuário e a data atual, formatada com f-strings
from datetime import date
nome_usuario = input("Digite seu nome: ")
data_atual = date.today().strftime("%d/%m/%y")

mensagem = f'''
     Bem-vindo {nome_usuario}!
     Hoje é {data_atual}
'''

print(mensagem)


#Exercício 5
#Escreva um programa que receba uma string, conte o número de vogais na string e exiba o total de vogais encontradas 
texto = input("Digite uma string: ")

vogais ="aeiouAEIOU"

contador = sum(1 for char in texto if char in vogais )
print("Total de vogais: ", contador)





# ENUNCIADOS E DESCRIÇÕES
'''
# Exercício 1:
# Enunciado: Escreva um programa que solicite dois números ao usuário e use operadores de comparação
# para verificar se o primeiro número é maior, menor ou igual ao segundo. Exiba os resultados.
# Descrição: O programa deve capturar dois números do usuário, realizar as comparações com operadores
# (<, >, ==) e exibir mensagens indicando a relação entre os números.

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))

if n1 > n2:
    print("O primeiro número é maior que o segundo")
elif n1 < n2:
    print("O segundo número é maior que o primeiro")
else:
    print("Os valores são iguais")

# Exercício 2:
# Enunciado: Desenvolva um programa que receba três números e determine se o primeiro é menor que o
# segundo e maior que o terceiro utilizando operadores combinados.
# Descrição: O programa deve capturar três números e verificar a relação combinada entre eles usando
# operadores (<, >) em uma única expressão.

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
n3= float(input("Digite o terceiro número:"))

if n1 < n2 and n1 > n3:
    print("O primeiro número está entre o segundo e terceiro número")

# Exercício 3:
# Enunciado: Crie um programa que receba a idade de uma pessoa e verifique se ela está apta a votar
# (idade maior ou igual a 16) ou a dirigir (idade maior ou igual a 18) usando operadores lógicos.
# Descrição: O programa deve capturar a idade do usuário, aplicar condições com operadores (and, or)
# e exibir as mensagens correspondentes às permissões.

idade = float(input("Quantos anos você tem? "))
if idade  >=18:
    print("Você já pode votar e dirigir")
elif idade >= 16:
    print("Você já pode votar")
elif idade > 16 and idade< 18:
    print("Você pode votar mas não pode dirigir")
else:
    print("Você ainda não pode votar e nem dirigir")
'''
# Exercício 4:
# Enunciado: Escreva um programa que compare duas listas para verificar se elas ocupam o mesmo espaço
# na memória usando operadores de identidade (is) e verifique se um elemento específico está presente
# em ambas usando operadores de associação (in).
# Descrição: O programa deve criar duas listas, realizar a comparação de identidade com (is) e verificar
# a presença de um elemento em ambas as listas usando (in).

l1 = [1,2,3]
l2 = [1,2,3]

numero = 3
print(l1 is l2)
print(numero in l1 and numero in l2)



# Exercício 5:
# Enunciado: Implemente um sistema de validação de login que verifica se o nome de usuário e a senha
# inseridos estão corretos, combinando operadores lógicos, de associação e de comparação.
# Descrição: O programa deve verificar se as credenciais inseridas pelo usuário coincidem com as
# credenciais armazenadas e exibir mensagens de sucesso ou erro.



usuario = 'kauany.katsan@gmail.com'
senha = '12345'

usuario_t = input("Digite seu email: ")
senha_t = input("Digite sua senha: ")

if usuario_t == usuario and senha_t == senha:
    print("Login efetuado com sucesso!")
else:
    print("Email ou senhas errados! Tente novamente.")

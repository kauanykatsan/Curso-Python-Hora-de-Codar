#Aula 24
#Round(): Permite reduzir o número de casas decimais de um float
#Funções de Piso e Teto: math.floor()earredondando para o menor inteiro
# E match.ceil para o maior inteiro próximo
#Mitigação de Erros: utilizar strings ou bibliotemas como decimal para maior precosão em aplicações críticas


numero = 2.6575

num_arredondado = round(numero, 2)  #Arredonda para 2 casas decimais
print(num_arredondado)

#biblioteca math
import math

valor = 7.9

valor_cima = math.ceil(valor)  #Arredonda par ao próiximo inteiro
valor_baixo = math.floor(valor) #Arredonda para baixo
print(valor_cima, valor_baixo)

resultado = 0.1 + 0.2
print(f"O resultado é {resultado:.2f}")   #Número de uma forma mais precisa

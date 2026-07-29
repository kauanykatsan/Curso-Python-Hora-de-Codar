#USO DE TUPLAS EM FUNÇÕES E RETORNOS MULTIPLOS
#Tuplas sao frequentemente usadas para retornar multiplos valores de uma funcao de forma eficiente e organixada
#Permitem agrupar valores relacionados, eliminando a necessidade de criar classes ou estruturas complexas para retornos simples 
#Sõ imutaveis, garantindo que os danos retornados por uma funcao são sejam alterados acidentalmente
#Atribuições múltiplas com tuplas tonam o código mais limpo e fácil de entender, especialmente ao lidar com valores relacionados
#Combinadas com desempacotamento, as tuplas facilitam as minipulações dedados retornados as funções
#Usar tuplas em funções ajuda a melhorar a modularidade e a çegibidade do código


def dividir(numerador, denominador):
    quociente = numerador // denominador
    resto  = numerador % denominador
    return quociente, resto

resultado = dividir(10, 3)

print(resultado)

print(f"Quociente {resultado[0]} e Resto {resultado [1]}")

#Envia os dados para função, faz as divisões, retorna uma tipla, desempacotando a tupla 2
quociente, resto = dividir(20, 2)
print(quociente, resto)


def calcular_area(dimensoes):
    largura, altura = dimensoes
    return largura * altura

area = calcular_area((5,4))
print(area)

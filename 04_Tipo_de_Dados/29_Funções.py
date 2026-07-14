#Aula 29 Funções Matemáticas Embutidas
# ABS, ROUND, POW, DIVMOD

numero = -15

numero_abs = abs(numero)
print(numero_abs)

numero_quebrado = 1.54614542
print(round(numero_quebrado, 2))
    
base=2
expoente= 5
modulo= 3

resultado = pow(base, expoente)
print(resultado)

quociente, resto = divmod(20, 6)  # 3 x 6, 20-18=2
print(quociente, resto)

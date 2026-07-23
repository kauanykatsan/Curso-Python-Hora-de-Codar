#CONTROLE DE FLUXO EM LOOPS COM CONTINUE
#pula a execução restante no loop atual e inicia a pr[oxima iteração imediatamente
numeros = [1, -3, 4, -5, 9, -12]

for numero in numeros:
    if numero <0:
        print("O número é ", numeros)

texto = "Python3.123456"
for letra in texto:
    if not letra.isalpha():
        continue
    print("Letra: ", letra)

for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)

#Break encerra o loop
#Continue pula para a proxima execucao

#COMBINAÇÃO DE BREAK E CONTIUNUE EM FLUXOS
#combinar esse dois permite criar fluxos de controle avançados e personalizados


for numero in range(20):
    if numero % 2 !=0:
        continue

    if numero % 5 ==0:
        print(f"Primeiro numero divisivel por 5: {numero}")
        break
    print(numero)


for numero in numeros:
    if numero < 0:
        continue

    elif numero >5:
        print("Número maior que o previsto, parando loop...")
        break


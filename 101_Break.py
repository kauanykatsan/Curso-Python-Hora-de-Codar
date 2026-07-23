#CONTROLE DE FLUXOS EM LOOPS COM BREAK

#usado para interromper a execução de um loop antes que ele seja concluido normalmente
#Ajuda a evitar processamento desnecessário

for numero in range (1, 50):
    print("Número: ",numero)

    if numero % 7 == 0:
        print("Encontramos o numero ", numero)
        break


while True:
    comando  = input("Digite 'sair' para encessar: ")
    if comando.lower()=='sair':
        print("Encerrando programa...")
        break

    print(comando)

frutas = ['maça', 'banana', 'una', 'laranja']
for fruta in frutas:
    print(fruta)

    if fruta == 'uva':
        print("Encontramos a uva")
        break
#Ocorrem quando um bloco if esta dentro de outro 

idade = 18
if idade>=18:

    print("Você é maior de idade!")
    if idade >=21:
        print("Você pode consumir bebida nos EUA!")
    else:
        print("Você não pode consumir bebida nos EUA!")


else:
    print("Você é menor de idade!")


nota = 10
if nota>=7:
    
    if nota == 10:
        print("Você tirou nota máxima!")

    print("Você foi aprovado!")

else:
    print("Você esta de recuperação")



lista = []
if len(lista) > 0:
    if 2 in lista:
        print("O numero 2 esta na lista!")
    else:
        print("O numero 2 não esta na lista")
else:
    print("Alista está vazia!")

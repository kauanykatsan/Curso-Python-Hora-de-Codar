'''
Gerar a tabuada de um número fornecido pelo usuário, exibindo os resultados de 1 a 10

'''

def tabuada():
    print("Bem-vindo a tabuada!")

    try:
        #Solicitar o número para o usuário
        numero = int(input("Digita um número: "))
        print(f"Exibindo a tabuada do número {numero}: ")

        for i in range (1, 11):
            print(f"{numero}x{i} = {numero *i}")

    except ValueError:
        print("Por favor, insira um número inteiro válido.")


if __name__ == "__main__":
    tabuada()

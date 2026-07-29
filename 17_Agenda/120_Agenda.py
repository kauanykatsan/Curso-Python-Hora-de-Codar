def exibir_contatos(contatos):
    if not contatos:
        print("A agenda esta vazia...")
    else:
        for i, contato in enumerate(contatos, start =1):
            print(contato)
            nome, telefone, email = contato
            print(f"{i}. Nome: {nome}, Telefone: {telefone}, E-mail: {email}")





def adicionar_contatos(contatos):
    nome=input("Digite o nome do contato: ")
    telefone=input("Digite o número de telefone: ")
    email=input("Digite o email:")

    novo_contatos = (nome, telefone, email)

    return contatos + (novo_contatos, )



def main():

    contatos = ()




    while True:
        print("Menu de Agenda")
        print("1-Exibir contatos")
        print("2-Adicionar contatos")
        print("3-Sair")

        

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("Exibindo contatos...")


            exibir_contatos(contatos)
        elif opcao == "2":
            print("Adionando novo contato...")
            contatos = adicionar_contatos(contatos)


        elif opcao == "3":
            print("Saindo do programa..")
            break


    
        else:
            print("Opção inválida! Tente novamente.")



if __name__ == "__main__":
    main()

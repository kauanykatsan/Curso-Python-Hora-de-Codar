'''
    Lista de compras funções:

    Adiconar um item a uma lista
    Remover item
    Visualizar item
    Limpar lista

'''

#Menu
def exibir_menu():
    print("Gerenciador Lista de Compras:")
    print("1 - Gerenciar item")
    print("2 - Remover item")
    print("3 - Visuaizar item")
    print("4 - Limpar a Lista")
    print("5 - Sair")


#Adiciona item a lista
def adicionar_item(lista):
    item = input("Digite o nome do item: ")
    lista.append(item)
    print(f"{item} foi adicionado a sua lista.")


#Remover item da lista
def remover(lista):
    if len(lista) == "0":
        print("A lista está vazia")
        return
    item = input("Digite o item que você deseja remover: ")
    if item in lista:
        lista.remove(item)
        print(f"O item '{item}' foi removido da lista.")
    else:
        print(f"O item '{item}' não foi encontrado na lista")


#Visualiza itens da lista
def visualizar_lista(lista):
    if len(lista) == 0:
        print("A lista está vazia")
    else:
        print("Lista de Compras")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")

#Limpar lista
def limpar_lista(lista):
    lista.clear()
    print("A lista agora está vazia.")





def gerenciador_lista_de_compras():
    lista_compras = []
    while True:
     exibir_menu()
     opcao= input("Escolha uma opção: ")


# um if e 4 elif = para se tornar uma unica operação
     if opcao == "1":
         adicionar_item(lista_compras)
     elif opcao == "2":
         remover(lista_compras)
     elif opcao == "3":
        visualizar_lista(lista_compras)
     elif opcao == "4":
        limpar_lista(lista_compras)
     elif opcao == "5":
       print("Obrigado por utilizar o gerenciador!")
       break
     else:
        print("Operação inválida. Digite outro número.")



#Iniciar programa
if __name__ == "__main__":
    gerenciador_lista_de_compras()




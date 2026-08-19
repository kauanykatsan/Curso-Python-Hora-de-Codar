#INVENTÁRIO
#1- Cadastrar novos produtos
#2- Atualizar a quantidade
#3- Consultar o estoque 

def exibir_menu():
    print("----Bem-vindo ao sistema de inventário----")
    print("1 - Adicionar produto")
    print("2 - Atualizar quantidade")
    print("3 - Consultar estoque")
    print("4 - Remover produto")
    print("5 - Sair")

    return input("Escolha uma opção: ")

def adicionar_produto(inventario):
    produto = input("Digite o nome do produto: ")
    if produto in inventario:
        print("O produto ja esta cadastrado!")
    else:
        quantidade = int(input("Digite a quantidade inicial do produto: "))
        inventario[produto]= quantidade
        print(f"O produto {produto} foi adicionado com sucesso!")

def consultar_estoque(inventario):
    if not inventario:
        print("O estoque está vazio!")
    else:
        print("---Estoque atual---")
        for produto, quantidade in inventario.items():
            print(f"{produto.capitalize()}: {quantidade} unidades")


def atualizar_quantidade(inventario):
    produto = input("Digite o nome do produto para atualizar: ")
    if produto not in inventario:
        print("O produto não existe!")
    else:
        quantidade = int(input("Digite a quantidade atual do produto: "))
        inventario[produto]= quantidade
        print(f"O produto {produto} foi atualizado!")

def remover_produto(inventario):
    produto = input("Digite o nome do produto que deseja remover do Inventário: ")

    if produto not in inventario:
            print("O produto não existe!")
    else:
        del inventario[produto]
        print("Produto removido com sucesso!")


def main():
    inventario = {}
    while True:
        opcao= exibir_menu()

        if opcao == "1":
            print("Adionar produto: " )
            adicionar_produto(inventario)


        elif opcao == "2":
            print("Atualizar quantidade: ")
            atualizar_quantidade(inventario)
           
        
        elif opcao == "3":
            print("Verificar estoque")
            consultar_estoque(inventario)
                    
        elif opcao == "4":
            print("Remover produto do inventário:")
            remover_produto(inventario)
            
        elif opcao == "5":
            print("Saindo do Sinstema de Inventário...")
            break

        else:
            print("Digite uma opção válida!")


if __name__ == "__main__":
    main()
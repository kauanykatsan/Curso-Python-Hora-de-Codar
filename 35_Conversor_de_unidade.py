#converter celsius para F
#converter F para C

def celsius_para_fahreinheit(celsius):
    return(celsius * 9/5) +32

def fahreinheit_para_celsius(fahreinheit):
    return (fahreinheit - 32) *5/9

def menu():
    print("Bem-vindo ao Conversos")
    print("Escolha uma opção")
    print("1-Converter de Celsius para Fahreinheit")
    print("2-Converter de Fahreinheit para Celsius")
    print("3-Sair")

def conversor_temperatura():
    menu()
    opcao = input("Digite a opção desejada (1/2/3): ")

    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahreinheit = celsius_para_fahreinheit(celsius)
        print(f"{celsius: 2f} é equivamente a {fahreinheit: 2f}F")

    elif opcao == "2":
        fahreinheit = float(input("Digite a tempertuta em Fahreinheir: "))
        celsius = fahreinheit_para_celsius(fahreinheit)
        print(f"{fahreinheit} é equivalente a {celsius}")
              
    elif opcao =="3":
        print("Obrigado por utilizar o Conversor!")

    else:
        print("Opção Inválida! Digite apenas 1, 2 ou 3")

 #Inicialização do sistema
if __name__ == "__main__":
    conversor_temperatura()
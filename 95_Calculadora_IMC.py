def calcular_imc():
    print("Bem-vindo a calculadora de IMC!")

    peso=float(input("Digite seu peso: "))
    altura=float(input("Digite sua altura: "))


    
    #Calcular IMC
    imc = peso / (altura**2)
    print(f"Seu IMC é {imc: .2f}")



    #Exibir a categoria do usuario
    if imc <18.5:
        print("Classificação: Abaixo do peso!")
    elif imc <24.9:
        print("Classificação: Peso normal!")
    elif imc <29.9:
        print("Classificação: Sobrepeso!")  
    elif imc <34.9:
        print("Classificação: Obesidade Grau1!")  
    elif imc <39.9:
        print("Classificação: Obesidade Grau 2!")  
    else :
        print("Classificação: Obesidade Mórbita!")  



if __name__ == "__main__":
    calcular_imc()

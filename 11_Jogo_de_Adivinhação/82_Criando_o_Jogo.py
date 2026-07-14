# Gerar um numero aleatorio
# Verificar se o usuario acertou
# Contabilizando as tentativas


import random  #do próprio Python - vai gerar um número aleatório

def jogo_adivinhacao():
    print("Bem-Vindo ao Jogo da Adivinhção")
    print("Tente adivinhar um número aleatório de 1 a 100!")
    
    #Gerar um numero aleatorio
    numero_secreto = random.randint(1 , 100)
    #Inicializar variaveis que vão ajudar o sistema a contabilizar as jogadas
    tentativas = 0
    acertou = False


    while not acertou: 
        
        palpite = int(input("Digite seu palpite:  "))
        tentativas += 1 
        #Verificar o palpite
        if palpite == numero_secreto:
            print(f"Parabéns, você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
        elif palpite < numero_secreto:
            print("O número secreto é maior. Tente novamente.")
        else:
            print("O número secreto é menor. Tente novamente.")

#Inicializar o programa
if __name__=="__main__":
    jogo_adivinhacao()


#Receber um texto
#E terminar quantas palavras, caracteres e linhas o texto tem

def analisar_texto(texto):
    
    #contar linhas wefew
    linhas = texto.splitlines()  #Splitline separa o texto pelas linhas
    numero_linhas=len(linhas) #Len conta quantas elementos existem

    #contar palavras
    palavras = texto.split() #Separa o texto em palavras
    numero_palavras = len(palavras)

    #contar caracteres
    numero_caracteres = len(texto)

    return numero_linhas, numero_palavras, numero_caracteres

def main():
    print("Bem-vindo ao analisador de texto")
    print("Digite o seu texto abaixo, e para finalizar pressione Enter duas vezes")

    #Entrada de texto
    texto = ""
    while True:  #Laço de repetição
        linha=input()
        #condição de encerramento
        if linha == "":
            break
        texto += linha + "\n"


    linhas, palavras, caracteres = analisar_texto(texto)


    print("Resultado da análise: ")
    print(f"Numero de linhas: {linhas}")
    print(f"Numero de palavras: {palavras}")
    print(f"Numero de carascteres: {caracteres}")

if __name__ == "__main__":
    main()




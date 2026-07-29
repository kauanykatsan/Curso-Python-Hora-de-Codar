def comparar_listas(lista1 , lista2):
    conj1 = set(lista1)
    conj2 = set(lista2)

    #INTERSEÇÃO, DEIFERENÇA, DIFERENÇA INVERSA, DIFERENÇA SIMÉTRICA
    em_ambas = conj1 & conj2
    somente_1 = conj1 - conj2
    somente_2 = conj2 - conj1
    uma_ou_outra = conj1 ^conj2

    print("=====COMPARAÇÃO DE LISTAS=====")
    print(f"Alunos em ambas as listas: {em_ambas}")
    print(f"Alunos somente na primeira lista: {somente_1}")
    print(f"Alunos somente na segunda lista: {somente_2}")
    print(f"Alunos que esão em Somente uma das listas {uma_ou_outra}")
    

def main():
    print("Bem-vindo ao programa de Comparação de Listas de Alunos")
    print("Digite os nomes dos alunos, e os separe por vírgula")


#Criando as listas
    lista1 = input("Digite os nomes da primeira lista: "). split(",")
    lista2 = input("Digite os nomes da segunda lista: "). split(",")

    #Remover os espaços em branco
    lista1 = [aluno.strip() for aluno in lista1]
    lista2 = [aluno.strip() for aluno in lista2]

    comparar_listas(lista1, lista2)
    


if __name__ == "__main__":
    main()
"""
EXERCÍCIO 1: Criando e manipulando um dicionário de alunos
DESCRIÇÃO: Crie um dicionário para armazenar nomes de alunos como chaves e suas notas como valores. 
Adicione três pares chave-valor ao dicionário, remova um aluno usando a chave e exiba o restante 
dos pares no dicionário formatados.
"""

print("Dicionários de alunos: ")
print("Lista de alunos:")
alunos = {"Ana": 9.5, "Bruno": 5.7, "Carlos": 10.00}
print(alunos)

remover = input("Digite o nome do aluno que deseja remover: ")

if remover in alunos:
    remover = alunos.pop(remover)

    print(alunos)
    print("Aluno removido com sucesso!")

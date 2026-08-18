"""EXERCÍCIO 3: Iterando sobre dicionários para exibir informações
DESCRIÇÃO: Crie um dicionário com informações de um funcionário, incluindo nome, cargo e salário. 
Use um loop for para iterar sobre o dicionário e exibir as informações formatadas chave por valor.
"""
print("Dados do funcioário: ")
funcionario = {"nome": "João", "cargo": "Analista", "salário": 3500.00}
for chave, valor in funcionario.items():
    print(f"{chave.capitalize()}: {valor}")

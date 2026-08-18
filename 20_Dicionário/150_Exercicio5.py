"""EXERCÍCIO 5: Trabalhando com dicionários aninhados para organização de dados
DESCRIÇÃO: Crie um dicionário aninhado para armazenar informações de clientes. Cada cliente deve 
ter um identificador único e conter informações como nome, idade e cidade. Exiba os dados de 
cada cliente formatados em linhas separadas.
"""

clientes = {
    "cliente1": {"nome": "Julia", "idade": 17, "cidade": "Sinop"},
    "cliente2": {"nome": "Paulo", "idade": 38, "cidade": "Floripa"},
    "cliente3": {"nome": "Julio", "idade": 24, "cidade": "Rio de Janeiro"}
}

for cliente, dados in clientes.items():
    print(f"{cliente.capitalize()}")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()} - {valor}")

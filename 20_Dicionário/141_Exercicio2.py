"""EXERCÍCIO 2: Acessando e filtrando valores em um dicionário
DESCRIÇÃO: Dado um dicionário com produtos e seus preços, filtre apenas os produtos com preço 
acima de R$50,00. Exiba o nome e o preço de cada produto que atenda a esse critério.
"""

produtos = {"Maça": 3.50, "Detergente": 4.75, "Pão": 0.75}
print("Produtos com preço acima de R$4,00: ")
filtro = {produto : preco for produto, preco in  produtos.items()if preco > 4.00}
print(filtro)

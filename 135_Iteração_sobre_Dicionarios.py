#ITERACO SOBRE DICIONARIOS COM FOR 
produto = {"nome": "Camisa", "preço": 20.90, "cor": "Preta"}

for chave in produto:
    print(chave)
    print(produto[chave])
    if chave == "nome":
        print(f"O nome do produto é: " + produto [chave])

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f"{chave} - {valor}")
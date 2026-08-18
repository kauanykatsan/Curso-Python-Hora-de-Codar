numeros = [1, 2, 3, 4]
produto = {"nome": "Camisa", "preço": 20.90, "cor": "Preta"}
quadrados = {num: num**2 for num in numeros}
print(quadrados)

filtrar = {chave: valor for chaves, valor in produto.items() if isinstance(valor, int)}
print(filtrar)
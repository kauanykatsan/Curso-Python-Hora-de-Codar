produto = {"nome": "Camisa", "preço": 20.90, "cor": "Preta"}
id_produto = produto.get("id")
print(id_produto)

config = dict.fromkeys({"tema", "volume", "idioma"}, "Padrão")
#dict.fromkeys cria um novo dicionário usando uma sequência de elementos como chaves e atribuindo a todos eles um mesmo valor opcional (que padrão é None se não for informado)

print(config)
produto_copia = produto.copy()
produto_copia['preço']=50
print(produto)
print(produto_copia)

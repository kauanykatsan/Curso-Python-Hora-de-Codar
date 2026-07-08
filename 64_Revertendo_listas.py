#O método Reverse() inverte a ordem dos elementos da lista diretamente, modificando a lista original)

cidades = [
    "São Paulo",
    "Rio De Janeiro",
    "Curitiba",
    "Chapecó"
]

cidades.reverse()#inverte
print(cidades)

cidades_p = list(reversed(cidades))#para voltar ao normal=cópia de segurança

print(cidades)
print(cidades_p)

nums= [1, 2, 3, 4, 5]
nums.reverse()
print(nums)



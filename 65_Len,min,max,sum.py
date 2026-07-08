#Len(lista) retorna o número de elesmentos da lista, útil pars verificar o tamanho de listas
#min(lista)encontra o menor elemento da lista, enquanto
#max(lista)retorna o maior valor com suporte para numeros strings
#sum(lista)calcula a soma de todos os elementos da lista, aplicavel apenas a listas numéricas


numeros = [10, 20, 30, 40, 50]
print(len(numeros))

print("Valor Máximo: " , max(numeros))
print("Valor Mínimo: " , min(numeros))

print("Soma dos valores: ", sum(numeros))

#kay, trabalhar com tamanho de strings em min e max
cidades = [
    "São Paulo",
    "Rio De Janeiro",
    "Curitiba",
    "Chapecó"
]


print("Maior cidade: ", max(cidades, key=len))
print("Menos cidade: ", min(cidades, key=len))

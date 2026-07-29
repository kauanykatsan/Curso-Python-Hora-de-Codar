#FROZENSET é uma versão imutável de conjuntos(set), garantindo que os elementos não possam ser alterados após a criaçõa

lista = [1,2,3,4,5]
fs = frozenset(lista)

print(fs)

fs2 = frozenset({4,5,6,7})

print(fs.union(fs2))
print(fs.intersection(fs2))

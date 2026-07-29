#OPERACOES MATEMATICAS COM CONJUNTOS

#A união (| oi union()) retorna um conjunto contendo todos os elementos únicos de dois conjuntos
#A interseccao (& ou intersection()) retonr os elemntos comuns entre dois conjuntos
#A diferença ( - ou difference()) retorna os eementos do primeiro conjunto que não estão no segundo
conj1 = {1,2,3}
conj2 = {2,4,6,8}

uniao = conj1 | conj2
print(uniao)

interseccao = conj1 & conj2
print( interseccao)

diferenca = conj1 - conj2
print(diferenca)


diferenca2 = conj2 - conj1
print(diferenca2)


#MESMOS RESULTADOS, MAS ATRAVES DE MÉTODOS
print(conj1.union(conj2))
print(conj1.intersection(conj2))
print(conj1.difference(conj2))

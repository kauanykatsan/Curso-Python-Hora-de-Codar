# Trabalhando com métodos de conjuntos

#O método add() insere um elemento único no conjunto, ignorando duplicados automaticamente
#O retodo remove() elimina um elemento específico, mas gera um erro se o elemento nãõ existir
#O método discard() remove um elemento sem erro, mesmo se o elemento não estiver no conjunto
#pop() remove e retorna um elemento arbitrário do conjunto, útil para processamento iterativo
#clear() remove todos os elementos, deixando o conjunto vazio

#ADD
conj1 = {1,2,3,4,5,6,7,8}
conj1.add(10)
print(conj1)


#REMOVE -> pelo valor do elemento
conj1.remove(2)

#DISCARD->remove sem erro
conj1.discard(99)
#ERRO: conj1.remove(99)

print(conj1)

conj1.clear()

print(conj1)
#O método remove() expclui a primeira ocorrência de um valor específico na lista: se o valor não for encontratado gera um erro
#O metodo append() adiciona um elemento ao final da lista, aumentando seu tamanho dinamicamente

animais = ["cachorro", "gato"]

animais.append("pássaro") #append= inserir no final 
print(animais)

animais.insert(1, "coelho") #insert= inserir no meio com posição especifica 
print(animais)


numero = []
numero.append(5)
#indice 0 = inserindo no inicio da lista
numero.insert(0,10)
print(numero)



#Aula 57
print(animais)

animais.remove("gato")
print(animais)

primeiro_elemento = animais.pop(1) #POP para recuperar esse elemento removido 
print(animais)
print(primeiro_elemento)

animais.pop()#Se utilizar o Pop sem indise vai acontecer a remoção do último elemento 
print(animais)




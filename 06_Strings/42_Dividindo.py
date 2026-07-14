#Uso do metodo Split()
#Dividindo String

#O método split() divide uma string em uma lista de sibstrings
#Com base em um delimitador especifico(por padrão, epsaço)

#Dividir palavras
frase = "Python é muito divertido"
lista_frase = frase.split()
print(lista_frase)



#indices de lista tambem começam com 0
print(lista_frase[1])
string_caracteres = "teste-testando-testou"
print(string_caracteres.split("-"))


#Maxsplit = finciona por numero de indices
print(frase.split(" ", 1))


#Replace
texto = "Python é ótimo"

print(texto.replace("ótimo", "perfeito"))

palavras = "maça laranja maça banada maça"

#Terceiro argumento: quantidade de substrituicoes
print(palavras.replace("maça","teste", 2))

#limpar caracteres
texto = "sei la @ teste "

print(texto.replace("@", ""))

print(texto)
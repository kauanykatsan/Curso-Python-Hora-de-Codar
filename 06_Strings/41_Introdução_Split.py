#Strings Possuem diversos metodo embutidos que facilitam a manipulação de texto 
#Metodos de String

texto = "Python é muito legal"

#Formatação
print(texto.upper()) #Maiusculo
print(texto.lower()) #Minusculo
print(texto.capitalize()) #Somente a primeira Maiuscula

#Remoção de espaço
espacos = " teste aqui "
espacos_limpos = espacos.strip()

print(espacos)
print(espacos_limpos)

#Substituição de caracteres
print(espacos.replace("python", "php")) #Substituição da palavra Python para Php
dados = "nome, telefone, endereco"

dados_separados = dados.split(", ")
print(dados_separados)

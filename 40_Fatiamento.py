#Permite extrair substrings usando a notação [inicio:fim:passo]
#Onde inicio é inclusivo e fim é exclusivo
#Fatiamento é uma ferramenta poderosa para extrair e manipular partes da strings em tarefas como validação e formataçõa

frase = "Bom dia"

subfrase = frase[:3]

print(subfrase)
print(frase[-6:])

#Fatiamento com passo
print(frase[::2])

#Inverter string

print(frase[::-1])


#Fatiamento além do limite
print(frase[5:100])

#Indice final exclusivo
print(frase[:3])

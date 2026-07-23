#Strings podem ser iteradas caracter por caracter, ermitindo análise ou transformação de texto

#Iteração sobre Strings, Listas e Dicionários
texto = "Python"
for letra in texto:
    print(f"Letra: {letra}")

dados={
    "nome": "Matheus",
    "Idade": 33,
    "esta_trabalhando":True
}


for chave in dados:
    print(f"Chave{chave} - Valor {dados[chave]}")

print(dados['nome'])

for chave, valor in dados.items():
    print(f"{chave} - {valor}")
    
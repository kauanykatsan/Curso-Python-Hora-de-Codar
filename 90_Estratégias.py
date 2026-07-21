#Estratégias para evitar condicionais aninhadas

def verifica_idade(idade):
    if idade < 18:
        return "Menor de idade"
    
    return "Maior de idade"

print(verifica_idade(16))
print(verifica_idade(26))

opcoes = {
    "vermelho":"Pare",
    "amarelo":"Atenção",
    "verde":"Siga"}

cor=input("Digite uma cor (verde, vermelho ou amarelo): ")
print(opcoes.get(cor, "Cor inválida!"))

idade=25
renda=3000
if idade> 18:
    if renda>2000:
        print("Elegível")


if idade > 18 and renda>2000:
    print("Elegivel")
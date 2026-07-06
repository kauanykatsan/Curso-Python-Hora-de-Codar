#Uso de Strings Multilinha Com Aspas Triplas
#São criadas usando aspas triplas (""ou  """) permitindoincluir várias linhas de testo em uma única variável
#Pode ser usado para armazenar menagens longas, como banners, contratos ou descrições detalhadas


texto = """Este é meu 
texto
com multilinha"""

print(texto)

texto2 = '''Este
também é
multilinha'''

print(texto2)

"""
    Função teste 
    Não aceita parametros
    E retorna o valor 1
"""
# Isso é o mesmo que um comentário, ele não funciona
def teste():
    return 1

nome = "Matheus"

frase = f"""Meu nome é
{nome}
tudo bem?"""

print(frase)

texto_com_escape = """
Qualquer coisa
\nteste\nteste
pulou linha"""

print(texto_com_escape)

#\n pula linha 
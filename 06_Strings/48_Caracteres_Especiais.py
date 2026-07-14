#Caracteres especiais em strings começam com uma barra invertida (\). Permitindo incluir novas linhas tabulações e aspas
#Sequências comuns incluem :
# \n(nova linha)
# \t(tabulação) = tabelas
# \'(aspas simples)
# \"(aspas duplas)


texto = "Testando\nCaracteres\nEspeciais"
print(texto)

aspas = "E quando \"colocar \"aspas"
print(aspas)

caminho_pasta = r"C:\users\Kau\Teste.txt"   #O R na frente faz a função funcionar e desconsidera as barras invertidas
print(caminho_pasta)

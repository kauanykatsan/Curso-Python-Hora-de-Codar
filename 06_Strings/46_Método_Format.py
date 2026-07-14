#O método format() permite inserir variáveis ou valores em strings usando marcadores
#Suporta argumentos posicionais e nomeados, facilitando a organizaçõa de dados complexos de strings
#é uma ferramenta poderosa para manipulação de strings

print("Meu nome é {} e eu tenho {} anos".format("Aline", 23))

valor = 1.123456789

print("O valor formatado é {:.3f}".format(valor))#(:) inicia as regras da formatção (.) Define o mimite de casas decimais (F) Numero flutuante - Float

print("Ordem de parametros invetida {1} e {0}".format("Primeiro", "segundo"))

#baseado no ao de nascimento do usiario
#calcular a idade dele
#2025 ou 2026

from datetime import datetime
#datetime = várias funcionalidades para lidar com datas
ano_atual = datetime.now().year

# print(ano_atual) == mosra o ano atual

ano_nascimento = int(input("Digite em que ano você nasceu: "))

idade = ano_atual - ano_nascimento
print(f" Você tem {idade} anos." )


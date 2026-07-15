#Operadores lõgicos : and, or, not

idade = 23
renda = 900

if idade  < 30 and renda < 1800:
    print("Você pode participar do programa!")

usuario = 'kauany'
senha=1234

if usuario == 'kauany' and senha == 1234:
    print("Você logou no sistema!")
else:
    print("Login ou senha erradas")


x=10
y=20
z=20
if x < y or y<z and x==10:
    print("Verdadeiro!")
else:
    print("Falso!")




x=10
y=20
z=20
if (x < y or y<z) and x==10:
    print("Verdadeiro!")
else:
    print("Falso!")

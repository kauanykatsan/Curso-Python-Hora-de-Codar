#IS verifica se duas variáveis apontam para o mesmo objeto na memória, retornando True ou False
#Not é a negação de is, retornando True se as variáveis não apontarem para o mesmo objeto


#USO DE IS & iS NOT
x = None
print(x is None)
print(x == None)
print(x is not None)


a = 10
b = 10

print(a is b)
print(a == b)

lista = [1, 2, 3]
lista2 = [1, 2, 3]

print(lista is lista2)
print(lista==lista2)

s1 = "Python"
s2 = "Python"

print(s1 is s2)
print(s1 == s2)




d = {}
d2 = {}

print(d is d2)

t = ()
t2 = ()
print(t is t2)


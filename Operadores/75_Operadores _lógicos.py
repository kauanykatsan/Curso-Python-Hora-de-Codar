#AND retorna True se ambas as combinações forem verdadeiras, sendo útil para verificar múltiplas condições ao mesmo tempo
#OR retorna True se pelo menos uma condição for verdadeira, permitindo maior flexibilidade
#NOT inverte o valor ógico de uma condição, tranformando True em False e vice-versa

idade= 25
print(idade > 18 and idade <30)

print(idade < 18 or idade > 65)

print(not True)

a = 10
b = 5
c = 6
d = 7

print(a > b or  c == d)  #Ficou True pq o Or necessita de somente um True para permanescer True

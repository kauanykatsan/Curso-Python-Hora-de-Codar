#DIFERENÇA SIMÉTRICA E TESTES DE SUBCONJUNTOS
#OPERACOES AVANCADAS
#A difereça simétrica ^ou symmetric_difference() retorna os elementos que estão em um conjunto ou no outro, mas não em ambos
#Testes de subconjuntos (issobset()) verificam se todos de um elemento do conjunto estão contidos em outro
#Testde de subconjuntos (issoperset()) verificam se um conjunto conté, todos os elementos do outro conjunto



conj1 = {1,2,3}
conj2 = {2,4,6,8}

#diferença simétria   - retira elementos que são iguais nos conjuntos
sim = conj1 ^ conj2
print(sim)

sim2= conj1.symmetric_difference(conj2)
print(sim2)

subconjuntos = {1,2}
subconj2 = {99, 101}

#issubset -> SUBCONJUNTOS -> CONJUNTO
print(subconjuntos.issubset(conj1))
print(subconj2.issubset(conj2))

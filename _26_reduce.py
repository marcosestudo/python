'''
o criiador do python disse pra usasr reduce somente se necessário
já que em 99% das vezes um loop for seria mais legível
reduce() recebe dois argumentos, uma função e um iterável
passa pra função como argumentos o resultado anterior e o proximo elemento do iterável 
'''
import functools


dados = [1, 2, 3, 4, 5]
# def funcao(a, b):
#     return a, b

# print(functools.reduce(funcao, dados))

# v o que o reduce passa pra função v
# resultado1 = funcao(1, 2)
# resultado2 = funcao(resultado1, 2)
# resultado3 = funcao(resultado2, 3)
# resultado4 = funcao(resultado3, 4)
# resultado5 = funcao(resultado4, 5)
# reduce() == funcao(funcao(funcao(funcao(1, 2), 3), 4), 5)


print(functools.reduce(lambda a, b: a + b, dados))

somatorio = 0
for x in dados:
    somatorio += x
print(somatorio)

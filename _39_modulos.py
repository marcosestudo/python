'''
módulos são outros arquivos python abertos no programa principal
'''

# import _017_funcoes # importa todo o módulo

# _017_funcoes.hello_world()


# from _017_funcoes import hello_world # impoprta só a função

# hello_world()


import random
# gerador de número muito louco
# num = list(str(random.random()))
# num.remove('.')
# print(sum(int(x) for x in num))

# print(random.randint(0, 100))
# print(random.uniform(0, 100))


# # gerador de apostas da mega-sena
# aposta = []
# while len(aposta) < 6:
#     num = random.randint(1, 61)
    
#     if num not in aposta:
#         aposta.append(num)

# print(aposta)


# # mesma função usando set
# aposta = set()

# while len(aposta) < 6:
#     aposta.add(random.randint(1, 61)) # set(conjunto) não aceita repetião, não precisa do if

# aposta = list(aposta)
# aposta.sort
# print(aposta)


# # choice() mostra um valor aleatório de um iterável 
# jogadas = 'pedra', 'papel', 'tesoura'

# print(random.choice(jogadas))


# # shuffle() embaralha os dados
# baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(baralho)
# print(random.shuffle(baralho))
# print(baralho)

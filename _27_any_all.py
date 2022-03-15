'''
all() retorna True se todos os elementos do iterável/coleção são True ou se o iterável estiver vazio
any() retorna True se qualquero elemento for True, retorna False se estiver vazio
'''


# print(all([0, 1, 2, 3, 4])) # retorna False por causa do 0

# nomes = 'Carlos', 'Cris', 'Cássio'
# print(all([nome[0] == 'C' for nome in nomes]))

# print(all([num for num in [2, 4, 6, 8] if num % 2 == 0]))
# print(all([num for num in [1, 3, 5, 7] if num % 2 == 0])) # se nenhum for par, gera uma lista vazia
#                                                           # cuidado, o all() retorna Trua em lista vazia


# print(any([0, 1, 2, 3, 4]))

"""tuplas não são dinâmicas, são imutáveis
usa-e em coleções que não devem ser mudadas, ex.: meses, chaves de dicionários
são mais rápidas e masi seguras que listas
operações com tulas devem gerar uma nova tupla
com tuplas não acontece shallow copy
com excessão dos métodos de inserção de elementos, tuplas têm os mesmos das listas
"""
# print(dir(()))

# listas são dinâmicas
# lista = [1, 9, 4, 3, 5, 8, 7, 6, 2, 0]
# print(lista)
# lista.sort()
# print(lista)
# lista.append(53)
# print(lista)

# tupla = (1, 9, 4, 3, 5, 8, 7, 6, 2, 0)
# print(tupla)

# tupla_sem_parenteses = 1, 9, 4, 3, 5, 8, 7, 6, 2, 0
# print(tupla_sem_parenteses)
# print(type(tupla_sem_parenteses))

# tupla_de_um_elemento = (1)
# print(tupla_de_um_elemento)
# print(type(tupla_de_um_elemento)) # um elemento mesmo com parênteses não cria uma tupla

# tupla_elemento_vazio = 1, 
# print(tupla_elemento_vazio)
# print(type(tupla_elemento_vazio)) # mesmo sem parênteses com vírgula é criada uma tupla de um elemento


# tupla_range = tuple(range(10))
# print(tupla_range)


# tupla = 1, 2, 3
# a, b, c = tupla # desempacotameto de tupla
# print(tupla)
# print(a)
# print(b)
# print(c)


# tupla = 1, 9, 4, 3, 5, 8, 7, 6, 2, 0
# print(tupla)
# print(sum(tupla))
# print(max(tupla))
# print(min(tupla))
# print(len(tupla))


# tupla1 = 1, 2, 3
# tupla2 = "a", "b", "c"
# print(tupla1, tupla2)
# print(tupla1 + tupla2)
# print(tupla1, tupla2)


# tupla = 1, 9, 4, 3, 5, 8, 7, 6, 2, 0
# print(1 in tupla)


# tupla = [1, 1, 1, 2, 3, 4, 4]
# print(tupla.count(1)) 

# tupla = tuple("palavra qualquer")
# print(tupla) 

"""conjuntos funcionam como na teoria dos conjuntos na matemática
os conjuntos são chamados de sets
sets não possuem valores duplicados
sets não são indexados,  não se acessa por índice
são representados por {} como os dicionários
mapas (dict) tem chaves e valores,  conjuntos (sets) têm apenas valores
útil, por exemplo, num museu onde se cadastra a cidade dos visitantes, criando um conjunto com uma única ocorrência de 
cada cidade
cria-se uma lista pra saber quantas pessoas foram cadastradas e passa pro conjunto(set) pra tirar as repetições
"""


# print(dir(set))


# conjunto1 = {5, 7, 4, 1, 3, 6, 9, 5, 2, 4, 7, 8, 4, 1, 2, 5, 8, 6, 3, 2, 0, 1, 0, 6, 0, 8, 0}

# conjunto2 = set({5, 7, 4, 1, 3, 6, 9, 5, 2, 4, 7, 8, 4, 1, 2, 5, 8, 6, 3, 2, 0, 1, 0, 6, 0, 8, 0}) # conjunto

# conjunto3 = set([5, 7, 4, 1, 3, 6, 9, 5, 2, 4, 7, 8, 4, 1, 2, 5, 8, 6, 3, 2, 0, 1, 0, 6, 0, 8, 0]) # lista

# conjunto4 = set((5, 7, 4, 1, 3, 6, 9, 5, 2, 4, 7, 8, 4, 1, 2, 5, 8, 6, 3, 2, 0, 1, 0, 6, 0, 8, 0)) # tupla

# conjunto5 = set('uma string repetida, repetida, repetida') # string, os números forma ordenados, as letras ficaram bagunçadas

# dicionario = {}.fromkeys(range(4), 'valor')
# conjunto6 = set(dicionario)
# conjunto7 = set(dicionario.keys())
# conjunto8 = set(dicionario.values())

# print(conjunto1) # os elementos foram ordenados e não tem elemento repetido
# print(conjunto2) 
# print(conjunto3) 
# print(conjunto4) 
# print(conjunto5) 
# print(dicionario)
# print(conjunto6) 
# print(conjunto7) 
# print(conjunto8) 

# conjunto = {1, 2, 3}
# print(conjunto)
# conjunto.add('a') # adiciona elemento
# print(conjunto)

# conjunto.remove(2) # remove elemento
# print(conjunto)
# conjunto.discard(8) # se o .remove não encontrar o elemento, dá key error
# print(conjunto)     # se o .discard não encontrar, ignora


# # com conjuntos acontece shallow copy


# métodos matemáticos com conjuntos (união, interseção)

# conjunto1 = {'A', 'E', 'I', 'B', 'C'}
# conjunto2 = {'B', 'C', 'D', 'A', 'E'}

# uniao = conjunto1.union(conjunto2) # elementos únicos
# print(uniao)
# uniao2 = conjunto1 | conjunto2 # caractere '|' (pipe) == caractere de união de conjuntos (sets) 
# pipe também significa or
# print(uniao2)

# intersecao1 = conjunto1.intersection(conjunto2)
# print(intersecao1)
# intersecao2 = conjunto1 & conjunto2 # & == caractere de interseção de conjnuntos
# print(intersecao2)

# so_no_primeiro = conjunto1.difference(conjunto2)
# print(so_no_primeiro)
# so_no_segundo = conjunto2.difference(conjunto1)
# print(so_no_segundo)


# conjunto_numerico = {0, 1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9}
# print(sum(conjunto_numerico))
# print(max(conjunto_numerico))
# print(min(conjunto_numerico))
# print(len(conjunto_numerico))

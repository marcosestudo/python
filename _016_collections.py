"""módulo collections
collections == high peformance container datatypes
"""


### COUNTER ###
# counter recebe um iterável e retorna um dicionário tendo os elementos como chave e a quantidade de ocorrências como valor

from collections import Counter

# print(type(Counter()))

# lista = [0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 9, 9, 9, 9, 9]
# contador = Counter(lista)

# print(type(contador)) # o tipo não é dict, é collections.Counter
# print(contador)

# print(Counter('uma string qualquer'))

# texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus blandit, felis quis aliquam accumsan, purus sem 
# dictum ligula, sed placerat dolor purus et lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus 
# lobortis elit dui, non scelerisque diam accumsan vitae. Integer eget massa pulvinar, finibus dui quis, mattis ipsum. Aenean 
# at leo leo. Phasellus commodo eros at dui ornare suscipit. Ut eleifend massa ex, eu rhoncus dolor mollis eget. Proin ornare 
# congue est, eu finibus eros."""

# palavras = texto.split()
# print(Counter(palavras), '\n')
# print(Counter(palavras).most_common(3)) # 3 palvras que mais aparecem no texto


### DEFAULTDICT ###

# dicionario = {'a': 1, 'b': 2, 'c': 3}
# dicionario['d'] = 4 
# print(dicionario['e']) # se não encontrar, retorna KeyErro

# criando o dicionário com defaultdict atribuimos um valor default
# quando tentarmos acessar uma chave inexistente, ela será criada com esse valor

# from collections import defaultdict 

# dicionario = defaultdict(lambda: 0)
# print(dicionario)
# dicionario['a'] = 1
# print(dicionario)
# print(dicionario['b']) # acrescentou 0 na chave 'b'e printou, não retornou erro
# print(dicionario)


### ORDEREDDICT ###
# OrderedDict mantém a ordem em que os itens foram inseridos

# dicionario = dict(b = 5 , a = 1 , d = 3 , c = 4 , e = 2)
# for chave, valor in dicionario.items():
#     print(f'{chave}: {valor}')

# print()


# from collections import OrderedDict

# dicionario2 = OrderedDict(b = 5 , a = 1 , d = 3 , c = 4 , e = 2)
# for chave2, valor2 in dicionario2.items():
#     print(f'{chave2}: {valor2}')


### NAMEDTUPLE ###

# from collections import namedtuple

# animal = tuple('cachorro nome idade raca')
# print(animal)
# # animal2 = tuple('cachorro', 'nome idade raca') # a tupla pede 1 arumento, foram dados 2, deu erro
# # print(animal2)

# animal3 = namedtuple('cachorro', 'nome idade raca') 
# print(animal3)
# animal4 = namedtuple('cachorro', ['nome', 'idade', 'raca'])
# print(animal4)
# animal5 = namedtuple('cachorro', 'nome, idade, raca')
# print(animal5) # namedtuple pede dois argumentos, cria um objeto de dado com o nome do primeiro argumento

# cachorro = animal5(nome='asd', idade=2, raca='vira lata')
# print(cachorro) 
# print(type(cachorro))
# # formas de assessar
# print(cachorro[0])
# print(cachorro.nome)


### DEQUE ###
# deque é uma lista de alta perfórmance

from collections import deque

deq = deque("uma string")
print(type(deq))
print(deq)

deq.append('maneira')
print(deq)

deq.appendleft('é')
print(deq)

deq.popleft()
print(deq)

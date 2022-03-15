'''
max() retorna o maior valor 
min() retorna o menor
'''


# print(max([1, 2, 5, 8, 7, 4, 2, 3, 9]))
# print(max(['a','s', 'd', 'e', 'a',' ','f']))
# print(max('asdeaf'))
# print(max({'a': 5, 'b': 3, 'c': 1}))
# print(max({'a': 5, 'b': 3, 'c': 1}.values()))
# print(max(1, 3, 2, 5, 4))

# print(min([1, 2, 5, 8, 7, 4, 2, 3, 9]))
# print(min(['a','s', 'd', 'e', 'a',' ','f']))
# print(min('asdeaf'))
# print(min({'a': 5, 'b': 3, 'c': 1}))
# print(min({'a': 5, 'b': 3, 'c': 1}.values()))
# print(min(1, 3, 2, 5, 4))


# nomes = 'Aria', 'Sansom', 'Andre', 'Dora', 'Tim', 'Olivander'
# print(max(nomes)) # ordem alfabética
# print(min(nomes))
# print(max(nomes, key=lambda nome: len(nome))) # maior
# print(min(nomes, key=lambda nome: len(nome)))


musicas = [
    {'título': 'música 1', 'tocou': 12},
    {'título': 'música 2', 'tocou': 16},
    {'título': 'música 3', 'tocou': 58},
    {'título': 'música 4', 'tocou': 53},
    {'título': 'música 5', 'tocou': 20},
    {'título': 'música 6', 'tocou': 52}
]

mais_tocada = max(musicas, key=lambda musica: musica['tocou'])['título']
print(mais_tocada)
print(min(musicas, key=lambda musica: musica['tocou'])['título']) # menos tocada


# usando for
max = 0
mais_tocada = None
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        mais_tocada = musica['título']

print(mais_tocada)

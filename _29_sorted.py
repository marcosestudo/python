'''
.sort() só funciona em listas
sorted() pode ser usado em qualquer iterável
'''
# lista = [2, 1, 4, 5, 0]
# print(f'original: {lista}')
# print(f'sort: {lista.sort()}') # não retorna nada
# print(f'depois do sort: {lista}') # muda a lista original

# print()

# lista2 = [2, 1, 4, 5, 0]
# print(f'original: {lista2}')
# print(f'sorted: {sorted(lista2)}') # retorna a lista ordenada
# print(f'depois do sorted: {lista2}') # gera uma lista ordenada, não muda a lista original


tupla = 2, 1, 4, 5, 0
generator = (num for num in tupla)
letras = 'd', 'a', 'b', 'e', 'c'
dicionario = {'d': 2, 'a': 1, 'b': 4, 'e': 5, 'c': 0}

# print(f'tupla: {tupla}')
# print(f'generator: {generator}')
# print(f'letras: {letras}')
# print(f'dicionário: {dicionario}')

# print(f'sorted tupla: {sorted(tupla)}') # mesmo ordenando uma tupla, retorna uma lista
# print(f'sorted generator: {sorted(generator)}') # retorna uma lista
# print(f'sorted letras: {sorted(letras)}')
# print(f'sorted dicionário: {sorted(dicionario)}')
# print(f'sorted dicionário.items: {sorted(dicionario.items())}')

# parâmetro extra
# print(f'sorted tupla: {sorted(tupla, reverse=True)}')


# usuarios = [
#     {'username': 'sam', 'tweets': ['uhul', 'twittei']},
#     {'username': 'carla', 'tweets': ['amo']},
#     {'username': 'jeff', 'tweets': []},
#     {'username': 'bob', 'tweets': []},
#     {'username': 'doggo', 'tweets': ['olha só, olha lá', 'ó esses raio de luz']},
#     {'username': 'gal', 'tweets': []}
# ]

# print(sorted(usuarios, key=(lambda usuario: usuario['username'])))
# print(sorted(usuarios, key=(lambda usuario: len(usuario['tweets'])), reverse=True)) # ordenando pelo número de tweets

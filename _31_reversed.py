'''
.reverse() só funciona em listas
reversed() pode ser usado em qualquer iterável
'''

# lista = [0, 1, 2, 3, 4, 5]
# print(f'original: {lista}')
# print(f'reverse: {lista.reverse()}') # não retorna nada
# print(f'depois do reverse: {lista}') # muda a lista original

# print()

# lista2 = [0, 1, 2, 3, 4, 5]
# print(f'original: {lista2}')
# print(f'reversed: {reversed(lista2)}') # retorna um objeto
# print(f'reversed list: {list(reversed(lista2))}')
# print(f'depois do reversed: {lista2}') # gera um objeto, não muda a lista original


tupla = 0, 1, 2, 3, 4, 5
generator = (num for num in tupla)
letras = 'd', 'a', 'b', 'e', 'c'
dicionario = {'d': 2, 'a': 1, 'b': 4, 'e': 5, 'c': 0}

# print(f'tupla: {tupla}')
# print(f'generator: {generator}')
# print(f'letras: {letras}')
# print(f'dicionário: {dicionario}')

# print(f'reversed tupla: {reversed(tupla)}') 
# # print(f'reversed generator: {reversed(generator)}') # erro - generator não é reversível
# print(f'reversed letras: {reversed(letras)}')
# print(f'reversed dicionário: {reversed(dicionario)}')
# print(f'reversed dicionário.items: {reversed(dicionario.items())}')


# # iterando reversed object
# tupla = reversed('asd fg')
# print(tupla)
# for num in tupla:
#     print(num, end='') # end='' pra printar tudo em uma linha, dá pra usar o join ou string slice pra isso 

# print()
# # usando join
# tupla = reversed('asd fg') # reatribuindo porque depois de usada no for acima, o objeto foi esvaziado
# print(f"join: {''.join(list(tupla))}")

# # usando slice
# tupla = 'asd fg'
# print(f'slice: {tupla[ : : -1]}')

# # loop reverso/invertido
# for i in reversed(range(0, 10)): # pode ser feito colocando o passo(terceeiro argumento) == -1
#     print(i)

# for i in range(9, -1, -1):
#     print(i)

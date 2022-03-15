'''
comprehensions cria um iterável a partir de outro iterável
'''


### gerando lista a partir de eoutro iterável
### list comprehension ###

# sinaxe > [dado for dado in interável]

# numeros = [0, 1, 2, 3, 4]
# lista = [num * 10 for num in numeros] # pode processar os arquivos ao mesmo tempo, nesse caso está multiplicando
# print(lista)


# def quadrado(num):
#     return num ** 2

# lista = [quadrado(num) for num in numeros]
# print(lista)


numeros = [0, 1, 2, 3, 4]
dobro = []

for num in numeros:
    dobro.append(num * 2)
print(dobro)

print([num * 2 for num in numeros]) # for acima feita com comperehension


# comprehension com condição / estrutura lógica condicional
# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([num for num in numeros if num % 2 == 0])
# print([num for num in numeros if not num % 2]) # jeito mais bonito de escrever

# print([num if num % 2 == 0 else 'impar' for num in numeros])


### dictionary comprehensions ###
# sintaxe > {chave for chave in dicionário} < retorna as chaves em um dicionário
#           {valor for chave, valor in dicionario.items() < retorna os valores em um docionário   
#           {chave:valor for chave, valor in dicionário.items} retorna as chaves e os valores
# .keys(), .values() e . itens retorna em tuplas
# comprehencion retorna em dicionários e podemos manipular os valores, criar condicões, etc


# dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
# print({valor for chave, valor in dicionario.items()})


# podemos gerar um dicionário com itens de uma lista
# lista = [0, 1, 2, 3, 4, 5]
# dicionario_lista = {lista.index(valor): valor ** 2 for valor in lista} # cria dicionário co os quadrados da lista
# print(dicionario_lista)                                                # também funciona com tuplas e sets(conjutos)

# chaves = '12345'
# valores = 'abcde'
# dicionario = {chaves[i]: valores[i] for i in range(len(valores))}
# print(dicionario)

# numeros = [1, 2, 3, 4, 5]
# print({num: ('par' if not num % 2 else 'impar') for num in numeros}) # if not num % 2 == if num % 2 != 0

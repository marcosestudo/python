"""mapas são conhecidos em python como dicionários
"""
receita = {'jan': 100, 'fev': 120, 'mar': 130, 'abr': 150}

print(receita)
print(receita.keys())
print(receita.values())
print(receita.items())

# print('chaves')
# for chave in receita: # é recomendável usar o .keys() no for de dicionários pra pegar as chaves
#     print(chave)

# print('\nvalores')
# for chave in receita(): # aqui é recomendável usar o .values()
#     print(receita[chave])

# print('\nchave: valor')
# for chave in receita.keys():
#     print(f'{chave}: {receita[chave]}')

# for chave, valor in receita.items(): # desempacotamento de dicionário
#     print(f'chave: {chave}, valor: {valor}')

# print(sum(receita))
# print(max(receita))
# print(min(receita))
# print(len(receita))

# print(sum(receita.values()))
# print(max(receita.values()))
# print(min(receita.values()))
# print(len(receita.values()))

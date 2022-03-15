# em outras linguagens dicionários são chamados de mapas
# é um mapeamento chave / valor
# nas listas o índice é a chave, o elemento é o valor
# nas listas a chave é implícita, nos dicionários a chave é explícita
# dicionários não são indexados, deve-se acessar os valores pelas chaves

# print(type({}))
# print(dir({}))

paises = {'chave': 'valor', 'br': 'Brasil', 'eua': 'Estados Unidos'}
print(paises)
# forma alternativa de criar dicionário
paises2 = dict(chave='valor', br='Brasil', eua='Estados Unidos')
print(paises2)

# paises = {'chave': 'valor', 'br': 'Brasil', 'eua': 'Estados Unidos'}
# print(paises['br']) # acessando dicionário pela chave
# print(paises['ru']) # se não encontrar, dá erro e encerra o programa
# print(paises.get('br')) 
# print(paises.get('ru')) # acessando via get - recomendado - se o elemento não existir, não dá erro, retorna None(tipo sem tipo)
# print(paises.get('ru', 'não existe')) # com dois argumentos, se o get não encontrar, retorna o segundo
# None == False

# russia = paises.get('br') 

# if russia is not None: # utilidade pro None (russia is not None == russia != None)
#     print('existe')
# else:
#     print('não existe')

# if russia: # funciona colocando só a variável
#     print('existe')
# else:
#     print('não existe')

# paises = {'chave': 'valor', 'br': 'Brasil', 'eua': 'Estados Unidos'}
# russia = 'ru'
# print(paises.get('ru', 'não existe'))

# paises = {'chave': 'valor', 'br': 'Brasil', 'eua': 'Estados Unidos'}
# print('br' in paises) # retorna True ou False
# print('brasil' in paises) # só retorna True se necontrar a chave, não faz a busca nos valores

# listas, tuplas, dicionários podem ser usados com chaves


# localidades = {
#     (1, 0): 'casa',
#     (3, 3): 'esritório',
#     (3, 8): 'garagem'
# }

# print(localidades)


# receita = {'jan': 100, 'fev': 120, 'mar': 130}
# print(receita)
# receita['abr'] = 150 # adiciona a chave 'abr' e o 2000.0050 
# print(receita)
# novo_dado = {'mai': 175}
# receita.update(novo_dado) # forma alternativa
# receita.update({'jun': 180})
# print(receita)

# receita['jan'] = 200 # mudando valor no dicionário, se a chave existir, muda, se não existir, cria
# receita.update({'fev': 250})
# print(receita) 


# receita = {'jan': 100, 'fev': 120, 'mar': 130, 'abr': 150}
# print(receita.pop('jan')) # diferente das listas, deve ser dada a chave para remoção
# print(receita)
# del receita['mar'] # o del não retorna nada
# print(receita)


# utilidade dos dicionários
# carrinho de compras - diferernça entre lista e dicionário

# carrinho = []

# produto1 = ['PS4', '1', '2000.00']
# produto2 = ['TV', '1', '1500.00']

# carrinho.append(produto1)
# carrinho.append(produto2)

# print(carrinho) # aqui deveríamos saber o índice dos nome, qunatidade e preço do produto

# # usando dicionário

# carrinho_dict = []

# produto1 = {'nome': 'PS4', 'quantidade': '1', 'preço': '2000.00'}
# produto2 = {'nome': 'TV', 'quantidade': '1', 'preço': '1500.00'}

# carrinho_dict.append(produto1)
# carrinho_dict.append(produto2)

# print(carrinho_dict)


# dicionario1 = dict(a=1, b=2, c=3)
# novo1 = dicionario1.copy()
# novo1['d'] = 4
# print(dicionario1)
# print(novo1) # deep copy

# dicionario2 = dict(a=1, b=2, c=3)
# novo2 = dicionario2
# novo2['d'] = 4
# print(dicionario2)
# print(novo2) # shallow copy


# dicionario_fromkeys = {}.fromkeys('a', '1') # só aceita dois aqrgumentos
# print(dicionario_fromkeys)
# dicionario_fromkeys = {}.fromkeys(['a', 'b', 'c', 'd', 'e'], '1') # o argumento 1 pode ser iterável (lista, range, tupla)
# print(dicionario_fromkeys)
# dicionario_fromkeys = {}.fromkeys(range(5), 'a') 
# print(dicionario_fromkeys)
# dicionario_fromkeys = {}.fromkeys('stringsss', 'stringsss') # não cria cahve repetida, para no 'g' 
# print(dicionario_fromkeys)

# d = {'a': '1', 'b': '2', 'a': '53'} # se tentar criar dicionáro com chave repetida, ele só atribui a última
# print(d)                            # como se tivesse adicionando novo elemento em uma chave já existente

'''
filter() filtar valores de uma coleção 8O óóóóóóóóóóóóóóóóóóóóóóó 
filter recebe uma função e um iterável como o map
'''


import statistics


# valores = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# media_valores = sum(valores) / len(valores)
# print(media_valores)


# valores2 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# media_valores2 = statistics.mean(valores2)
# print(media_valores2)


# acima_da_media = filter(lambda x : x > media_valores2, valores2)
# print(list(acima_da_media))
# print(list(map(lambda x : x > media_valores2, valores2))) # quando True, passa pelo filter()


# # filter é util pra remover dados faltantes/vazios
# dados = ['', 'a', 's', 'd', ' ', '       ', 'f', 'g', '']
# print(list(filter(lambda dado: len(dado) > 0, dados)))
# print(list(filter(lambda dado: bool(dado), dados)))
# print(list(filter(None, dados))) # pra remover vazios, o filter não precisa de função


# exemplo
# filtrar os usuários que estão inativos no Twitter

# usuarios = [
#     {'username': 'sam', 'tweets': ['uhul', 'twittei']},
#     {'username': 'carla', 'tweets': ['amo']},
#     {'username': 'jeff', 'tweets': []},
#     {'username': 'bob', 'tweets': []},
#     {'username': 'doggo', 'tweets': ['olha só, olha lá', 'ó esses raio de luz']},
#     {'username': 'gal', 'tweets': []}
# ]


# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0 ,usuarios))
# print(inativos)
# inativos = list(filter(lambda usuario: usuario['tweets'] == [] ,usuarios))
# print(inativos)
# inativos = list(filter(lambda usuario: not usuario['tweets'] ,usuarios))
# print(inativos)


# combinando filter() e map()
# criar lista com nomes com menos de 5 caracteres
# cria strings escrito 'nome:' + 'nome selecionado'

nomes = ['1', '123456', '123', '12', '123456789', '1234', '12345']
print(list(map(lambda nome: f'nome: {nome}', filter(lambda nome: len(nome) < 5, nomes))))

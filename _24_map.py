'''
map faz o mapeamento de função e valor
não confunda com dicionário que mapeia chave e valor
map retorna um map object com a execução da função para cada elemento do iterável
retorno > map object: função(1), função(2), função(3)...
'''


import math


# def area(r):
#     return math.pi * r ** 2


# raios = [1, 2, 3, 4, 5]


# # calcular as áreas com os raios da lista usando for
# areas = []
# for raio in raios:
#     areas.append(area(raio))


# print(areas) 


# # usando map
# areas_map = map(area, raios)


# print(areas_map)
# print(list(areas_map))


# raios = [1, 2, 3, 4, 5]
# print(list(map(lambda raio: math.pi * raio **2, raios))) # fazendo tudo acima em uma linha usando map e lambda


# lista_de_areas = map(lambda raio: math.pi * raio **2, raios)
# print(list(lista_de_areas))
# print(list(lista_de_areas)) # depois de passar pra lista, o map object é esvasiado, limpando a memória


temp = [('br', 30), ('eua', 22), ('arg', 20)]
temp_far = list(map(lambda temp: (temp[0], (9/5) * temp[1] + 32), temp))
print(temp_far)

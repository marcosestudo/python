'''
### listas aninhadas ###
listas aninhadas são arrays
arrays podem ser unidimensionais(arrays/vetores) ou multidimensionais(matrizes)
em Java, arrays são definidos com tamanho e tipo fixos
'''


# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # mattriz 3x3
# for x in matriz:
#     print(x)

# for x in matriz:
#     for y in x:
#         print(y)

# print([[y for y in x] for x in matriz]) # printando matri usando comprehesion

# matriz_gerada = [[0 for y in range(1, 4)] for x in range(1, 4)] # gerando matriz 3x3 usando comprehension
# print(matriz_gerada)

# # achando o índice de um item
# valor = 2
# for x in matriz:
#     for y in x:
#         if y == valor:
#             print(f'{matriz.index(x)}, {matriz[matriz.index(x)].index(valor)}') # deve ter uma forma melhor de fazer isso

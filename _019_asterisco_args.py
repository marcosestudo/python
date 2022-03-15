"""*args é um parâmetro como otro qualquer iniciado com asterisco
o *args coloca os valores de entrada em uma tupla
"""
# def argumentos(*args):
#     print(args)

# argumentos()
# argumentos(0)
# argumentos(0, 1)
# argumentos(0, 1, 2)


# def soma_tudo(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(soma_tudo())
# print(soma_tudo(1))
# print(soma_tudo(1, 2))
# print(soma_tudo(1, 2, 3))
# numeros = [1, 2, 3]
# print(soma_tudo(*numeros)) # o * antes do nome do parâmetro faz o pyton desempacotá-lo
                             # desempacota mesmo sem estar usando *args
# print(soma_tudo(numeros)) # não pôde somar int e lista, o args passou a lista como um elemento único da tupla 


# def soma_com_sum(outro='outro', *args): # pode ter outros parâmetros além do *args
#     print(outro)
#     return sum(args)

# print('^-teste 1->: ', soma_com_sum())
# print('^-teste 2->: ', soma_com_sum(1))
# print('^-teste 3->: ', soma_com_sum(1, 2))
# print('^-teste 4->: ', soma_com_sum(1, 2, 3))

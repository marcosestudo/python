'''
len() retorna o tamanho de um iterável
abs() retorna o valor absoluto(sem sinal) de um int ou float
sum() retorna o somatório de um iterável
round() arredonda pra n casas decimais, se não colocar o numero de casas, por parão arredonda para
'''


# tupla = 0, 1, 2, 3, 4, 5
# print(len(tupla))
# print(tupla.__len__()) # essas funções com __ são chamaadas da dunder


# print(abs(5))
# print(abs(-5))
# print(abs(-5.0))
# print(abs(5.5))
# # print(abs('a')) # erro


# print(sum([1, 2, 3, 4, 5]))
# print(sum([1, 2, 3, 4, 5], 5))
# print(sum([1, 2, 3, 4, 5], -5))
# # print(sum('a', 'b', 'c')) # pra concatenar strings, use o join() 
# print(sum({'a': 1, 'b': 2,'c': 3,'d': 4,'e': 5}.values())) # não esquece das funções dos dicionários(.keys(), .values, .items())

# print(round(1.3))
# print(round(1.4))
# print(round(1.5))
# print(round(1.6))
# print(round(1.15555))
# print(round(1.15555, 2))
# print(round(1.2, 2))
# print(round(1.122222222222, 2 ))

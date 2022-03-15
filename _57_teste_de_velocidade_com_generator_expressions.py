'''teste de velocidade'''


# # generator function
# def gen_func(num: int = 0):
#     for i in range(num):
#         yield i


# gen1 = gen_func(10)
# print(gen1)
# print(list(gen1))


# # generator expression
# gen2 = (num for num in range(10))
# print(gen2)
# print(list(gen2))


### testando a velocidade com a biblioteca time ###
import time

# momento inicial
gen_inicio = time.time()
# generator expression
print(sum(num for num in range(1000_000_0)))
# tempo final == momento atual menos o momento inicial
gen_tempo = time.time() - gen_inicio


list_inicio = time.time()
print(sum([num for num in range(1000_000_0)])) #com mais um zer deu MemoryError
list_tempo = time.time() - list_inicio


print(f'gen: {gen_tempo}')
print(f'list: {list_tempo}')

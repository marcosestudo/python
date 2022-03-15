'''
generators são iterators
generator function não é um iterator
generator function gera um generator

geradores podem ser criados com expressões geradoras como as comprehensions como visto no arquivo '_28_generators.py'
geradores também podem ser criados com funções geradoras que utuilizam a palavra reservada yeld

diferenças entre function e generator function:
--------------------------------------------------------------------------------
| functions                              | generator functions                 |
--------------------------------------------------------------------------------
| return                                 | yield                               |
--------------------------------------------------------------------------------
| só tem 1 return                        | pode ter vários yield               |
--------------------------------------------------------------------------------
| retorna um valor, quando não retorna   | retorna um generator                |
| nada retorna None, que é um valor      |                                     |
--------------------------------------------------------------------------------

uma função normal termina no return
um função geradora, quando chega no yield, para e aguarda um next() pra continuar
'''


def conta_ate(valor_maximo):
    contador = 0
    while contador <= valor_maximo:
        yield contador
        contador += 1


teste_generator = conta_ate(5)
print(teste_generator)
print(type(teste_generator)) # criou um generator


print(next(teste_generator))
print(next(teste_generator))
print(next(teste_generator))
print(next(teste_generator))
print(next(teste_generator))
print(next(teste_generator))
# print(next(teste_generator)) # erro StopIteration


print(list(teste_generator)) # depois de usado, o objeto é esvaziado


# recriando porque o primeiro está vazio
teste_generator = conta_ate(5)


for num in (teste_generator):
    print(num)

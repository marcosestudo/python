'''
diferenças entre um iterador e um itrável

iterator
    objeto que retorna um dado, um elemento por vez quando a função next() é executada
    itera sobre o iterável

iterable
    objeto que retorna um iterator quando a função iter() é executado 

iterator itera sobre o iterable, iterable retorna um iterator, iterator retorna um dado
'''


# iterables
nome = 'string'
numeros = [0,1,2,3,4,5]

# # print(next(nome)) # não tem a função next() porque não é um iterator


# criando iterators
iterador1 = iter(nome) 
iterador2 = iter(numeros)

print(next(iterador1))
print(next(iterador1))
print(next(iterador1))
print(next(iterador1))
print(next(iterador1))
print(next(iterador1))

print()

for caractere in nome: # esse for cria um iterator como iter() e itera sobre o iterável com o next()
    print(caractere)

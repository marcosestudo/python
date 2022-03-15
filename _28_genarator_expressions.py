'''
gerarators expression são como os list, dictionary e set comprehencions com tuplas
o genarator é mais veloz, se puder escolher qual usar, use o generator
use os outros apenas quando for a única opção
'''
# no exemplo da aula passada foi usada uma list comprehension pra gerar a lista com True ou False pro all()
nomes = 'Carlos', 'Cris', 'Cássio'
print(all([nome[0] == 'C' for nome in nomes]))

print(all(nome[0] == 'C' for nome in nomes)) # tirando os colchetes, estamos usando generator


print([nome[0] == 'C' for nome in nomes]) # list comprehencion

print(nome[0] == 'C' for nome in nomes) # generator - foi criado um generator object

print(list(nome[0] == 'C' for nome in nomes))


generator = (num for num in range(10)) # mesma sintaxe das comprehencions, só que com tuplas
print(generator)


from sys import getsizeof
print(getsizeof((num for num in range(10)))) # generator é mais leve que comprehencions
print(getsizeof([num for num in range(10)]))
print(getsizeof({num for num in range(10)}))
print(getsizeof({num: num * 2 for num in range(10)}))


# generator = (num for num in range(10))

# for num in generator:
#     print(num)

'''
zip() gera um objeto com os elementos dos iteráveis passados
zip de dois elementos fica parecido com o dict.items()
'''
# lista1 = [0, 1, 2, 3, 4]
# lista2 = ['a', 'b', 'c']
# lista3 = '98765'

# zip1 = zip(lista1, lista2)
# zip2 = zip(lista1, lista2, lista3)

# print(zip1)
# print(type(zip1))
# print(list(zip1)) # cria tuplas com os itens agrupados com o len igual ao do menor iterável 
# print(list(zip2))

# zip1 = zip(lista1, lista2)
# print(dict(zip1)) # pode-se usar um zip object pra criar um dicionário

# zip1 = zip(lista1, lista2)
# dicionario = dict(zip1)
# print(dicionario)
# print(dicionario.items())


# dados = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
# print(list(zip(*dados))) # asterisco antes do argumento para dempacotá-lo


# # criar dicionário com nome da aluno e maior nota 

prova1 = [8, 7, 9]
prova2 = [5, 6, 8]
alunos = ['aluno1', 'aluno2', 'aluno3']

print(list(zip(alunos, prova1, prova2)))
maior_nota = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(maior_nota)

# usando map
# O map tá jogando todas as notas de prova1 e prova2 dentro da lambda
maior_nota = dict(zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2))))
print(maior_nota)

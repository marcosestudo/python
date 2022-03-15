"""listas em python == vetores ou matrizes / arrays em outras linguagens
listas em python são dinâmicas e acietam qualquer tipo de dado
arrays em C / JAVA possuem tamanho e tipo de dado fixos
"""


print(dir([]))

lista1 = [1, 9, 7, 8, 3, 6, 2, 0, 4, 5]
lista2 = ["b", "e", "a", "D", "f", " ", "C"] 
lista3 = []
lista4 = list(range(5))
lista5 = list("asd fg".title())
lista6 = [[1, 2], [3, 4], [5, 6]]


# lista1.sort() # ordena a lista
# print(lista1)
# lista2.sort() # também funciona com lista de strings
# print(lista2)


# if 4 in lista6[1]:
#     print("sim")
# else:
#     print("não")


# print(lista1.count(0))  # conta quantos "0" tem na lista


# print(lista6[1][0]) #printa o número 3


# print(lista6)

# lista6.append([52, 53]) # acrescenta elemento no final da lista
# print(lista6)

# lista6.extend([52, 53]) # acrescenta os elementos da lista um a um, extend só aceita iteráveis (lista, string, range, etc) 
# print(lista6)           # extend não aceita elemento único como argumento

# lista6.insert(1, "aqui") #insere no índice dado como prineiro argumento
# print(lista6)

# print(lista1 + lista2) # concatenação de listas


# print(lista6)
# print(lista6[::-1]) # invertendo usando slice de string
# lista6.reverse() #invertendo usando reverse
# print(lista6)


# lista_copia = lista6.copy()
# print(lista_copia)


# print(len(lista6))


# print(lista6)
# print(lista6.pop()) # remove e retorna o último elemento
# print(lista6)
# lista6.pop()

# print(lista6)
# print(lista6.pop(1)) # podemos especificar o índice d elemento a ser removido
# print(lista6)

# print(lista6)
# lista6.clear() # limpa a lista
# print(lista6)


# lista_nova = [1, 2, 3]
# lista_nova *= 3
# print(lista_nova)


# frase = "uma frase qualquer"
# print(frase.split()) # separa nos espaços por padrão, pode inserir um argumento qualquer pra separar
# print(frase)

# frase = frase.split()
# print(frase)
# frase = " ".join(frase) # transfirma lista em string com os elementos separados pelo que está entre as aspas
# print(frase)


# for elemento in lista6:
#     print(elemento)

# indice = 0
# (len(lista6))
# while indice < len(lista6):
#     print(lista6[indice]) 
#     indice += 1

# for i in enumerate(lista2): # pra lembrar de como o enumerate funciona
#     print(i)

# for indice, elemento in enumerate(lista2): # printa o índice do lado do elemento
#     print(indice, elemento)

# print(lista2.index("a")) # diz o índice do elemento "a"
# print(lista2.index("x")) 
# print(lista2.index("a", 3)) # pode-se especificar o índice do  início da busca, útil pra achar itens repetidos
# print(lista2.index("a", 1, 4)) #índices do início e do fim da busca

# produto = " "
# carrinho = []

# while produto != "sair":
#     produto = input("digite o nome do produto ou 'sair'\n")
#     if produto != "sair":
#         carrinho.append(produto)
    
# for produto in carrinho:
#     print(produto)

# print(carrinho)


# print(lista2[ : ]) # string slice
# print(lista2[ : :2])
# print(lista2[ : :-1])
# lista2.reverse()
# print(lista2)

# lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(lista_numeros)) # soma todos os elementos
# print(max(lista_numeros))
# print(min(lista_numeros)) # funciona com strings
# print(len(lista_numeros)) # funciona com strings

# print(lista6)
# tupla = tuple(lista6)
# print(tupla)


# a, b, c = lista6 # desempacotamento de lista, deve-se atribuir um número de variáveis igual ao de elemenos da lista
# print(a)
# print(b)
# print(c)


# lista = [1, 1, 1, 2, 3, 4, 4]
# print(lista.count(1)) 


# shallow copy e deep copy
# .copy() cria a nova lista em novo espaço na memória

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# lista_copia = lista.copy() # copiou uma lista em outra lista independente == deep copy
# lista_copia.append(53)
# print(lista_copia)
# print(lista)

# lista_copia = lista # as duas listas respondem como se fossem uma == shallow copy
# lista.append(52)    # shallow copy não acontece com tuplas  
# lista_copia.append(53)
# print(lista_copia)
# print(lista)

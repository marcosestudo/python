"""o **kargs coloca os parâmetros em um dicionário"""


# lembrando como criar dicionários

# dicionario1 = {'a':1, 'b':2, 'c':3}
# dicionario2 = dict(a=1, b=2, c=3)

# print(dicionario1)
# print(dicionario2)


# def kwargumentos(**kwargs):
#     print(kwargs)

# kwargumentos(a=1, b=2, c=3) # funciona como o dict(), cria um dicionário chamado kwargs pra usar internamente na função
# kwargumentos('a':1, 'b':2, 'c':3)


### ordem dos argumentos ###
# 1 parâmetros obrigatórios
# 2 *args
# 3 parâmetros opcionais
# 4 **kwargs

# def funcao(arg1, arg2, *args, arg4=None, **kwargs):
#     print(f'{arg1}\n{arg2}\n{args}\n{arg4}\n{kwargs}')

# funcao('a', 'b', 1, 2, 3, arg4=True, a=1, b=2, c=3)


# # desempacotando dicionário com **
# # desempacota mesmo sem estar usando o **kwargs
# # lembre: um asterisco desempaconta listas, tuplas e conjuntos, que têm valor - asterisco == valor
# #         dois asteriscos desempacotam dicionários, qeu têm chave e valor - asterisco1 == chave, asterisco2 == valor
# #         os nomes das chaves do dicionário devem ser os mesmos dos parâmetros como se tivéssemos dando parâmetros nomeados
# def desempacotador(**kwargs):
#     print(f"desempacotado: {kwargs['chave1']}, {kwargs['chave2']}")

# pacote = {'chave1': 'valor1', 'chave2': 'valor2'}

# desempacotador(**pacote)
# desempacotador(pacote) # recebendo o dicioário, dá erro

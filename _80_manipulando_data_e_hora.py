'''
Python tem um módulo built-in (integrado) para trabalhar com data e hora - datetime
'''


import datetime


# print(dir(datetime))


# # anos máximo e mínimo que o datetime() suporta
# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)


# # data e hora atuais
# # por que está escrito datetime duas vezes em datetime.datetime.now()?
# # o primeiro é o nome do módulo, o segundo é o nome da classe - módulo.classe.método()
# print(datetime.datetime.now())
# print(type(datetime.datetime.now()))

# # retorna (year, month, day, hour, minute, second, microsecond)
# print(repr(datetime.datetime.now()))


# # marcando o temp de execução do loop
# inicio = datetime.datetime.now()
# for i in range(1000):
#     # print(i)
#     if i % 100 == 0:
#         print(i)
# tempo = datetime.datetime.now() - inicio
# print(tempo)


# # fazendo ajustes na hora usando replace()
# # replace é um método da classe string, com funcionamento diferente (sobrescrito?) na classe datetime
# # pode ser útil, por exemplo, no caso de precisar executar algo x minutos depois de acessado
# inicio = datetime.datetime.now()
# print(inicio)

# inicio = inicio.replace(year=1, month=1, day=1, hour=1, minute=1, second=1, microsecond=12)
# print(inicio)


# # criando data e hora
# evento = datetime.datetime(2022, 2, 13, 13,) # dia 13 de fevereiro de 2022, 13 horas
#                                              # como não foram passados os minutos e segundos, eles recebem zero
# print(evento)
# print(type(evento))
# print(type('13/02/2022')) # como transformar uma data passada em uma string para um objeto datetime?

# # transformando string em objeto datetime
# data = '13/02/2022' # data no formato (dd/mm/yyyy)
# data = data.split('/')
# data = datetime.datetime(int(data[2]), int(data[1]), int(data[0])) # ordem pra deixar no formato (yyyy/mm/dd)
# print(data)


# # acessando elementos da data
# data = datetime.datetime.now()
# print(dir(data))
# print(data)
# print(data.microsecond)

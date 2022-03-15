

import datetime


# # O now() e o today() retornam a mesma coisa
# # No now() podemos especificar um timezone (fuzo horário) com parâmetro, no today(), não
# agora = datetime.datetime.now()
# print(agora)
# print(type(agora))
# print(repr(agora))


# hoje = datetime.datetime.today()
# print(hoje)
# print(type(hoje))
# print(repr(hoje))


# # Mudanças ocorrendo à meia noite com combine()
# # O datetime.time() sem argumentos retorna hora, minuto e segundo iguais a zero
# # O combine vai combinar a soma do dia de hoje do now() + 1 dia do timedelta() com o time()
# # Retornará a data do dia seguinte com o horário 00:00:00 (meia noite)
# manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
# print(manutencao)
# print(type(manutencao))
# print(repr(manutencao))


# # Dia da semana
# # 0 - segunda; 1 - terça; 2 - quarta; 3 - quinta; 4 - sexta; 5 - sábado; 6 - domingo
# print(datetime.datetime.now().weekday())

# nascimento = '29/04/1993' # nascimento no formato (dd/mm/yyyy)
# nascimento = nascimento.split('/')
# nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0])) # ordem pra deixar no formato (yyyy/mm/dd)
# print(nascimento.weekday()) # dá pra criar um monte de if e elif pra dizer em qual dia da semanna nasceu de acordo co a linha 30


# # formatando data e hora com o strftime() - string format time
# # o nosso formato é o (dd/mm/yyyy), o padrão do Python é o formato americano (yyyy/mm/dd)
# data = datetime.datetime.now()
# print(data)

# data_formatada = data.strftime('%d/%m/%Y, %H:%M:%S') # "Y" maiúsculo retorna o ano com 4 dígitos, minúsculo retorna com 2
# print(data_formatada)



# from textblob import TextBlob


# # traduzindo data com textblob
# data = datetime.datetime.now()
# data_formatada_ingles = data.strftime('%d/%B/%Y')


# # O textBlob usa a internete para traduzir, devemos estar conectados
# # Para traduzir desconectado, podemos criar uma sequência de if e elifs pros meses
# def formata_data(data):
#     return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

# print(formata_data(data))


# # Passando data de uma string para um objeto datetime
# nascimento = datetime.datetime.strptime('29/04/1993', '%d/%m/%Y')
# print(nascimento)


# # Somente a hora
# hora = datetime.datetime.now().time()
# print(hora)

# almoco = datetime.time(12, 30, 0)
# print(almoco)


# # Marcando o tempo de execução do código com timeit
import timeit

# # o join está juntando os números separados por um traço
# # execute no terminalpra ver >>> '-'.join(str(n) for n in range(100))
# # timeit recebe dois parâmetros
# # uma expressão que será executada em uma string e a quantidade de vezes que será executada

# # testando com generator
# tempo = timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000) 
# print(tempo) # 0.0005292000132612884

# # testando com list compehention
# tempo = timeit.timeit("'-'.join([str(n) for n in range(100)])", number=10000) 
# print(tempo)

# # testando com map
# tempo = timeit.timeit("'-'.join(map(str, range(100)))", number=10000) 
# print(tempo)

# # somando os dígitos do tempo igual a um doido
# a = 0
# for n in list('9299810000811704'):
#     a += int(n)
# print(a)


import timeit, functools

def teste(n):
    soma = 0
    for num in range(n):
        soma = soma + num ** num
    return soma 


# # functools.partial() recebe a função que queremos executar e os parâmetro a ser colocado nela num *args
# # é útil para testarmos funções no timeit que só pode receber uma expressão como argumento
# # timeit recebe dois parâmetros
# # uma expressão que será executada em uma string e a quantidade de vezes que será executada
print(timeit.timeit(functools.partial(teste, 12), number=10000))

'''
Delta é a difereça entre dois objetos datetime (data final e a inicial)
delta == data_final - data_inicial
'''


import datetime 

# # timedelta
data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2025, 4, 29)

tempo_pro_evento = aniversario - data_hoje # não funciona com soma, dá TypeError
                                           # soma deve ser feita como na forma abaixo, na linha 19, somando o timedelta
print(repr(tempo_pro_evento)) # o retorno da subtração das datas ofi um datetime.timedelta
print(tempo_pro_evento)


# # acrescentando dias na data inicial
data_da_compra = datetime.datetime.now()
print(data_da_compra)

# 3 dias de diferença entre o dia da compra e do vencimento do boleto
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento = data_da_compra + regra_boleto
print(vencimento)

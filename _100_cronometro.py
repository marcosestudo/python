"""Tentando criar um cronômetro de brincadeira"""


import time


def cronometro(segundos):
    x = segundos
    contador = 0
    while x > 0:
        y = time.time()
        # o loop será executado por um segundo, ou seja, até time.time() - y chegar a 1 
        while time.time() - y < 1:
            pass
        contador += 1
        print(contador)
        x -= 1


def contagem_regressiva(segundos):
    x = segundos
    contador = 0
    while x >= 0:
        y = time.time()
        # o loop será executado por um segundo, ou seja, até time.time() - y chegar a 1 
        while time.time() - y < 1:
            pass
        print(x)
        x -= 1


cronometro(3)

contagem_regressiva(3)

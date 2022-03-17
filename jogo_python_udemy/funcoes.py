from random import randint
from jogador import Jogador


def vida(vida: int, vida_max: int, vida_perdida: int) -> str:
    """retorna a barra de vida para ser printada"""
    return f"]{'|' * (vida)}{int(vida / vida_max * 100)}%{'-' * vida_perdida}["


def dificuldade(dif: int, jogador: Jogador) -> list:
    """Retorna o valores mínimos e máximos e as operações possiveis de acordo com o nível de dificuldade"""
    if dif == '1':
        jogador.vida = vida_max = 20
        min = -10
        max = 10
        mult = div = False

    elif dif == '2':
        jogador.vida = vida_max = 16
        min = -100
        max = 100
        mult = div = True

    elif dif == '3':
        jogador.vida = vida_max = 12
        min = -100
        max = 100
        mult = div = True

    return min, max, mult, div, vida_max


def operacao(min: int, max: int, mult: bool, div: bool, operacao: int = randint(1, 4)) -> int:
    """retorna uma operação de acordo com a dificuldade"""
    a, b = randint(min, max), randint(min, max) 

    if operacao == 1:
        print(f'{a} + {b} = ', end='')
        return a + b

    elif operacao == 2:
        # abs pra não ter dois sinais de menos como "a - -b", por exemplo
        print(f'{a} - {abs(b)} = ', end='')
        return a - abs(b)

    elif operacao == 3 and mult:
        print(f'{a} * {b} = ', end='')
        return a * b

    if operacao == 4 and div:
        while a < b or b == 0:
            a = b = randint(1, 9)
        print(f'{a * (multiplicador := randint(5, 10))} / {b} = ', end='')
        return a * multiplicador // b

from random import randint, random
from tkinter.tix import Tree
from jogador import Jogador


# não esquecer de trocar essa função po ruma lambda
def vida(vida: int, vida_max: int, vida_perdida: int) -> str:
    """retorna a barra de vida para ser printada"""
    return f"]{'|' * (vida)}{int(vida / vida_max * 100)}%{'-' * vida_perdida}["


def dificuldade(dif: int, jogador: Jogador):
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
        jogador.vida = vida_max = 10
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

dificuldade_escolhida = None

j = Jogador()
vida_perdida = 0

while dificuldade_escolhida not in ('1', '2', '3'):
    dificuldade_escolhida = input('''
    Escolha a dificuldade: digite 1, 2 ou 3
                           1 para fácil
                           2 para média
                           3 para difícil
                           ''')
dif = dificuldade(dificuldade_escolhida, j)


while True:
    print()
    gabarito = operacao(dif[0], dif[1], dif[2], dif[3], randint(1, 4))
    # no nível fácil não tem operacões de multiplicação e divisão, se cair uma delas rotrnara None e operacao() será reexecutada
    while gabarito == None:
        gabarito = operacao(dif[0], dif[1], dif[2], dif[3], randint(1, 4))
    resposta = input()
    # checagem = (x for x in range(-1000000, 1000000))
    while resposta not in (str(x) for x in range(-100000, 100000)):
        resposta = input('insira um número inteiro\n')
    
    if int(resposta) == gabarito:
        print('Correto')
        j.pontuacao += 1        
    else:
        print('Errado')
        vida_perdida += 4
        j.vida -= 4
    
    print(f'\nPontuacao: {j.pontuacao}\nVida: {vida(j.vida, dif[4], vida_perdida)}\n')

    if j.vida <= 0 or input('Continuar: s / n\n') == 'n':
        print(f'\nSua pontuação é: {j.pontuacao}\n')
        break

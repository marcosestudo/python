from random import randint, random
from tkinter.tix import Tree
from jogador import Jogador


# não esquecer de trocar essa função po ruma lambda
def vida(vida: int, vida_max: int, vida_perdida: int) -> str:
    """retorna a barra de vida para ser printada"""
    return f"Vida: ]{'|' * (vida)}{int(vida / vida_max * 100)}%{'-' * vida_perdida}["


def dificuldade(dif):
    """Retorna o valores mínimos e máximos e as operações possiveis de acordo com o nível de dificuldade"""
    if dif == 1:
        min = -10
        max = 10
        mult = div = False

    elif dif == 2:
        min = -100
        max = 100
        mult = div = True

    elif dif == 3:
        min = -100
        max = 100
        mult = div = True

    return min, max, mult, div


def operacao(min: int, max: int, mult: bool, div: bool, operacao: int = randint(1, 4)) -> int:
    a, b = randint(min, max), randint(min, max) 

    if operacao == 1:
        print(f'{a} + {b} = ', end='')
        return a + b

    elif operacao == 2:
        # abs pra não ter dois sinais de menos como "a - -b", por exemplo
        print(f'{a} - {abs(b)} = ', end='')
        return a - abs(b)

    elif operacao == 3:
        print(f'{a} * {b} = ', end='')
        return a * b

    if operacao == 4:
        while a < b or b == 0:
            a = b = randint(1, 9)
        print(f'{a * (multiplicador := randint(5, 10))} / {b} = ', end='')
        return a * multiplicador // b


dif = dificuldade(1)
for i in range(10):
    print(operacao(dif[0], dif[1], dif[2], dif[3]))


# dificuldade = None


# while dificuldade not in ('1', '2', '3'):
#     dificuldade = input('''Escolha a dificuldade: digite 1, 2 ou 3
#                        1 para fácil
#                        2 para média
#                        3 para difícil
#                        ''')


# if dificuldade == '1':
#     j = Jogador(vida_max := 20) 

# elif dificuldade == '2':
#     j = Jogador(vida_max := 16) 

# else:
#     j = Jogador(vida_max := 12) 

# vida_perdida = 0

# operacao = None


# if dificuldade == '1':
#     while True:
#         # cehcagem testa se o input é um um número entre 0 e 1_000_000
#         checagem = (str(x) for x in range(1000000))

#         if random.choice([1, 2, 3]) == 1 or 2 or 3:
#             a, b = randint(0, 9), randint(0, 9)
#             resposta = input(f'\n{a} + {b} = ')
            
#             while resposta not in checagem:
#                 checagem = (str(x) for x in range(1000000))
#                 resposta = input('Insira um número inteiro\n')

#             if int(resposta) == a + b:
#                 print('\ncorreto\n')
#                 j.pontuacao += 1
#             else:
#                 print('\nerrado\n')
#                 vida_perdida += 4
#                 j.vida -= 4

#         print(vida(j.vida, vida_max, vida_perdida))
#         print(f'Pontuacao: {j.pontuacao}\n')

#         if j.vida == 0 or input('Continuar? s / n\n' ) == 'n':
#             print(f'\nSua pontuação é: {j.pontuacao}')
#             break


# if dificuldade == '2':
#     while True:
#         # cehcagem testa se o input é um um número entre 0 e 1_000_000
#         checagem = (str(x) for x in range(1000000))
#         if random.choice([1, 2, 3]) == 1 or 2 or 3:
#             a, b = randint(0, 99), randint(0, 99)
#             resposta = input(f'\n{a} + {b} = ')
            
#             while resposta not in checagem:
#                 checagem = (str(x) for x in range(1000000))
#                 resposta = input('Insira um número inteiro\n')

#             if int(resposta) == a + b:
#                 print('\ncorreto\n')
#                 j.pontuacao += 1
#             else:
#                 print('\nerrado\n')
#                 vida_perdida += 4
#                 j.vida -= 4

#         print(vida(j.vida, vida_max, vida_perdida))
#         print(f'Pontuacao: {j.pontuacao}\n')

#         if j.vida == 0 or input('Continuar? s / n\n' ) == 'n':
#             print(f'\nSua pontuação é: {j.pontuacao}')
#             break


# if dificuldade == '3':
#     while True:
#         # cehcagem testa se o input é um um número entre 0 e 1_000_000
#         checagem = (str(x) for x in range(1000000))
#         if random.choice([1, 2, 3]) == 1 or 2 or 3:
#             a, b = randint(0, 999), randint(0, 999)
#             resposta = input(f'\n{a} + {b} = ')
            
#             while resposta not in checagem:
#                 checagem = (str(x) for x in range(1000000))
#                 resposta = input('Insira um número inteiro\n')

#             if int(resposta) == a + b:
#                 print('\ncorreto\n')
#                 j.pontuacao += 1
#             else:
#                 print('\nerrado\n')
#                 vida_perdida += 4
#                 j.vida -= 4

#         print(vida(j.vida, vida_max, vida_perdida))
#         print(f'Pontuacao: {j.pontuacao}\n')

#         if j.vida == 0 or input('Continuar? s / n\n' ) == 'n':
#             print(f'\nSua pontuação é: {j.pontuacao}')
#             break

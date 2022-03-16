from random import randint, random
from jogador import Jogador

# não esquecer de trocar essa função po ruma lambda
def vida(vida: int, vida_max: int, vida_perdida: int) -> str:
    """retorna a barra de vida para ser printada"""
    return f"Vida: ]{'|' * (vida)}{int(vida / vida_max * 100)}%{'-' * vida_perdida}["


def operacao(a: int, b: int, operacao: int = randint(1, 4)) -> int:
    if operacao == 1:
        print(f'{a} + {b} = ', end='')
        return a + b
    elif operacao == 2:
        print(f'{a} - {b} = ', end='')
        return a - b
    elif operacao == 3:
        print(f'{a} * {b} = ', end='')
        return a * b
    if operacao == 4:
        while a < b or b == 0:
            a = b = randint(1, 9)
        print(f'{a * (multiplicador := randint(5, 10))} / {b} = ', end='')
        return a * multiplicador // b
            

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

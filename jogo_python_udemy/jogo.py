from random import randint
from jogador import Jogador
from rank import atualizar_rank
from funcoes import vida, dificuldade, operacao


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

    gabarito = operacao(dif['min'], dif['max'], dif['mult'], dif['div'], randint(1, 4))

    # no nível fácil não tem operacões de multiplicação e divisão, se cair uma delas rotrnara None e operacao() será reexecutada
    while gabarito == None:
        gabarito = operacao(dif['min'], dif['max'], dif['mult'], dif['div'], randint(1, 4))
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

    print(f"\nPontuacao: {j.pontuacao}\nVida: {vida(j.vida, dif['vida_max'], vida_perdida)}\n")


    if j.vida <= 0 or input('Continuar: s / n\n') == 'n':
        print(f'\nSua pontuação é: {j.pontuacao}\n')
        break


atualizar_rank(j.pontuacao, input('Insira o teu nome: '))

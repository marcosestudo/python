import random


pontuacao = 0


dificuldade = input('''Escolha a dificuldade: digite 1, 2 ou 3
                       1 para fácil
                       2 para média
                       3 para difícil
                       ''')


if dificuldade == '1':
    vida, vida_perdida = 20, 0
    
    while True:
        # cehcagem testa se o input é um um número entre 0 e 1_000_000
        checagem = (str(x) for x in range(1000000))
        if random.choice([1, 2, 3]) == 1 or 2 or 3:
            a, b = random.randint(0, 9), random.randint(0, 9)
            resposta = input(f'{a} + {b} = ')
            
            while resposta not in checagem:
                checagem = (str(x) for x in range(1000000))
                resposta = input('Insira um número inteiro')
            

            if int(resposta) == a + b:
                print('\ncorreto\npontuação++\n')
                pontuacao += 1
            else:
                print('\nerrado\nvida--\n')
                vida_perdida += 4
                vida -= 4

        print(f"Vida ]{'|' * (vida)}{int(vida / 20 * 100)}%{' ' * vida_perdida}[")
        print(f'Pontuacao {pontuacao}\n')

        if vida == 0:
            break

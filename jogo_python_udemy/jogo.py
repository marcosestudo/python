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
        if random.choice([1, 2, 3]) == 1 or 2 or 3:
            a, b = random.randint(0, 9), random.randint(0, 9)
            
            if resposta := int(input(f'{a} + {b} = ')) == a + b:
                pontuacao += 1
            else:
                vida_perdida += 4
                vida -= 4

        print(f"Vida ]{'|' * (20 - vida_perdida)}{' ' * vida_perdida}[")
        print(f'Pontuacao {pontuacao}')

        if vida == 0:
            break

import random


pontuacao = 0


dificuldade = input('''Escolha a dificuldade: digite 1, 2 ou 3
                       1 para fácil
                       2 para média
                       3 para difícil
                       ''')



if dificuldade == '1':
    vida_perdida = 0    
    print(vida := f"vida ]{'|' * (20 - vida_perdida)}{' ' * vida_perdida}[")
    print(pontuacao)    

    if random.choice([1, 2, 3]) == 1 or 2 or 3:
        print(pergunta := random.randint(0, 9) + random.randint(0, 9))
        if resposta:= input(('Resposta: ')) == pergunta:
            pontuacao += 1
        else:
            vida_perdida += 4

    print(vida)
    print(f'Pontuação: {pontuacao}')

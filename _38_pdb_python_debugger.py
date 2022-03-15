'''
é mais prático usar o debugger do vscode
pra usar o python debugger deve-se importar a biblioteca pdb e usa a função set_trace()
no python atual não precisa importar nada, pode-se usar a função built-in(integrada) breakpoint()
comandos básicos do pdb
l (lista onde estamos no código)
n (próxima linha)
p (printa variável)
c (continuar execução)
'''

import pdb


def divide(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err: # podemos passar uma tupla com város erros
        return f'ocorreu um erro {err}'

print(divide(1, 'a'))

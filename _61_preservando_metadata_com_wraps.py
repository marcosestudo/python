'''
Metadados são os dados sobre outrso dados
Ex.: uma imegem tem nome, tamanho, dimensões... esses são os metadados da imagem

Wraps são funções que envlolvem elementos com diversas finalidades
'''


# # name e doc são metadados da função
# def teste():
#     '''documentação da função'''
#     pass

# print(teste.__name__)
# print(teste.__doc__)



def ver_log(funcao):
    def logar(*args, **kwargs):
        '''Sou uma função (logar) dentro de outra'''
        print(f'você está chamando a função: {funcao.__name__}')
        print(f'Documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a: int=0, b: int=0):
    '''Soma dois números'''
    return a + b


print(soma(10, 2))


### Problema ### 
# Quando pedimos os metadados da função decorada, recebemos os da função que está dentro da decoradora
print('\nV Problema V')
print(soma.__name__)
print(soma.__doc__)


### Solução ###
# a solução está na função wraps da biblioteca functools
# é só colocar o wraps dentro da decorator
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        '''Sou uma função (logar) dentro de outra'''
        print(f'você está chamando a função: {funcao.__name__}')
        print(f'Documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


print('-----------------------------------------------------')
@ver_log
def soma(a: int=0, b: int=0):
    '''Soma dois números'''
    return a + b


print(soma())


# Resolvido
print('\nV Reosolvido V')
print(soma.__name__)
print(soma.__doc__)

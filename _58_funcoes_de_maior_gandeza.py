'''
HOF
higher order functions

qunado um alinguegm de programação suporta HOF, podemos ter funções que retornam outras funções, 
passar funções como argumentos para outras ou criar variáveis do tipo de funções

first class citizen
em python, funções são cidadões de primeira class


'''


# def somar(a, b):
#     return a + b


# def subtrair(a, b):
#     return a - b


# def multiplicar(a, b):
#     return a * b


# def dividir(a, b):
#     return a / b


# def calcular(num1, num2, funcao):
#     return funcao(num1, num2)


# print(calcular(1, 2, somar))
# print(calcular(1, 2, subtrair))
# print(calcular(1, 2, multiplicar))
# print(calcular(1, 2, dividir))


### nested functions ###
# funções dentro de funções, conhecidas como nested functions ou inner functions


from random import choice


# def cumprimento(pessoa):
#     def humor():
#         return choice(('E aí ', 'Colé ', 'Olar '))
#     return humor() + pessoa

# print(cumprimento('Cornolio'))


# def faz_me_rir():
#     def rir():
#         return choice(('lol', 'haha', 'rs'))
#     return rir()

# print(faz_me_rir())


# # inner / nested functions podem acessar o escopo de funções mais esternas
def faz_me_rir2(pessoa):
    escolha = choice(('lol', 'haha', 'rs'))
    def rir():
        return f'{escolha}, {pessoa}'
    return rir()

print(faz_me_rir2('Cornnolio'))

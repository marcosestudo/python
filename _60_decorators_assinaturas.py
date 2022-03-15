'''
decorators com diferentes assinaturas / diferenets parâmetros

a assinatura de uma função é representada por seu retorno, nome e parâmetros de entrada
decorators com diferentes assinaturas significa que podemos passar funções co diferentes números de parâmetros de entrada
usando *args e **kwargs
'''


# def gritar(funcao):
#     print('executou 1')
#     def aumentar(nome):
#         return funcao(nome).upper()
#     return aumentar


# @gritar
# def saudacao(nome):
#     print('executou 2')
#     return f'Ia am {nome}'


# @gritar
# def ordenar(pedido, acompanhamento):
#     print('executou 3')
#     return f'um {pedido} com {acompanhamento}'
 

# print(saudacao('Cornolio'))


# print(ordenar('pau', 'bolas')) # a função aumentar peded um argumento, dois foram dados
#                                # para resolver, usamos um padrão de projeto chamado decorator pattern 
#                                # refatorando o código com *args e **kwargs
# # o código acima foi mantido para estudo, ele será refatorado abaixo


### refatorando com decorator pattern ###

def gritar(funcao):
    # print('executo 1')
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    # print('executou 2')
    return f'Ia am {nome}'


@gritar
def ordenar(pedido: str = 'pau', acompanhamento: str = 'bolas'):
    # print('executou 3')
    return f'adoraria um {pedido} com {acompanhamento}'
 

@gritar
def lol():
    return 'lol'


print(saudacao('Cornolio'))
print(ordenar())
print(lol())


### decorators com argumentos ###

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            print(f'args: {args}')
            if args and args[0] != valor:
                return f'valor incorreto! Primeiro argumento deve ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1: int=10, num2: int=0):
    return num1 + num2


# print(soma_dez())


def a(funcao):    
    print('passou no A')
    print(funcao())
    def aa(*args, **kwargs):
        print(funcao())
        return 'AA'
    return aa

@a
def b():
    print('passou no B')
    return 'B'

print(b())

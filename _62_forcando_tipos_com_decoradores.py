'''
Em outras linguagens o tipo da variável deve ser declarado na sua criação
No pyton podemos atribuir qualquer tipo à qualquer variável
Para evitar problemas no programa, podemos forçar o tipo de entrada usando uma decorator function
'''


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


# @forca_tipo(str, int) # o decorator está convertendo a variável "msg" para "str", e a "vezes" para "int"
# def repete_mensagem(msg, vezes):
#     for _ in range(vezes): # um cast aqui(range(int(vezes))) faria o mesmo que a função
#         print(msg)


# repete_mensagem(12, '3')


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir('10', '2')

'''
Classes são os modelos dos objetos do mundo real que serão representados computacionalmente

Para criar um controlador para as lâmpadas de uma loja
como não existe o tipo lampada, criaríamos a classe "lampada" para representá-las

Nomes de classes em Python são escritos em CamelCase
Classes internas do Python estão escritas com letra minúscula para diferenciarmos as dele das nossas

Em Java uma classe deve ficar em um arquivo com o mesmo nome dela

Classe também são chamadas de entidade < a confirmar
'''


# revendo os tipos
a, b, c = 1, 1.0, 'Cornolio' 
print(f'{type(a)}\n{type(b)}\n{type(c)}')


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))

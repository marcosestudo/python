"""Uma docstring é uma string literal presente na primeira linha da definição de um módulo, classe ou função"""

from random import random

def cara_ou_coroa():
    """retorna a string "cara" ou a string "coroa""" # <- isso é uma docstring
    if random() < 0.5:
        print('cara')
    else:
        print('coroa')
    
print(cara_ou_coroa.__doc__) # __doc__ mostra a docstring
print('^ doc ^   v help v')
print(help(cara_ou_coroa))

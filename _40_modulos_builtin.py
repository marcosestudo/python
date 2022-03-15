'''
móduos builtin (integrados) são os módulos que ja vêm no python como o random, por exemplo
não precisam ser baixados de fora
'''

# podemos criar um alias(apelido) pro módulo ao importar

# import random as random_alias
# from random import random as random_funcao_alias # també podemos apelidar funções

# random_alias.random()
# # random.random() # criado o alias, não dá pra usar o nome original


from random import random
random()

from random import * # importa todas as funções, sendo desnecessário digitar o nome do módulo para usá-las
random()

import random # assim precisamos usar o nome do módulo antes do nome da função
random.random()


# podemos importar mais de uma função na mesma linha
from random import random, randint

# caso tenha muitas funções, utilizamos uma tupla para facilitar a leitura
from random import (
    random, 
    randint, 
    uniform, 
    shuffle, 
    choice
)

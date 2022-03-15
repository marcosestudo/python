'''
JSON - JavaScript Object Notation

json são muito utilizados sem api's de empresas como twitter google, etc.
As informações no arqivos json são ou se parecem com dicionários
API - Application Programming Interface (buscar sobre api no goolge)
apis' são uma forma de comunicação entre a aplcação e os desenvolvedores
'''


# import json


# retorno = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '110v', 2500)}])

# print(type(retorno))
# # dumps() retorna uma  string
# # Note que foi formatada, as áspas simples foram trocadas por duplas porque o json não trabalha com áspas simples
# # O dumps deixa a string preparada pro formato json
# print(retorno)
# print(retorno[0], retorno[1], retorno[2])


# import json


# class Gato:
#     def __init__(self, nome, raca):
#         self.__nome = nome
#         self.__raca = raca

#     @property
#     def nome(self):
#         return self.__nome

#     @nome.setter
#     def nome(self, nome):
#         self.__nome = nome

#     @property
#     def raca(self):
#         return self.__raca

#     @raca.setter
#     def raca(self, raca):
#         self.__raca = raca


# gato1 = Gato('Conrolio', 'Vira lata')

# print(gato1.__dict__)
# # O json.dumps() form tou o __dict__ com áspas duplas para o formato json
# retorno = json.dumps(gato1.__dict__)
# print(retorno)


'''
Integrando json com pickle
pip install jsonpiclke
'''

import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca


gato1 = Gato('Conrolio', 'Vira lata')

# jsonpickle.encode() retorna um dicionário em string
# O primeiro elemento do dicionário tem como chave "py/object" 
# indicando que esse é um objeto python pra hora de retorná-lo ao original
# retorno = jsonpickle.encode(gato1)

# print(type(retorno))
# print(retorno)


'''Escrevendo um arqivo jsonpickle'''

gato_json = Gato('Conrolio', 'Vira lata')

with open('gato_json.json', 'w') as arquivo:
    retorno = jsonpickle.encode(gato_json)
    arquivo.write(retorno)

print(type(retorno))


'''Lendo um arquivo json'''

with open('gato_json.json', 'r') as arquivo:
    conteudo = arquivo.read()
    retorno = jsonpickle.decode(conteudo)

print(retorno)
print(type(retorno))
print(retorno.__dict__)

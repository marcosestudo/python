'''
O método super() se refere à super classe
'''


class Animal:
    
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca


gato1 = Gato('Cornolio', 'Felino', 'Vira lata')
gato1.faz_som('miau')

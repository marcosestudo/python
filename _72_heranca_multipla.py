'''
Em Java, uma classe só pode herdar de uma classe
Em python, uma classe pode herdar diretamente de várias
A classe filha herda todos os atributos e mátodos de todas as classes herdadas

Quando ma classe herda de outra, dizemaos que ela deriva da classe pai
A herança múltipla pode ser feita por 
    multiderivação direta; 
    multiderivação indireta.
'''


### miultiderivação direta ###

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2):
    pass


### multiderivação indireta ###

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


# Exemplo

class Animal:

    def __init__(self, nome):
        self.__nome = nome


    # em herança, properties devem ficar na classe pai
    @property
    def nome(self):
        return self.__nome


    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'


    # Metodo sobrescrito (overriding)
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        return f'{self.nome} está andando' # estamos acessando sem o __ por causa da property lá na classe pai, linha 58
                                           # deixei self._animal__nome na classe aquatica como referência
                                           # pra saber que podemos acessar das duas formas
    def cumprimentar(self):
        return f'Eu sou {self.nome} da terra'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

baleia = Aquatico('Wally')

pinguim1 = Pinguim('Cornolio')

print(pinguim1.__dict__)
# print(dir(pinguim1))
# print(pinguim1.andar())
# print(pinguim1.nadar())
print(pinguim1.cumprimentar()) # Executou o método sobrescrito na classe Terrestre
                               # Por que o pinguim escolheu o método da classe Terrestre?
                               # A respsosta está na Method Resolution Order - MRO

# Diz se o objeto é instância da classe
# O pinguim pertence à todas as classes que ele herda
print(isinstance(pinguim1, Aquatico))
print(isinstance(pinguim1, Terrestre))
print(isinstance(pinguim1, Animal))

print(isinstance(pinguim1, str))
print(isinstance(pinguim1, object)) # Toda classe criada em Python herda de object
print(pinguim1)

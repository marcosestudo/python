'''
MRO - method resolution order

Em python, podemos ver a ordem de execução das classes de 3 formas:
    via propriedadde da classe __mro__
    via método mro()
    via help
'''


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
                                           # deixei self._animal__nome na classe Aquatico como referência
                                           # pra saber que podemos acessar das duas formas
    def cumprimentar(self):
        return f'Eu sou {self.nome} da terra'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


pinguim1 = Pinguim('Cornolio')


print(pinguim1.cumprimentar())
print(f'Ordem de resolução via __mro__:\n{Pinguim.__mro__}\n')
print(f'Ordem de resolução via mro():\n{Pinguim.mro()}\n')
print(f'Ordem de resolução via help:\n{help(Pinguim)}\n')

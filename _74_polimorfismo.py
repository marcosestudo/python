'''
Polimorfismo significa várias formas
Objetos podem possuir várias formas ou, melhor dizendo, podem se comportar de várias formas

Qunado reemplementamos um método da classe painas classes filhas, estamos fazendo um method overriding
dando outras formas para a funçao da classe pai, overriding é a melhor represnetação que temos do polimorfismo
'''


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    # Não foi implementado aqui porque cada animal tem seu próprio jeito de falar
    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        return f'{self.__nome} está comendo.'


class Cachorro(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self.nome} diz au au'

    def comer(self):
            return f'{self.nome} está comendo...'

class Gato(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} diz miau' # deixando dessa forma _Animal__nome pra não esquecer dessa forma de acesso


class Rato(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)

    # Rato não tem os método falar pra testarmos o raise no falar classe pai
    # O método falar foi sobrescrito nas outras duas classes
    # podemos dizer que ele tem uma forma na classe pai e uma forma diferene em cada classe em que foi sobrescrito
    # logo, o método falar tem várias formas, overriding é a melhor represnetação que temos do polimorfismo


gato1 = Gato('Felix')
cachorro1 = Cachorro('Cornolio')
rato1 = Rato('Hantaro')

# chamando as 3 formas do método falar
print(cachorro1.falar())
print(gato1.falar())
print(rato1.falar())

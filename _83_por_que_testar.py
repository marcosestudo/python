'''
Muitos programadores não gosta de executar testes, pois devem ser programados 
e às vezes programar os testes dá mais trabalho que programar o próprio sistema

Por que realizar testes?
    - reduzir bugs;
    - garantem que novos recursos da aplicação não quebrem ou alterem recursos antigos;
    - garantem que bugs corrigios anteiormente continuem corrigidos;
    - garantem que a refatoração do código não traga novos bugs;
    - o próprio teste serve como documentação do teu programa.


uma vertente de testes automatizados bastante utilizada é chamada de TDD
TDD - test driven development -desenvolvimento guiado por testes
Nela o teste é escrito antes de escrever o próprio código
Primeiro é escrito o teste, depois é escrito o código mínimo que seja suficiente para passar no teste
depois refatora para realizar a funcionalidade e testa novamente
Passar no teste significa que o código foi executado com sucesso

Os estágios de desenvolvimento do TDD são como um mantra que os desenvolvedores seguem conecido como:
    - red;
    - green;
    - refactor.
red e green são sobre as cores das saídas dos teste, vermelho quando dá erro, verde quando passa

'''

class Gato:
    
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    def miar(self):
        print(f'{self.__nome} está miando...')


# testamos as nossas classes instanciando um objeto, acessando seus atributos e executando seus métodos 
# pra ver se estão se comportando da forma esperada
# esses testes são manuais, podemos fazê-los de forma automatizada
gato1 = Gato('Cornolio')
print(gato1.__dict__)
print(dir(gato1))
gato1.miar()
print(gato1.nome)

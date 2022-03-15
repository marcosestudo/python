'''
Às vezes queremos porteger os dados que vamos salvar, salvando-os em formato dierente de documento de texto
Pickle salva dados como se fosse um banco de dados rudimentar
Não salva os dados de forma textual, salva de forma serializada em formato binário hexadecimal

O pickle pode "binarizar" objetos Python e "desbinarizá-los" de volta, isso é chamado de serialização ou deserialização

O Pickle não é seguro contra dados maliciosos
Não dá pra saber o que tem no arqivo antes de executá-lo
Não é seguro trabalhar com arquivos prckle de fontes desconhecidas
'''


import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    def comer(self):
        print (f'{self.__nome} está comendo ...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def miar(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f'{self.nome} está latindo...')


'''Escrita em arquivo pickle'''

gato_antes = Gato('Felix')
cachorro_antes = Cachorro('Cornolio')

# Flag 'wb' >>> w == write, b == binary
with open('animais.pickle', 'wb') as arquivo:
    # dump recebe 2 argumentos, o primeiro, por ter mais de um elemento, foi passado em uma tupla
    pickle.dump((gato_antes, cachorro_antes), arquivo)

print(type(arquivo))
print(arquivo)


'''Leitura de dados de um arquivo pickle'''
# load() retorna uma tupla com os objetos
with open('animais.pickle', 'rb') as arquivo:
    gato_depois, cachorro_depois = pickle.load(arquivo)
    arquivo.seek(0)
    tupla = pickle.load(arquivo)

print(type(tupla))
print(len(tupla)) # podemos ver o len(tupla) pra saber quantos objetos tem no pickle pra distribuí-los como nalinha 65
print(tupla)
print()

print(gato_depois.nome)
print(type(gato_depois))
gato_depois.miar()
print()

print(cachorro_depois.nome)
print(type(cachorro_depois))
cachorro_depois.latir()

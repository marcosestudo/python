'''
Em linguages como o Java, quando declaramos atributos privados, criamos métodos para manipulá-los
Esses métdos são chamados de getters and setters
getters retornam o valor do atributo, setters os alteram

Em python, no lugar dos getters e setters, costumamos usar propriedades

Propriedades usam o decorator @property pros getters e @nome_do_atributo.setter pros setters
'''


# class Conta:

#     contador = 0

#     def __init__(self, titular, saldo, limite):
#         self.__numero = Conta.contador + 1
#         self.__titular = titular
#         self.__saldo = saldo
#         self.__limite = limite
#         Conta.contador += 1

#     def extrato(self):
#         return f'Titular: {self.__titular}\nSaldo: {self.__saldo}\nLimite: {self.__limite}\n'

#     def depositar(self, valor):
#         self.__saldo += valor
                
#     def sacar(self, valor):
#         self.__saldo -= valor

#     def transferir(self, valor, destino):
#         self.__saldo -= valor
#         destino.__saldo += valor

#     def get_numero(self):
#         return self.__numero

#     def get_titular(self):
#         return self.__titular

#     def set_titular(self, titular):
#         self.__titular = titular

#     def get_saldo(self):
#         return self.__saldo

#     def get_limite(self):
#         return self.__limite

#     def set_limite(self, limite):
#         self.__limite = limite 


# conta1 = Conta('Cornolio', 1000, 1000)
# conta2 = Conta('Zerado', 0, 0)
# conta2.set_limite(2000)
# print(conta1.extrato())
# print(conta2.extrato())


'''Refatornado a classe acima com propriedades'''

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # As properties devem vir antes das funções para ficar mas legível 
    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite 

    # podemos criar atributos com as properties
    # o atributo soma_saldo_e_limite não existe na classe
    # poderemos acessá-lo como se fosse um atributo criado no __init__
    @property
    def soma_saldo_e_limite(self):
        return self.__saldo + self.__limite

    def extrato(self):
        return f'Titular: {self.__titular}\nSaldo: {self.__saldo}\nLimite: {self.__limite}\n'

    def depositar(self, valor):
        self.__saldo += valor
                
    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Cornolio', 1000, 1000)
conta2 = Conta('Zerado', 0, 0)

# Com as properties, parece que estamos acessando os atributos diretamente
print(conta2.saldo)
conta2.limite = 'xxxxx'
print(conta2.__dict__)
print(conta2.limite) # com oo decorator @limite.setter conseguimos modificar e acessar a propriedade
# Acessando o atribuo criado com a property
print(conta1.soma_saldo_e_limite)

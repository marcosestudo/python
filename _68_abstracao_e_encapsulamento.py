'''
O objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes

    ______classe______
   |     atributos    |
   |______métodos_____|

Abstração em POO é o ato de espor apenas os dados relevantes de uma classe
escondendo atributos e métodos privados do usuário
ex.: Quando fazemos uma chamada telefônica, o telefone se conecta na cenral da operadora, faz um busca pelo outro número no
banco de dados, conecta os dois e gerencia a chamada. Pro usuário, isso tudo é irrelevante e é abstraído

Significado de abstrair: não considerar, não levar em conta; alhear-se.
'''


# class Conta():
    
#     contador = 400

#     def __init__(self, titular, saldo, limite):
#         self.numero = Conta.contador
#         self.titular = titular
#         self.saldo= saldo
#         self.limite = limite
#         Conta.contador += 1

#     def extrato(self):
#         print(f'Titular: {self.titular}\nNúmero: {self.numero}\nSaldo: {self.saldo}\nLimite: {self.limite}')

#     def depositar(self, valor):
#         self.saldo += valor

#     #exemplo bem simples, deveria ser feita uma checagem se existe saldo para sacar
#     def sacar(self, valor):
#         self.saldo -= valor


# conta1 = Conta('Cornolio', 1200, 3500)
# # com atributos públicos, podemos acessá-los diretamente
# print(conta1.numero) 
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)
# print(conta1.__dict__)
# # se podemos acessá-los, podemos auterá-los
# conta1.numero = 'x' 
# conta1.titular = 'x'
# conta1.saldo = 'x'
# conta1.limite = 'x'
# conta1.extrato()

'''
Os dados devem ser encapsulados e protegidos pela classe
Refatorando a clase com atributos privados
'''

class Conta():
    
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo= saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Titular: {self.__titular}\nNúmero: {self.__numero}\nSaldo: {self.__saldo}\nLimite: {self.__limite}\n')

    def depositar(self, valor):
        if valor >= 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor >= 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor precisa ser positivo')

    def transferencia(self, valor, conta_destino):
        self.sacar(valor)
        # taxa de transferência
        self.__saldo -= 10 
        conta_destino.depositar(valor)


conta1 = Conta('Cornolio', 1200, 3500)
conta2 = Conta('Zerado', 0, 0)

# print(conta1.__dict__)

conta1.transferencia(1200, conta2)
conta1.extrato()
conta2.extrato()

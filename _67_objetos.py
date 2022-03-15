'''
Objetos são instâncias da classe

Depois de definida a classe podemos criar quantos objetos / instâncias forem necessárias
Podemos pensar no objeto como variáveis do tipo definido na classe
'''


class Lampada:
    
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__votagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampaada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz_oi(self):
        print(f'{self.__nome} diz oi') 

class ContaCorrente:

    contador = 1000
    # podemos passar um objeto como parâmetro
    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero 

    def mostra_cliente(self):
        print(f'Cliente: {self.__cliente._Cliente__nome}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# lamp1 = Lampada('branco', 120, 65)
# print(f'Está acesa? {lamp1.checa_lampaada()}') 
# lamp1.ligar_desligar()
# print(f'Está acesa? {lamp1.checa_lampaada()}') 

cliente1 = Cliente('Cornolio', 12345678911)

cc1 = ContaCorrente(5000, 20000, cliente1)
cc1.mostra_cliente()
cc1._ContaCorrente__cliente.diz_oi() # forma de acesso de fora da classe, deixando aqui só pra mostrar que é possível

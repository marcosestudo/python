'''
Métodos são as funções de uma classe
São as ações que a classe pode realizar no seu sistema


Os métodos são ivididos em 2 grupos
    métodos de instância / objeto
    métodos de classe


Os métodos de instâncias estão vinculados a cada instância criada


Os métodos de classe não precisam de instância para serem executados
Na declaração de métodos de classe são usados decorators para indicar que é método de classe, não de instância


Métodos de instância acessam atributos de instância usando o "self"
Métodos de classe acessam atributos de classe usando o "cls"
Métodos staticos não têm parâmetros


Métodos de classe são conhecidos como métodos estáticos em outras linguagens
Python tem os métodos de classe com @classmethod e tem seus próprios métodos estáticos com @staticmethod


Métodos privados tem nome iniciado por __


O método __init__ é um método especial chamado de construtor, ele controi o objeto a partir da classe
Os métodos / funões iniciados e terminados com __ são chamados de dunder
Os métodos dunder são chamados de métodos mágicos, são métodos internos do Python
Não é recomendado criar métodos dunder pra não confundir com os métodos internos
'''


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 1000

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        '''retorna o valor do produto com o desconto'''
        return self.__valor * (100 - porcentagem) / 100


# # Não se coloca código entre as funções, foi colocado aqui pra facilitar a vizualização e ficar mais didático
# p1 = Produto('A', 'Letra A', 1000)
# print(p1.desconto(20))
# print(Produto.desconto(p1, 25)) # pode-se acessar classes de instâncias dessa forma, não é usual


# Foi instalada a bliblioteca passlib com >>> pip install passlib

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def definicao():
        print('Definição')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self): # está sendo usado no contrutor, linha 104
        return self.__email.split('@')[0]

    def gera_usuario_publica(self):
        return self.__gera_usuario()

user1 = Usuario('Cornolio', 'Butthole', 'iamcornolio@gmail.com', '12345')
print(user1._Usuario__gera_usuario()) # acesso direto ao método privado
print(user1.gera_usuario_publica()) # buscar forma correta de se acessar métodos privados
                                    # está sendo usado da forma correta no contrutor, linha 104


# Usuario.conta_usuarios()


# nome = input('Nome ')
# sobrenome = input('Sobrenome ')
# email = input('Email ')
# senha = input('Senha ')
# confirma_senha = input('Confirme a senha ')


# # # deixei o usuário pronto pra não precisar ficar rodando todos aqueles inputs a cada teste
# # user1 = Usuario('Cornolio', 'Butthole', 'iamcornolio@gmail.com', '12345')


# if senha == confirma_senha:
#     user1 = Usuario(nome, sobrenome, email, senha)
# else:
#     print('Senha não confere')
#     exit(1) # 1 é o código de saída que vai aparecer no console, se tiver mais de um exite, sabemos por qual saiu

# print('Usuário criado com sucesso')

# senha = input('Senha: ')

# if user1.checa_senha(senha):
#     print('Acesso permitido')
# else:
#     print('Acesso negado')

# print(f'Senha criptografada: {user1._Usuario__senha}')

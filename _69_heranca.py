'''
POO
Herança - Inheritance


Herança vem da ideia de reaproveitar código e extender as classes
Com a herança, a partir de uma classe existente, extendemos outra classe que passa a herdar seus atributos e métodos
As duas classes devem ter uma relação de "é um"
Ex: todo funcionáro é uma pessoa

Imaginemos um sistema de um banco som as entidades cliente e funcionário

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda.

Funcionário
    - nome;
    - sobrenome;
    - cpf;
    - matrícula.

Ambas as classes têm nome, sobrenome, cpf e o método nome_completo()
Teríamos uma classe genérica com esses atributos?
Poderíamos criar a classe pessoa

Quando uma classe herda de outra classe, ela herda todos os atributos e métodos da classe herdada
Quando cliente e funcionário herdam pessoa, passam ter nome, sobrenome, cpf e o método nome_completo()
A classe herdada é chamada de:
    super classe; 
    classe mãe; 
    classe pai; 
    classe base.
    classe genérica
As classes que herdam de outra classe são chamadas de:
    subclasse
    classe filha
    classe específica

Métodos da classe pai podem ser reescritos na classe filha para funcionar de forma específica nela
isso é chamado de sobrescrita de método (method overriding)
'''


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    '''Cliente(Pessoa) significa: Cliente extende Pessoa ou Cliente herda de Pessoa'''

    def __init__(self, nome, sobrenome, cpf, renda):
        '''Passamos nome, sobrenome, cpf e renda como parâmetros pra criar cliente
        o método super().__init__() vai acessar o construtor da super classe e vai "pegar" os nome, sobrenome e cpf 
        passados no instanciamento do cliente
        com super() podemos acessar qualquer método ou atributo da super classe'''
        
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # classe sobrescrita (overriding) parar mostrar também a matrícula
    def nome_completo(self):
        return f'{self._Pessoa__nome} {self._Pessoa__sobrenome}, matrícula: {self.__matricula}'


cliente1 = Cliente('Cornolio', 'Buthole', '123.456.789-11', 6500)
funcionario1 = Funcionario('Cornolio', 'Buthole', '123.456.789-11', 6500)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
# note que as informações em comum vêm de pessoa, enda e matrícula vêm de cliente e funcionario respectivamente
print(cliente1.__dict__)
print(funcionario1.__dict__)





# # Classes antes de serem refatoradas usando herança

# class Cliente:
#     def __init__(self, nome, sobrenome, cpf, renda):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#         self.__renda = renda

#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'

# class Funcionario:
#     def __init__(self, nome, sobrenome, cpf, matricula):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#         self.__matricula = matricula

#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'

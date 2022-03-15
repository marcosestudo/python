'''
Atributos

Representam as características do objeto

Em Python, dividimos os atributos em 3 grupos
    atributos de instância / obj
    atributos de classe
    atributos dinâmicos

# classe de exemplo
class Produto:

    imposto = 1.05 # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor): # <- método construtor
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


Atributos de instância 
São atibutos declarados dentro do método construtor
Método construtor é usado para a construção do objeto
Todas as instâncias criadas terâo seus próprios atributos de instância
Ao criar o produto p1
p1.nome, p1.descricao e p1.valor são os atributos de instância


Atributos da classe
São declarados dentro da classe fora do construtor, o valor é compartilhado para todas as instâncias
No exemplo, imposto e contador são atributos de classe 
Não é preciso criar uma intância para acessar um atributo de classe
A forma correta de se acessar atributos de classe é sem usar nenhuma instância
Em Java os atributos de classe são chamados de atributos de classe


Atributos dinâmicos
São atributos de instância que podem ser criados durante o tempo de execução
Um atributo dinâmico é exclusivo da instância que o criou
Normalmente não se usa atributos dinâmicos

Em Java, a classe lâmpada ficaria assim
public class Lampada(){               # em Java os atribuots podem ser privados, públicos ou protegidos
    private int nome;             # private só é visivel dentro da classe
    public string email;                # public é visivel em todoo programa
    protected Boolean senha = false; # protected só é visivel dentro do pacote

    public lampada(int nome, string email){     <- esse é o construtor no Java
        this.nome = nome;
        this.email = email;
    }

    public int getnome(){
        return this.nome
    }
    # também seriam criadas funções getemail e getsenha
}

Em Python, por convenção, todo atributo de classe é público
Para sinalizá-los privados, usa-se o dunder "__"
Isso é só uma convenção, o Python não vai nos impedir de acessar os atributos sinalizados como privados fora da classe
Isso é conhecido como name mangling
'''


from mailbox import NotEmptyError


class Lampada:

    def __init__(self, nome, email):
        self.nome = nome # o dunder "__" aqui é equivalente ao private no Java
        self.email = email
        self.senha = False


class Contaemailrente:
    
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    
    def __init__(self, nome,  email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos privados só podem ser acessados dentro da própria classe
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha


    def mostra_senha(self):
        return self.__senha


    @property
    def senha(self):
        return self.__senha


# O Python não impede que acessemos os atributos sinalizados como privados fora da classe
# Usando dir() vemos o atributo "privado" com o nome da classe com um underline antes, isso é chamado de name mangling,
# dessa forma podemos acessar os atributos "privados", não devemos fazer dessa forma
# Podemos acessar criando um método comum ou usando @property, ambos para acessá-lo de dentro da própria classe
user = Acesso('iamcornolio@gmail.com', '12345')


print(dir(user))
print(user.email)
print(f'> acesso direto (não recomendado): {user._Acesso__senha}')
print(f'> método / função comum: {user.mostra_senha()}')
print(f'> método / função com @property: {user.senha}') # só é possível acessar dessa forma por causa da função senha() com o @property


user._Acesso__senha = 'I am Cornolio' # acessando diretamente podemos mudar o valo do atributo
print(user.senha)


# user.senha = 'You shall not pass' # desse jeito não passa, não passa mesmo não





class Produto:

    imposto = 1.05 # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor): # <- método construtor
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto # aqui não foi usado self porque não estamos acessando um atributo da instância/obj
        Produto.contador = self.id           # estamos acessando o atributo da classe


p1 = Produto('A', 'letra A', 1000)
p2 = Produto('B', 'letra B', 1500)

print(p1.valor)
print(Produto.contador) # Não é preciso criar uma intância para acessar um atributo de classe
                       # Essa é a forma recomendável de acessar um atributo de classe
print(p1.id)
print(p2.id) # cada produto criado incrementa o contador


# Atributos dinâmicos
p1.peso = '5Kg' # na classe Produto não existe o atributo peso, está sendo criado agora só pro p1
print(p1.peso)
# print(p2.peso) # AtributeError o objeto p2 não tem o atributo peso 

print(p1.__dict__) # __dict__ gera um dicionário com os atributos e valores da classe
print(p2.__dict__)
print(Produto.__dict__)

del p1.peso # atributos podem ser deletados, não só os dinâmicos
del p2.valor
print('Depois de deletar')
print(p1.__dict__)
print(p2.__dict__)

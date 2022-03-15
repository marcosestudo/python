'''
Métodos mágicos são os método iiciados e terminados com dunder __
Os métodos que estamos sobrescervendo aqui são da classe object

Todo objeto extende da classe object
'''


class Livro:
    
    def __init__(self, titulo, autor, paginas):
        # Não foram usados atributos privados para a aula ficar mais dinâmica
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # # o método __repr__ faz a representação do objeto
    # # a representação padrão do objeto livro quando printamos é <__main__.Livro object at 0x00ED84D8>
    # # __repr__ é um método da classe object
    # # aqui estamos sobrescrevendo o método
    # # fica mais fácil pro desenvolvedor saber o que está acontecendo
    def __repr__(self):
        return f'"{self.titulo}", escrito por {self.autor}'

    # pra criar uma representação visul apro usuário final, usa-se o __string__
    # visualmente não tem diferença
    # se deixar os dois, será executado o __str__
    def __str__(self):
        # return f'"{self.titulo}", escrito por {self.autor}, agora usando o __str__'
        return self.titulo

    # não dá pra usar a função len() em objetos, retorna um erro
    # usando o método __len__ definimos que ao usar a função len() em objetos da classe Livro retornará o número de páginas
    # devevos deixar como return sempre um número inteiro
    def __len__(self):
        return len(self.titulo)

    # podemos deletar variáveis, objetos, etc da memória
    # a = 1
    # del a
    # se tentarmo acessa a variável "a" retornará um erro dizendo que ela não foi deifinida
    # podemos sobrescerver o comportamento do del
    # quando termina de executar o programa, o python deleta todos os objetos
    # vai aparecer essa mensagem para quantos objetos estiverem sido criados no programa
    def __del__(self):
        print(f'Um objeto do tipo {type(self)} foi deletado da memória\n')


    # Não podemos concatenar dois objetos
    # Podemos sobrescrever o método __add__, transformar os objetos em string e concatená-los
    def __add__(self, outro):
        return f'{self} + {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Impossível concatenar'


livro1 = Livro('I am Cornolio', 'Cornolio', 120)
livro2 = Livro('Python rocks!', 'Stalone Cobra', 520)

print(livro1)
print(livro2, '\n')

print(len(livro1), '\n')

# del livro2
# print(livro2)

# concatenando depois de sobrescrever o método __add__
print(livro1 + livro2)

print(livro1 * 3)

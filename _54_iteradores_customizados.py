'''
como funciona um range por dentro
'''


class contador:
    def __init__(self, menor, maior): # funções em objetos / classes são chamadas de métodos da classe
        self.menor = menor            # __init__ é chamado de construtor
        self.maior = maior

    # iteradores devem ter obrigatoriamente as funções __iter__() e __next__()
    def __iter__(self): # transforma o objeto em um iterator
        return self

    def __next__(self): # todo iterável precisa na função next()
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero 
        raise StopIteration ('cabou, lek')


cont = contador(0, 5)


# iterador = iter(cont)


# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))


for i in contador(0,5): # dá pra usar como se fosse um range()
    print(i)

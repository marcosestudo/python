'''
lambdas == funções anônimas ou funções sem nome
sintaxe > lambda parâmetro_de_entrada: saída
'''

def quadrado(num):
    return num ** 2

lambda num: num ** 2 # faz o mesmo que afunção de cima, só que é uma expressão lamba(anônima/sem nome)

quadrado_lambda = lambda num: num ** 2

print(quadrado_lambda(3))


nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# .strip() remove espaçõs aantes e depois da string
print(nome_completo('           asdf         fg      ', '           gh jkl ')) # coloquei espaçoes a mais pra testar o .strip()


sem_entrada = lambda : 'não tenho entrada'
print(sem_entrada())


autores = ['H. G. Wells', 'Isaac Asimov', 'Arthur C. Klarke']
# ordem alfabética pelo sobrenome
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower()) # expressão lambda que coloca só os sobrenomes no .sort()
print(autores) # lambdas são muito usadas para filtragem de dados como nesse caso

print(lambda : 'não tenho entrada')
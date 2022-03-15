"""funções integradas ao python são chamadas de built-in como a função print()
funções são criadas para evtitar repetições no código - coceito DRY - don't repeat yourself
parâmetros vs argumentos
parêmetros são declarados na definição da função
argumentos são passados na hora de chamar da função no lugar dos parâmetros
"""
### DEFININDO A FUNÇÃO ###

# nome da função deve ser em snake_case
# parâmetros de entrada são opcionais, se tiver mais de um devem ser separados por vírgula
# funções podem ou não ter retorno
"""
def nome_da_função(parâmetros_de_entrada):
    bloco_da_função / copro_da_função / implementação
"""

def hello_world():
    print('HELLO WORLD!')

variavel_teste_do_aquivo_41 = 'também dá pra importar variáveis'

print('teste no arquivo _41_: ao importar, executa todo o arquivo, módulos devem ter apenas funções')

if __name__ == '__main__':
    print('teste com if __main__ no arquivo _41_: ao importar, executa todo o arquivo, módulos devem ter apenas funções')

# hello_world()
# print(hello_world()) # a função retorna None


### funções com retorno ###

# def dois_mais_dois():
#     return 2 + 2

# print(dois_mais_dois())


# def dois_retornos_alternativos():
#     if input('digite 1 ou 2\n') == '1':
#         print('digitou 1')
#         return 1
#     print('digitou 2')
#     return 2

# print(dois_retornos_alternativos())


# def tres_numeros():
#     return 1, 2, 3

# print(tres_numeros()) # foi gerada uma tupla por ter sido criada com vírgula sem (), [] ou {}
# num1, num2, num3 = tres_numeros() # tuplas podem ser criadas com ou sem ()
# print(num1, num2, num3)


# from random import random

# def cara_ou_coroa():
#     if random() < 0.5:
#         print('cara')
#     else:
#         print('coroa')
    
# cara_ou_coroa()


### funções com parâmetros ###

# def quadrado(x):
#     return x * x

# print(quadrado(5))


# def soma(a, b):
#     return a + b

# print(soma(2, 3))


### argumentos nomeados (keyword arguments) ###

# def printa_na_ordem(primeiro, segundo):
#     print(f'a: {primeiro}, b: {segundo}')

# printa_na_ordem('um', 'dois')
# printa_na_ordem(segundo='dois', primeiro='um') # passa o argumento pro parâmetro escolhido independentemente da ordem


### funções com parâmetro pardrão - parâmetro opcional ###

# a função print(), por exemplo, funciona com ou sem parâmetro

# def exponencial(numero: int = 0, potencia=2):
#     if numero is not None:
#         return numero ** potencia

# print(exponencial())
# print(exponencial(2)) # se não informar a potência, eleva ao quadrado
# print(exponencial(2, 3))


# def parafun(funcao): # função pode ser dada como parâmetro
#     print('função')
#     print(funcao())

# parafun(exponencial)


### variáveis globais vs variáveis locais

# nome = 'Marcos' # variável global

# def oi(nome): # variável local
#     print(f'Oi, {nome}!')
#     nome = 'Fernando' # variável local e golbal de mesmo nome, muda somente a local
#     print(f'Oi, {nome}!') 

# oi(nome)

# print(nome) 

# def muda_global(nome_novo):
#     global nome
#     nome = nome_novo

# muda_global('Asd Fg')
# print(f'depois de mudar na função: {nome}')

# contador = 0
# def fora():
#     contador = 0

#     def dentro():
#         nonlocal contador # variável não local e ao mesmo tempo não global
#         contador += 1
#         return contador
#     return dentro()

# print(f'contador global 1: {contador}')
# print(f'contador da função 1: {fora()}')
# print(f'contador global 2: {contador}') # o contador global não foi alterado
# print(f'contador da função 2: {fora()}') # o contador da função é inicializado a cada execução

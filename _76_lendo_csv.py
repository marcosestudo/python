'''
CSV - comma separated values - valores separados por vírgula
Podem vir separados por outros separadores como ponto e vírgula, traço, espaço

Pros exemplos da aula foi usado o arquivo lutadores.csv
No site dados.gov.br/dataset podemos coneguir dados para praticar

lutadores.csv veio com cabeçalho, veio escrito "(em cm)", na leitura, fica com "\n"
devemos remover esses dados pois não vamos usá-los
quando começamos a trabalhar um arquivo devemos deixar só o que for útil 
chamamos esse porcesso de limpesa de dado

Python possui duas funções no módulo csv para ler arquivos csv sem precisarmos fazer tudo "a mão"
    reader - itera as linhasdo arquivo csv como listas
    DictReader - itera sobre as linhas do arquivo como OrderedDict
        lembrando: dicionários comuns não mantém a ordem dos elementos, OrderedDict mantém
        aula sobre OrderedDict o arquivo "_16_collections.py"
'''

# # estava dando problema pra ler o arquivo, foi resolvido passando o segundo argumento (encoding='utf_8')
# arquivo = open('lutadores.csv', encoding='utf_8')
# arquivo.close()


from csv import reader


with open('lutadores.csv', encoding='utf_8') as arquivo:
    leitor_csv = reader(arquivo, delimiter=',') # por padrão,  o delimitador é a vírgula
                                                # se for outro, devemos mudar o argumento delimiter    
    # A função reader() retorna um iterator, se não quisermos a primeira linha(se o arquivo tiver cabeçalho)
    # damos um next() no iterator antes de entrar no for e ele começará na segunda linha
    print(type(leitor_csv))
    print(leitor_csv)
    next(leitor_csv)
    
    ordem = 1
    for linha in leitor_csv:
        print(f'linha {ordem}: {linha}')
        ordem += 1


from csv import DictReader


with open('lutadores.csv', encoding='utf_8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',') # por padrão,  o delimitador é a vírgula
                                                    # se for outro, devemos mudar o argumento delimiter
    print()
    print(type(leitor_csv))
    print(leitor_csv)
    next(leitor_csv)

    ordem = 1
    for linha in leitor_csv:
        print(f'linha {ordem}: {linha}')
        ordem += 1

    # Lembrando que dicionários se acessam pelas chaves, não pelos índices
    arquivo.seek(0) # voltando o cursor pro início do arquivo para releitura
    leitor_csv = DictReader(arquivo) # relendo porque o objeto é esvaziado depois do uso

    for linha in leitor_csv:
        print(f"{linha['Nome']} | {linha['País']} | {linha['Altura (em cm)']}")



'''Exercício de dicionários feito usando as informaçoes do arquivo .csv antes de iniciar a aula'''
# # Tudo isso foi feito diretamente usando o DictReader

# print('\nV Exercício V')

# lista = [['Nome', 'País', 'Altura (em cm)'], 
#         ['Ryu', 'Japão', 175], 
#         ['Ken', 'EUA', 175], 
#         ['Chun-Li', 'China', 165],
#         ['Guile', 'EUA', 185],
#         ['E. Honda', 'Japão' , 185],
#         ['Dhalsim', 'Índia', 176],
#         ['Blanka', 'Brasil', 192],
#         ['Zangief', 'Rússia', 214]]


# dict_zip = []
# for i in range(1, len(lista)):
#     dict_zip.append(zip(lista[0], lista[i]))

# print(dict_zip)


# dict_lista = []
# for i in range(len(dict_zip)):
#     dict_lista.append(dict(dict_zip[i]))


# for i in range(len(dict_lista)):
#     print(dict_lista[i])


'''chegando nessa lista usando o reader'''


# from csv import reader


# with open('lutadores.csv', encoding='utf_8') as arquivo:
#     leitor_csv = reader(arquivo)
    
#     # A função reader() retorna um iterator, se não quisermos a primeira linha(se o arquivo tiver cabeçalho)
#     # damos um next() no iterator antes de entrar no for e ele começará na segunda linha
#     print(type(leitor_csv))
#     # next(leitor_csv)
    
#     lista = []
#     for linha in leitor_csv:
#         lista.append(linha)

# for linha in lista:
#     print(linha)

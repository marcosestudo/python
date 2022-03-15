'''
como funciona um loop por dentro
'''


def meu_for(interavel):
    iterador = iter(interavel)
    while True:
        try:
            print(next(iterador)) # o loop vai printar sem precisar da fnção print()
        except StopIteration:
            break


meu_for('string')


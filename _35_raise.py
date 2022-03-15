'''
raise é uma palavra reservada que lança exceções / erros
com raise podemos criar nossas próprias exceções e mansagens de erro
sintaxe > raise TipoDoErro('mensagem de erro')
'''
# raise Exception('eu sabia que tu ia fazer cagada')

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')

    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'cor deve ser {cores}')
    
    print(f'O texto {texto} será impresso na cor {cor}')
    
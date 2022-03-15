"""
Usa-se palavra reservada "assert" pra realizar simples afirmaçõae realizadas nos testes
Usa-se em uma expressão que queremos checar se é válida

Se a expressão for verdadeira,  retorna None, se for falsa levanta um AssertionError

Podemos especificar um segundo argumento ou uma mensagem de erro personalisada
assert pod ser usada em qualquer parte do código mesmo fora dos testes

Se o programa for ezecutado com o parâmeto / flag -O, nenhum assertion será validado
no terminal >>> python -O nome_do_programa.py inicia o programam dessa forma
Por isso é preferível checar p código com try except
"""


# assert 1 == 2, '1 não é igual a 2'

def soma_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos'
    return a + b

print(soma_positivos(1, 2))

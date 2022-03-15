"""
Doctest é um test passado dentro de uma docstring

Para executar os doctests digite no terminal
python -m doctest -v nome_do_módulo.py

Saída ao executar a linha e comando acima:
Trying:
    soma(1, 2)
Expecting:
    3
ok
Trying:
    soma(5, 3)
Expecting:
    8
ok
1 items had no tests:
    _85_doctests
1 items passed all tests:
   2 tests in _85_doctests.soma
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
"""


def soma(a, b):
    """
    Soma os números "a" e "b"
    
    >>> soma(1, 2)
    3

    >>> soma(5, 3)
    8
    """
    return a + b

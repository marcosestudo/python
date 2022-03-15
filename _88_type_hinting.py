"""O typehinting nos diz os tipos do paâmetro e o tipo de retorno
Não nos impede de colocarmos outro tipo, é só uma dica (hint)
Existem ferramentas de checagem de tipos que usa os typehintings como o módulo mypy, por exemplo
pip install mypy
O typehinting deixa a execução do código um pouco mais lenta
"""


from __future__ import annotations


# função com typehinting
def soma(a: int = 0, b: int = 0) -> int:
    return a + b


# função sem type hinting
def soma2(a=0, b=0):
    return a + b


# typehint também pode ser usado em variáveis
variavel: int = 53

lista1: list = []
tupla1: tuple = ()
dicionario1: dict = {}
conjunto: set = {}


# parar dizer os tipos de dentro do s containers devemos importar os tipos / métodos do módulo typing
from typing import Dict, List, Tuple, Set


lista1: List[int] = [1, 2, 3]
tupla1: Tuple[int, int, int] = (1, 2, 3)
dicionario1: Dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
conjunto: Set[int] = {1, 2, 3}


class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade

    def andar(self) -> str:
        return f'{self.__nome} está andando'


pessoa1 = Pessoa(nome='Cornolio', idade=12)

# __annotations__ retorna um dicionário com os typehints
print(soma.__annotations__)

# annotations sozinho diz os typehints das variáveis globais do código
print(__annotations__)

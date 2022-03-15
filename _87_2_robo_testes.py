"""Para executar os teste no terminal:
python nome_do_arquivo_de_testes.py

Para executar os teste no terminal no modo verbose:
python nome_do_arquivo_de_testes -v
"""


import unittest

# Estamos impoprtando a classe Robo(com letra maiúscula)
from _87_1_robo import Robo


# class RoboTestes(unittest.TestCase):

#     # Aqui, sem setUp(), devemos instanciar o robo a cada teste
#     # A partir da linha 29 este código será refatorado usando setUp() e tearDown()
#     def test_carregar(self):
#         cornoliobot = Robo('Cornolio', bateria=50)
#         cornoliobot.carregar()
#         self.assertEqual(cornoliobot.bateria, 100)

#     def test_dizer_nome(self):
#         cornoliobot = Robo('Cornolio', bateria=50)
#         self.assertEqual(cornoliobot.dizer_nome(), 'BEEP, eu sou CORNOLIO')
#         self.assertEqual(cornoliobot.bateria, 49, 'A bateria deveria estar em 49%')


"""Refatorando"""


class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.cornoliobot = Robo('Cornolio', bateria=50)
        print('setUp() sendo executado')

    def test_carregar(self):
        self.cornoliobot.carregar()
        self.assertEqual(self.cornoliobot.bateria, 100)
        print('test 1 sendo executado')

    def test_dizer_nome(self):
        self.assertEqual(self.cornoliobot.dizer_nome(), 'BEEP, eu sou CORNOLIO')
        self.assertEqual(self.cornoliobot.bateria, 49, 'A bateria deveria estar em 49%')
        print('test 2 sendo executado')

    def tearDown(self):
        print('tearDown() sendo executado')


if __name__ == '__main__':
    unittest.main()

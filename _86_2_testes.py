"""Para executar os teste no terminal:
python nome_do_arquivo_de_testes.py

Para executar os teste no terminal no modo verbose:
python nome_do_arquivo_de_testes -v
"""


import unittest

from _86_1_atividades import comer, dormir


# É interessante nomear a clase co o mesmo nome do módulo a ser testado
class AtividadesTestes(unittest.TestCase):
    # por convenção, criamos a função de teste com o nome test_[nome da função testada](unitest.TestCase)
    def test_comer_saldavel(self):
        """Testando com comida saldável"""
        self.assertEqual(
            comer('aveia', True),
            'Estou comendo aveia pra manter a forma.'
        )


    def test_comer_fastfood(self):
        """Testando com comida não saudável"""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False), 
            'A ente só vive uma vez'
        )


# Se o arquivo / modulo de teste for executado diretamente o seu nome será "__main__"
# Será executada função main() do unittest que varrerá o arquivo executando todos os unittests do TestCase
if __name__ == '__main__': # Esse if garante que os testes só serão executados se executarmos o arquivo de testes diretamente
    unittest.main()

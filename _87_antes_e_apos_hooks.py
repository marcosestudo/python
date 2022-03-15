"""Antes do início dos teste devemos ter em mãos dados, objetos e afins para trabalharmos nos testes
Após os teste devemos zerar dados, fechar conexões com bancos de dados, etc

Esses momentos de pré inicialização e encerramento são conhecidos como hooks
-------------------------
hooks são os testes em si
------------------------- 
Estamos falando de realizar algo antes ou depopis dos testes / hooks

O unittest tem 2 métodos pra isso
    setUp()
    tearDown()
setUp() é executado antes de cada métodos de teste, útil para criarmos instâncias e outros dados
tearDown() é executado ao final de cada método de teste, útil para excluir dados(arquivo de texto criado no teste, por exemplo) 
ou fechar conexões com bancos de dados
"""


import unittest


class ModuloTest(unittest.TestCase):
    
    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # O setUp() vai rodar antes do teste
        # O tearDown() vai rodar após o teste
        pass

    def test_primeiro(self):
        pass 

    # O tearDown() pode ser declarado no início da classe, será executado no fim da mesma forma
    # Sempre antes do teste é executado o setUp() e depois é executado o tearDown()
    def tearDown(self):
        # Configuraçãoes do tearDown()
        pass

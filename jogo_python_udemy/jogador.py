class Jogador:

    def __init__(self, pontuacao, vida):
        self.__pontuacao = pontuacao
        self.__vida = vida

    @property
    def pontuacao(self):
        return self.__pontuacao

    @property
    def vida(self):
        return self.__vida

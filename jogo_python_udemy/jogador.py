class Jogador:

    def __init__(self, vida: int, pontuacao: int = 0):
        self.__vida = vida
        self.__pontuacao = pontuacao
        
    @property
    def vida(self):
        return self.__vida

    @property
    def pontuacao(self):
        return self.__pontuacao

class Robo:
    
    def __init__(self, nome: str, bateria: int = 100, habilidades: list = []) -> None:
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'BEEP, eu sou {self.__nome.upper()}'
        return 'Bateria fraca :||0||'

    def aprender_habilidade(self, nova_habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidades.append(nova_habilidade)
            return f'UAU! Eu aprendi {nova_habilidade}'
        return 'Bateria insuficiente, recarregue e tente novamente'

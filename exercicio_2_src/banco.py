from exercicio_2_src.dinheiro import Moeda
from exercicio_2_src.agencia import Agencia

class Banco:

    def __init__(self, nome, moeda : Moeda):
        self.__nome = nome
        self.__moeda = moeda
        self.__agencias = []

    @property
    def nome(self):
        return self.__nome

    @property
    def moeda(self):
        return self.__moeda

    def criar_agencia(self, nome):
        agencia = Agencia(nome, len(self.__agencias)+1, self)
        self.__agencias.append(agencia)
        return agencia

    def obter_agencias(self):
        return self.__agencias

    def obter_agencia(self, nome) -> Agencia:
        for agencia in self.__agencias:
            if agencia.nome == nome:
                return agencia
        return None

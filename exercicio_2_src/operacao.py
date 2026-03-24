from enum import Enum


class EstadosDeOperacao(Enum):
    SUCESSO = 1
    SALDO_INSUFICIENTE = 2
    MOEDA_INVALIDA = 3



class Operacao:

    def __init__(self, estado : EstadosDeOperacao):
        self.__estado = estado

    def obter_estado(self):
        return self.__estado

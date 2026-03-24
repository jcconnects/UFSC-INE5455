from exercicio_2_src.transacao import Transacao
from exercicio_2_src.dinheiro import Dinheiro

class Conta:

    def __init__(self, titular, codigo, agencia):
        self.__titular = titular
        self.__codigo = codigo
        self.__agencia = agencia
        self.__transacoes = []

    def obter_identificador(self):
        return '{0:04d}-{1}'.format(self.__codigo, len(self.__titular) % 10)

    @property
    def titular(self):
        return self.__titular

    @property
    def agencia(self):
        return self.__agencia

    def calcular_saldo(self):
        moeda = self.agencia.banco.moeda
        saldo = Dinheiro(moeda, 0, 0).positivo()
        for transacao in self.__transacoes:
            saldo = transacao.contabilizar(saldo)
        return saldo

    def adicionar_transacao(self, transacao : Transacao):
        self.__transacoes.append(transacao)

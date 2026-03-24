from exercicio_2_src.dinheiro import Moeda, Dinheiro, ValorMonetario
from exercicio_2_src.banco import Banco
from exercicio_2_src.conta import Conta
from exercicio_2_src.operacao import EstadosDeOperacao, Operacao
from exercicio_2_src.transacao import TransacaoNaoRealizada, Entrada, Saida

class SistemaBancario:

	def __init__(self):
		self.__bancos = []

	def criar_banco(self, nome, moeda : Moeda):
		banco = Banco(nome, moeda)
		self.__bancos.append(banco)
		return banco

	def __moeda_invalida(self, conta : Conta, quantia : Dinheiro):
		moeda_do_banco = conta.agencia.banco.moeda
		moeda_da_operacao = quantia.moeda
		return moeda_do_banco != moeda_da_operacao

	def depositar(self, conta : Conta, quantia : Dinheiro):
		entrada = Entrada(quantia)
		estado = EstadosDeOperacao.SUCESSO
		if self.__moeda_invalida(conta, quantia):
			entrada = TransacaoNaoRealizada(entrada)
			estado = EstadosDeOperacao.MOEDA_INVALIDA
		elif quantia.inteiro + quantia.fracionado <= 0:
			entrada = TransacaoNaoRealizada(entrada)
			estado = EstadosDeOperacao.SALDO_INSUFICIENTE
		conta.adicionar_transacao(entrada)
		return Operacao(estado)
		# return Operacao(estado, entrada)

	def saldo_ficara_negativo(self, saldo : ValorMonetario, quantia : Dinheiro):
		return saldo.obter_quantia().obter_quantia_em_escala() < quantia.obter_quantia_em_escala()

	def sacar(self, conta : Conta, quantia : Dinheiro):
		saldo = conta.calcular_saldo()
		saida = Saida(quantia)
		estado = EstadosDeOperacao.SUCESSO
		if saldo.negativo() or self.saldo_ficara_negativo(saldo, quantia):
			saida = TransacaoNaoRealizada(saida)
			estado = EstadosDeOperacao.SALDO_INSUFICIENTE
		if self.__moeda_invalida(conta, quantia):
			saida = TransacaoNaoRealizada(saida)
			estado = EstadosDeOperacao.MOEDA_INVALIDA
		conta.adicionar_transacao(saida)
		return Operacao(estado)
		# return Operacao(estado, saida)

	def transferir(self, origem : Conta, destino : Conta, quantia : Dinheiro):
		saida = Saida(quantia)
		entrada = Entrada(quantia)
		estado = EstadosDeOperacao.SUCESSO
		if self.__moeda_invalida(origem, quantia) or self.__moeda_invalida(destino, quantia):
			saida = TransacaoNaoRealizada(saida)
			entrada = TransacaoNaoRealizada(entrada)
			estado = EstadosDeOperacao.MOEDA_INVALIDA
		elif origem.calcular_saldo().obter_quantia().obter_quantia_em_escala() < quantia.obter_quantia_em_escala():
			saida = TransacaoNaoRealizada(saida)
			entrada = TransacaoNaoRealizada(entrada)
			estado = EstadosDeOperacao.SALDO_INSUFICIENTE
		origem.adicionar_transacao(saida)
		destino.adicionar_transacao(entrada)
		return Operacao(estado)
		# return Operacao(estado, saida, entrada)

	def obter_bancos(self):
		return self.__bancos

	def obter_banco(self, nome) -> Banco:
		for banco in self.__bancos:
			if banco.nome == nome:
				return banco
		return None

import unittest

from exercicio_2_src.dinheiro import Dinheiro, Moeda, ValorMonetario
from exercicio_2_src.banco import Banco
from exercicio_2_src.agencia import Agencia
from exercicio_2_src.conta import Conta
from exercicio_2_src.sistema_bancario import SistemaBancario
from exercicio_2_src.transacao import Entrada
from exercicio_2_src.operacao import EstadosDeOperacao

# In-line setup
# Implicit setup
#   Usa um usa um método setup antes de executar o teste efetivamente
# Delegated setup
#   Outra classe com os métodos utilizados para setup

# Faça 20 ou mais testes de unidade para as seguintes
# classes:
# ▪ Dinheiro
# ▪ Valor Monetario
# ▪ Conta
# ▪ Agencia
# ▪ Banco
# ▪ SistemaBancario

class TestHelper(unittest.TestCase):
    def criar_estrutura_bancaria_padrao(self):
        banco = Banco("Banco do Brasil", Moeda.BRL)
        agencia = Agencia("001", 1, banco)
        conta = Conta("JOAO", "123456", agencia)
        return banco, agencia, conta

    def criar_sistema_com_duas_contas(self):
        sistema = SistemaBancario()
        banco = sistema.criar_banco("Banco do Brasil", Moeda.BRL)
        agencia = banco.criar_agencia("Agencia Central")
        conta_joao = agencia.criar_conta("JOAO")
        conta_pedro = agencia.criar_conta("PEDRO")
        return sistema, conta_joao, conta_pedro

    def criar_conta_com_saldo(self, reais):
        _, _, conta = self.criar_estrutura_bancaria_padrao()
        conta.adicionar_transacao(Entrada(self.dinheiro_brl(reais)))
        return conta

    def dinheiro_brl(self, reais, centavos=0):
        return Dinheiro(Moeda.BRL, reais, centavos)

    def dinheiro_usd(self, dolares, centavos=0):
        return Dinheiro(Moeda.USD, dolares, centavos)


class TestDinheiro(unittest.TestCase):
    def test_obter_quantia_em_escala(self):
        # Inline setup
        dinheiro = Dinheiro(Moeda.BRL, 100, 13)
        # Exercise SUT
        quantia_em_escala = dinheiro.obter_quantia_em_escala()
        # Verify Result
        self.assertEqual(quantia_em_escala, 10013)
        # Fixture Teardown

    def test_zero(self):
        # Inline setup
        dinheiro = Dinheiro(Moeda.BRL, 0, 0)
        # Exercise SUT
        result_zero = dinheiro.zero()
        # Verify Result
        self.assertTrue(result_zero)
        # Fixture Teardown

    def test_not_zero(self):
        # Inline setup
        dinheiro = Dinheiro(Moeda.BRL, 0, 7)
        # Exercise SUT
        result_zero = dinheiro.zero()
        # Verify Result
        self.assertFalse(result_zero)
        # Fixture Teardown

    def test_formatar_com_moeda(self):
        # Inline setup
        dinheiro = Dinheiro(Moeda.BRL, 10, 7)
        # Exercise SUT
        result_formatar_com_moeda = dinheiro.formatar_com_moeda()
        # Verify Result
        self.assertEqual(result_formatar_com_moeda, "10,07 BRL")
        # Fixture Teardown

    def test_formatar_sem_moeda(self):
        # Inline setup
        dinheiro = Dinheiro(Moeda.USD, 0, 21)
        # Exercise SUT
        result_formatar_sem_moeda = dinheiro.formatar_sem_moeda()
        # Verify Result
        self.assertEqual(result_formatar_sem_moeda, "0,21")
        # Fixture Teardown


class TestValorMonetario(unittest.TestCase):
    def setUp(self) -> None:
        self.moeda = Moeda.BRL
        self.valor_inicial = ValorMonetario(self.moeda, 1000)
        return super().setUp()

    def test_somar(self):
        # Implicit setup
        # Inline setup
        valor_monetario_a_ser_somado = ValorMonetario(self.moeda, 1500)
        # Exercise SUT
        valor_monetario = self.valor_inicial.somar(valor_monetario_a_ser_somado.obter_quantia())
        # Verify Result
        self.assertEqual(valor_monetario.obter_quantia().formatar_sem_moeda(), "25,00")
        # Fixture Teardown

class TestBanco(unittest.TestCase):
    def test_criar_banco(self):
        # Exercise SUT
        banco = Banco("HSBC", Moeda.BRL)
        # Verify Result
        self.assertEqual(banco.nome, "HSBC")
        self.assertEqual(banco.moeda, Moeda.BRL)
        # Fixture Teardown

    def test_criar_agencia(self):
        # Inline setup
        banco = Banco("HSBC", Moeda.BRL)
        # Exercise SUT
        agencia = banco.criar_agencia("A melhor agencia")
        # Verify Result
        self.assertEqual(agencia.nome, "A melhor agencia")
        # Fixture Teardown

    def test_obter_agencia(self):
        # Inline setup
        banco = Banco("HSBC", Moeda.BRL)
        banco.criar_agencia("A melhor agencia")
        # Exercise SUT
        agencia_obtida = banco.obter_agencia("A melhor agencia")
        # Verify Result
        self.assertEqual(agencia_obtida.nome, "A melhor agencia")
        self.assertEqual(agencia_obtida.banco.nome, "HSBC")
        self.assertEqual(agencia_obtida.obter_identificador(), "001")
        self.assertEqual(agencia_obtida.obter_contas(), [])
        # Fixture Teardown


class TestAgencia(unittest.TestCase):
    def setUp(self):
        self.banco = Banco("Banco do Brasil", moeda=Moeda.BRL)
        self.agencia = Agencia("0001", 1, "Banco do Brasil")
        return super().setUp()
    
    def test_get_banco(self):
        # Implicit setup
        # Exercise SUT
        banco = self.agencia.banco
        # Verify Result
        self.assertEqual(banco, "Banco do Brasil")
        # Fixture Teardown

    def test_obter_identificador(self):
        # Implicit setup
        # Exercise SUT
        identificador = self.agencia.obter_identificador()
        # Verify Result
        self.assertEqual(identificador, "001")
        # Fixture Teardown


class TestConta(unittest.TestCase):
    # Delegated setup
    def setUp(self):
        self.test_helper = TestHelper()
        _, _, self.conta = self.test_helper.criar_estrutura_bancaria_padrao()
        return super().setUp()

    def test_get_titular(self):
        # Delegated setup
        # Implicit setup
        # Exercise SUT
        titular = self.conta.titular
        # Verify Result
        self.assertEqual(titular, "JOAO")
        # Fixture Teardown

    def test_calcular_saldo(self):
        # Delegated setup
        dinheiro = self.test_helper.dinheiro_brl(10)
        # Implicit setup
        # Inline setup
        self.conta.adicionar_transacao(Entrada(dinheiro))
        # Exercise SUT
        saldo = self.conta.calcular_saldo()
        # Verify Result
        self.assertEqual(saldo.obter_quantia().formatar_sem_moeda(), "10,00")
        # Fixture Teardown


class TestSistemaBancario(unittest.TestCase):
    def setUp(self):
        self.test_helper = TestHelper()
        # Delegated setup
        self.sistema_bancario, self.conta_joao, self.conta_pedro = self.test_helper.criar_sistema_com_duas_contas()
        return super().setUp()

    def test_criar_banco(self):
        # Implicit setup
        # Inline setup
        banco_esperado = Banco("HSBC", Moeda.BRL)
        # Exercise SUT
        banco = self.sistema_bancario.criar_banco("HSBC", Moeda.BRL)
        # Verify Result
        self.assertEqual(banco.nome, banco_esperado.nome)
        self.assertEqual(banco.moeda, banco_esperado.moeda)
        # Fixture Teardown

    def test_obter_banco(self):
        # Implicit setup
        # Inline setup
        banco_esperado = self.sistema_bancario.criar_banco("Bradesco", Moeda.BRL)
        # Exercise SUT
        banco = self.sistema_bancario.obter_banco("Bradesco")
        # Verify Result
        self.assertEqual(banco.nome, banco_esperado.nome)
        self.assertEqual(banco.moeda, banco_esperado.moeda)
        # Fixture Teardown

    def test_depositar_sucesso(self):
        # Delegated setup
        dinheiro = self.test_helper.dinheiro_brl(10)
        # Implicit setup
        # Exercise SUT
        resultado = self.sistema_bancario.depositar(self.conta_joao, dinheiro)
        # Verify Result
        self.assertEqual(resultado.obter_estado(), EstadosDeOperacao.SUCESSO)
        # Fixture Teardown

    def test_depositar_moeda_invalida(self):
        # Delegated setup
        dinheiro = self.test_helper.dinheiro_usd(10)
        # Implicit setup
        # Exercise SUT
        resultado = self.sistema_bancario.depositar(self.conta_joao, dinheiro)
        # Verify Result
        self.assertEqual(resultado.obter_estado(), EstadosDeOperacao.MOEDA_INVALIDA)
        # Fixture Teardown

    def test_transferir_sucesso(self):
        # Delegated setup
        dinheiro = self.test_helper.dinheiro_brl(10)
        # Implicit setup
        # Inline setup
        self.conta_joao.adicionar_transacao(Entrada(dinheiro))
        # Exercise SUT
        resultado = self.sistema_bancario.transferir(self.conta_joao, self.conta_pedro, dinheiro)
        # Verify Result
        self.assertEqual(resultado.obter_estado(), EstadosDeOperacao.SUCESSO)
        self.assertEqual(self.conta_joao.calcular_saldo().obter_quantia().moeda, self.test_helper.dinheiro_brl(0).moeda)
        self.assertEqual(self.conta_joao.calcular_saldo().obter_quantia().formatar_sem_moeda(), self.test_helper.dinheiro_brl(0).formatar_sem_moeda())
        self.assertEqual(self.conta_pedro.calcular_saldo().obter_quantia().moeda, dinheiro.moeda)
        self.assertEqual(self.conta_pedro.calcular_saldo().obter_quantia().formatar_sem_moeda(), dinheiro.formatar_sem_moeda())
        # Fixture Teardown

    def test_transferir_saldo_insuficiente(self):
        # Delegated setup
        dinheiro = self.test_helper.dinheiro_brl(20)
        # Implicit setup
        # Exercise SUT
        resultado = self.sistema_bancario.transferir(self.conta_joao, self.conta_joao, dinheiro)
        # Verify Result
        self.assertEqual(resultado.obter_estado(), EstadosDeOperacao.SALDO_INSUFICIENTE)
        # Fixture Teardown

    def test_transferir_moeda_invalida(self):
        # Delegated setup
        dinheiro = self.test_helper.dinheiro_usd(10)
        # Implicit setup
        # Exercise SUT
        resultado = self.sistema_bancario.transferir(self.conta_joao, self.conta_pedro, dinheiro)
        # Verify Result
        self.assertEqual(resultado.obter_estado(), EstadosDeOperacao.MOEDA_INVALIDA)
        # Fixture Teardown

if __name__ == "__main__":
    unittest.main()

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ocorrencia import Ocorrencia, TipoOcorrencia, PrioridadeOcorrencia
from src.empresa import Empresa
from src.funcionario import Funcionario


class Test(unittest.TestCase):

    def setUp(self):
        self.empresa = Empresa(nome="WEG")

    # Teste 01
    def test_criar_empresa(self):
        empresa = Empresa(nome="WEG")
        self.assertIsInstance(empresa, Empresa)
        self.assertEqual(empresa.nome, "WEG")

    # Teste 02
    def test_criar_um_funcionario(self):
        funcionario = self.empresa.criar_funcionario(nome="João")
        self.assertEqual(len(self.empresa.funcionarios), 1)
        self.assertEqual(self.empresa.funcionarios[0], funcionario)

    # Teste 03
    def test_criar_dois_funcionarios(self):
        funcionario1 = self.empresa.criar_funcionario(nome="João")
        funcionario2 = self.empresa.criar_funcionario(nome="Maria")
        self.assertEqual(len(self.empresa.funcionarios), 2)
        self.assertEqual(self.empresa.funcionarios[0], funcionario1)
        self.assertEqual(self.empresa.funcionarios[1], funcionario2)

    # Teste 04
    def test_criar_um_projeto(self):
        self.empresa.criar_projeto(nome="Motor a jato")
        self.assertEqual(len(self.empresa.projetos), 1)
        self.assertEqual(self.empresa.projetos[0].nome, "Motor a jato")

    # Teste 05
    def test_criar_projeto_com_nome_vazio(self):
        with self.assertRaises(ValueError):
            self.empresa.criar_projeto(nome="")

    # Teste 06
    def test_criar_empresa_com_nome_vazio(self):
        with self.assertRaises(ValueError):
            Empresa(nome="")

    # Teste 07
    def test_criar_funcionario_com_nome_vazio(self):
        with self.assertRaises(ValueError):
            self.empresa.criar_funcionario(nome="")

    # Teste 08
    def test_assinar_um_funcionario_a_um_projeto(self):
        funcionario = self.empresa.criar_funcionario(nome="Augusto")
        projeto = self.empresa.criar_projeto(nome="O pior projeto de todos")
        self.empresa.assinar_funcionario_a_projeto(funcionario, projeto)
        self.assertTrue(funcionario in projeto.funcionarios)
        self.assertTrue(projeto in funcionario.projetos)

    # Teste 09
    def test_assinar_dois_funcionarios_a_um_projeto(self):
        funcionario_carlos = self.empresa.criar_funcionario(nome="Carlos")
        funcionario_jose = self.empresa.criar_funcionario(nome="José")
        projeto = self.empresa.criar_projeto(nome="Um projeto legal")
        self.empresa.assinar_funcionario_a_projeto(funcionario_carlos, projeto)
        self.empresa.assinar_funcionario_a_projeto(funcionario_jose, projeto)
        self.assertTrue(funcionario_carlos in projeto.funcionarios)
        self.assertTrue(funcionario_jose in projeto.funcionarios)

    # Teste 10
    def test_assinar_dois_funcionarios_a_dois_projetos(self):
        funcionario_carlos = self.empresa.criar_funcionario(nome="Carlos")
        funcionario_jose = self.empresa.criar_funcionario(nome="José")
        projeto_iot = self.empresa.criar_projeto(nome="IoT")
        projeto_tdd = self.empresa.criar_projeto(nome="TDD")
        self.empresa.assinar_funcionario_a_projeto(funcionario_carlos, projeto_iot)
        self.empresa.assinar_funcionario_a_projeto(funcionario_jose, projeto_tdd)
        self.empresa.assinar_funcionario_a_projeto(funcionario_carlos, projeto_iot)
        self.empresa.assinar_funcionario_a_projeto(funcionario_jose, projeto_tdd)
        self.assertTrue(funcionario_carlos in projeto_iot.funcionarios)
        self.assertTrue(funcionario_jose in projeto_tdd.funcionarios)
        self.assertTrue(funcionario_carlos in projeto_iot.funcionarios)
        self.assertTrue(funcionario_jose in projeto_tdd.funcionarios)

    # Teste 11
    def test_criar_varios_funcionarios(self):
        funcionario_joao = self.empresa.criar_funcionario(nome="João")
        funcionario_maria = self.empresa.criar_funcionario(nome="Maria")
        funcionario_ana = self.empresa.criar_funcionario(nome="Ana")
        funcionario_carlos = self.empresa.criar_funcionario(nome="Carlos")
        funcionario_jose = self.empresa.criar_funcionario(nome="José")
        self.assertEqual(len(self.empresa.funcionarios), 5)
        self.assertEqual(self.empresa.funcionarios[0], funcionario_joao)
        self.assertEqual(self.empresa.funcionarios[1], funcionario_maria)
        self.assertEqual(self.empresa.funcionarios[2], funcionario_ana)
        self.assertEqual(self.empresa.funcionarios[3], funcionario_carlos)
        self.assertEqual(self.empresa.funcionarios[4], funcionario_jose)

    # Teste 12
    def test_criar_varios_projetos(self):
        projeto_av = self.empresa.criar_projeto(nome="AV")
        projeto_carro = self.empresa.criar_projeto(nome="Carro")
        projeto_hidroaviao = self.empresa.criar_projeto(nome="Hidroaviao")
        projeto_quantico = self.empresa.criar_projeto(nome="Quantico")
        projeto_espacial = self.empresa.criar_projeto(nome="Espacial")
        self.assertEqual(len(self.empresa.projetos), 5)
        self.assertEqual(self.empresa.projetos[0], projeto_av)
        self.assertEqual(self.empresa.projetos[1], projeto_carro)
        self.assertEqual(self.empresa.projetos[2], projeto_hidroaviao)
        self.assertEqual(self.empresa.projetos[3], projeto_quantico)
        self.assertEqual(self.empresa.projetos[4], projeto_espacial)

    # Teste 13
    def test_criar_uma_ocorrencia_bug(self):
        projeto_cco = self.empresa.criar_projeto(nome="Projetinho de CCO")
        funcionario_jasmin = self.empresa.criar_funcionario(nome="Jasmin")
        self.empresa.assinar_funcionario_a_projeto(
            funcionario=funcionario_jasmin, projeto=projeto_cco
        )
        resumo = "Falha no sistema."
        ocorrencia_bug = self.empresa.projetos[0].criar_ocorrencia(
            tipo=TipoOcorrencia.BUG,
            prioridade=PrioridadeOcorrencia.MEDIA,
            resumo=resumo,
            responsavel=funcionario_jasmin.id,
        )
        self.assertTrue(ocorrencia_bug.estado)
        self.assertEqual(ocorrencia_bug.tipo, TipoOcorrencia.BUG)
        self.assertEqual(ocorrencia_bug.resumo, resumo)
        self.assertEqual(ocorrencia_bug.prioridade, PrioridadeOcorrencia.MEDIA)

        self.assertEqual(ocorrencia_bug.responsavel, funcionario_jasmin.id)
        self.assertEqual(funcionario_jasmin.ocorrencias[0], ocorrencia_bug)
        self.assertEqual(ocorrencia_bug.projeto, projeto_cco.id)
        self.assertEqual(projeto_cco.ocorrencias[0], ocorrencia_bug)

    # Teste 14
    def test_criar_uma_ocorrencia_tarefa(self):
        projeto = self.empresa.criar_projeto(nome="Projeto Tarefa")
        funcionario = self.empresa.criar_funcionario(nome="Carlos")
        self.empresa.assinar_funcionario_a_projeto(funcionario, projeto)
        resumo = "Implementar feature X."
        ocorrencia = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.TAREFA,
            prioridade=PrioridadeOcorrencia.BAIXA,
            resumo=resumo,
            responsavel=funcionario.id,
        )
        self.assertTrue(ocorrencia.estado)
        self.assertEqual(ocorrencia.tipo, TipoOcorrencia.TAREFA)
        self.assertEqual(ocorrencia.resumo, resumo)
        self.assertEqual(ocorrencia.prioridade, PrioridadeOcorrencia.BAIXA)
        self.assertEqual(ocorrencia.responsavel, funcionario.id)
        self.assertEqual(funcionario.ocorrencias[0], ocorrencia)
        self.assertEqual(ocorrencia.projeto, projeto.id)
        self.assertEqual(projeto.ocorrencias[0], ocorrencia)

    # Teste 15
    def test_criar_uma_ocorrencia_refatoracao(self):
        projeto = self.empresa.criar_projeto(nome="Projeto Refatoracao")
        funcionario = self.empresa.criar_funcionario(nome="Maria")
        self.empresa.assinar_funcionario_a_projeto(funcionario, projeto)
        resumo = "Refatorar modulo Y."
        ocorrencia = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.REFATORACAO,
            prioridade=PrioridadeOcorrencia.ALTA,
            resumo=resumo,
            responsavel=funcionario.id,
        )
        self.assertTrue(ocorrencia.estado)
        self.assertEqual(ocorrencia.tipo, TipoOcorrencia.REFATORACAO)
        self.assertEqual(ocorrencia.resumo, resumo)
        self.assertEqual(ocorrencia.prioridade, PrioridadeOcorrencia.ALTA)
        self.assertEqual(ocorrencia.responsavel, funcionario.id)
        self.assertEqual(funcionario.ocorrencias[0], ocorrencia)
        self.assertEqual(ocorrencia.projeto, projeto.id)
        self.assertEqual(projeto.ocorrencias[0], ocorrencia)

    # Teste 16
    def test_criar_multiplas_ocorrencias(self):
        projeto = self.empresa.criar_projeto(nome="Projeto Multi Bug")
        funcionario = self.empresa.criar_funcionario(nome="Jose")
        self.empresa.assinar_funcionario_a_projeto(funcionario, projeto)
        oc_bug = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.BUG,
            prioridade=PrioridadeOcorrencia.ALTA,
            resumo="Bug tenebroso",
            responsavel=funcionario.id,
        )
        oc_tarefa = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.TAREFA,
            prioridade=PrioridadeOcorrencia.MEDIA,
            resumo="Corrigir o bug tenebroso",
            responsavel=funcionario.id,
        )
        oc_refatoracao = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.REFATORACAO,
            prioridade=PrioridadeOcorrencia.BAIXA,
            resumo="Refatorar código ao redor do bug tenebroso",
            responsavel=funcionario.id,
        )
        self.assertEqual(len(projeto.ocorrencias), 3)
        self.assertEqual(projeto.ocorrencias[0], oc_bug)
        self.assertEqual(projeto.ocorrencias[1], oc_tarefa)
        self.assertEqual(projeto.ocorrencias[2], oc_refatoracao)
        self.assertEqual(len(funcionario.ocorrencias), 3)
        self.assertEqual(funcionario.ocorrencias[0], oc_bug)
        self.assertEqual(funcionario.ocorrencias[1], oc_tarefa)
        self.assertEqual(funcionario.ocorrencias[2], oc_refatoracao)

    # Teste 17
    def test_criar_ocorrencia_tipo_invalido(self):
        projeto = self.empresa.criar_projeto(nome="Projeto X")
        funcionario = self.empresa.criar_funcionario(nome="Ana")
        self.empresa.assinar_funcionario_a_projeto(funcionario, projeto)
        with self.assertRaises(ValueError):
            projeto.criar_ocorrencia(
                tipo="invalido",
                prioridade=PrioridadeOcorrencia.MEDIA,
                resumo="Resumo",
                responsavel=funcionario.id,
            )

    # Teste 18
    def test_criar_ocorrencia_prioridade_invalido(self):
        projeto = self.empresa.criar_projeto(nome="Projeto bala")
        funcionario = self.empresa.criar_funcionario(nome="Ana")
        self.empresa.assinar_funcionario_a_projeto(funcionario, projeto)
        with self.assertRaises(ValueError):
            projeto.criar_ocorrencia(
                tipo=TipoOcorrencia.BUG,
                prioridade="invalido",
                resumo="Resumo",
                responsavel=funcionario.id,
            )

    # Teste 19
    def test_criar_ocorrencia_resumo_invalido(self):
        projeto = self.empresa.criar_projeto(nome="Algum projeto")
        funcionario = self.empresa.criar_funcionario(nome="Joaquim")
        self.empresa.assinar_funcionario_a_projeto(funcionario, projeto)
        with self.assertRaises(ValueError):
            projeto.criar_ocorrencia(
                tipo=TipoOcorrencia.BUG,
                prioridade=PrioridadeOcorrencia.MEDIA,
                resumo="",
                responsavel=funcionario.id,
            )

    # Teste 20
    def test_criar_ocorrencia_responsavel_invalido(self):
        projeto = self.empresa.criar_projeto(nome="Piloto")
        funcionario = self.empresa.criar_funcionario(nome="Carol")
        self.empresa.assinar_funcionario_a_projeto(funcionario, projeto)
        with self.assertRaises(ValueError):
            projeto.criar_ocorrencia(
                tipo=TipoOcorrencia.BUG,
                prioridade=PrioridadeOcorrencia.MEDIA,
                resumo="Resumo",
                responsavel=9999,
            )

    # Teste 21
    def test_mudar_responsavel_de_ocorrencia_aberta(self):
        projeto = self.empresa.criar_projeto(nome="Projeto 21")
        funcionario_alice = self.empresa.criar_funcionario(nome="Alice")
        funcionario_bob = self.empresa.criar_funcionario(nome="Bob")
        self.empresa.assinar_funcionario_a_projeto(funcionario_alice, projeto)
        self.empresa.assinar_funcionario_a_projeto(funcionario_bob, projeto)
        ocorrencia = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.BUG,
            prioridade=PrioridadeOcorrencia.MEDIA,
            resumo="Bug aberto",
            responsavel=funcionario_alice.id,
        )
        ocorrencia.mudar_responsavel(funcionario_bob.id)
        self.assertEqual(ocorrencia.responsavel, funcionario_bob.id)

    # Teste 22
    def test_mudar_responsavel_de_ocorrencia_fechada(self):
        projeto = self.empresa.criar_projeto(nome="Projeto 22")
        funcionario_carlos = self.empresa.criar_funcionario(nome="Carlos")
        funcionario_diana = self.empresa.criar_funcionario(nome="Diana")
        self.empresa.assinar_funcionario_a_projeto(funcionario_carlos, projeto)
        self.empresa.assinar_funcionario_a_projeto(funcionario_diana, projeto)
        ocorrencia = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.BUG,
            prioridade=PrioridadeOcorrencia.MEDIA,
            resumo="Bug fechado",
            responsavel=funcionario_carlos.id,
        )
        ocorrencia.fechar()
        with self.assertRaises(ValueError):
            ocorrencia.mudar_responsavel(funcionario_diana.id)

    # Teste 23
    def test_modificar_prioridade_de_ocorrencia_aberta(self):
        projeto = self.empresa.criar_projeto(nome="Projeto 23")
        funcionario_eva = self.empresa.criar_funcionario(nome="Eva")
        self.empresa.assinar_funcionario_a_projeto(funcionario_eva, projeto)
        ocorrencia = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.TAREFA,
            prioridade=PrioridadeOcorrencia.BAIXA,
            resumo="Tarefa aberta",
            responsavel=funcionario_eva.id,
        )
        ocorrencia.modificar_prioridade(PrioridadeOcorrencia.ALTA)
        self.assertEqual(ocorrencia.prioridade, PrioridadeOcorrencia.ALTA)

    # Teste 24
    def test_modificar_prioridade_de_ocorrencia_fechada(self):
        projeto = self.empresa.criar_projeto(nome="Projeto 24")
        funcionario_fred = self.empresa.criar_funcionario(nome="Fred")
        self.empresa.assinar_funcionario_a_projeto(funcionario_fred, projeto)
        ocorrencia = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.TAREFA,
            prioridade=PrioridadeOcorrencia.BAIXA,
            resumo="Tarefa fechada",
            responsavel=funcionario_fred.id,
        )
        ocorrencia.fechar()
        with self.assertRaises(ValueError):
            ocorrencia.modificar_prioridade(PrioridadeOcorrencia.ALTA)

    # Teste 25
    def test_fechar_ocorrencia_aberta(self):
        projeto = self.empresa.criar_projeto(nome="Projeto 25")
        funcionario_gabi = self.empresa.criar_funcionario(nome="Gabi")
        self.empresa.assinar_funcionario_a_projeto(funcionario_gabi, projeto)
        ocorrencia = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.BUG,
            prioridade=PrioridadeOcorrencia.ALTA,
            resumo="Bug para fechar",
            responsavel=funcionario_gabi.id,
        )
        ocorrencia.fechar()
        self.assertFalse(ocorrencia.estado)

    # Teste 26
    def test_fechar_ocorrencia_fechada(self):
        projeto = self.empresa.criar_projeto(nome="Projeto 26")
        funcionario_hugo = self.empresa.criar_funcionario(nome="Hugo")
        self.empresa.assinar_funcionario_a_projeto(funcionario_hugo, projeto)
        ocorrencia = projeto.criar_ocorrencia(
            tipo=TipoOcorrencia.BUG,
            prioridade=PrioridadeOcorrencia.ALTA,
            resumo="Bug ja fechado",
            responsavel=funcionario_hugo.id,
        )
        ocorrencia.fechar()
        with self.assertRaises(ValueError):
            ocorrencia.fechar()

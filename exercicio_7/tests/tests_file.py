import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

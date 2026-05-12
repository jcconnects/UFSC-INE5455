import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.empresa import Empresa

class Test(unittest.TestCase):

    # Teste 01
    def test_criar_empresa(self):
        empresa = Empresa(nome="WEG")
        self.assertIsInstance(empresa, Empresa)
        self.assertEqual(empresa.nome, "WEG")
    
    # Teste 02
    def test_incluir_um_funcionario(self):
        empresa = Empresa(nome="WEG")
        empresa.incluir_funcionario("João")
        self.assertEqual(len(empresa.funcionarios), 1)
        self.assertEqual(empresa.funcionarios[0], "João")

    # Teste 03
    def test_incluir_dois_funcionarios(self):
        empresa = Empresa(nome="WEG")
        empresa.incluir_funcionario("João")
        empresa.incluir_funcionario("Maria")
        self.assertEqual(len(empresa.funcionarios), 2)
        self.assertEqual(empresa.funcionarios[0], "João")
        self.assertEqual(empresa.funcionarios[1], "Maria")

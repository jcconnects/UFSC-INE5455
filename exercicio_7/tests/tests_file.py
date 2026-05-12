import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.empresa import Empresa
from src.funcionario import Funcionario

class Test(unittest.TestCase):

    # Teste 01
    def test_criar_empresa(self):
        empresa = Empresa(nome="WEG")
        self.assertIsInstance(empresa, Empresa)
        self.assertEqual(empresa.nome, "WEG")
    
    # Teste 02
    def test_incluir_um_funcionario(self):
        empresa = Empresa(nome="WEG")
        funcionario = Funcionario(id=1, nome="João")
        empresa.incluir_funcionario(funcionario)
        self.assertEqual(len(empresa.funcionarios), 1)
        self.assertEqual(empresa.funcionarios[0], funcionario)

    # Teste 03
    def test_incluir_dois_funcionarios(self):
        empresa = Empresa(nome="WEG")
        funcionario1 = Funcionario(id=1, nome="João")
        funcionario2 = Funcionario(id=2, nome="Maria")
        empresa.incluir_funcionario(funcionario1)
        empresa.incluir_funcionario(funcionario2)
        self.assertEqual(len(empresa.funcionarios), 2)
        self.assertEqual(empresa.funcionarios[0], funcionario1)
        self.assertEqual(empresa.funcionarios[1], funcionario2)

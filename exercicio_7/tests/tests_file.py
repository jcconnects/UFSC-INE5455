import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.empresa import Empresa

class Test(unittest.TestCase):

    # Teste 01
    def test_criar_empresa(self):
        empresa = Empresa(nome="WEG")
        self.assertEqual(type(empresa), type(Empresa))
        self.assertEqual(empresa.nome, "WEG")


from funcionario import Funcionario

class Empresa:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.funcionarios = []

    def criar_funcionario(self, nome):
        funcionario = Funcionario(id=len(self.funcionarios) + 1, nome=nome)
        self.funcionarios.append(funcionario)
        return funcionario


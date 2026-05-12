
from funcionario import Funcionario
from projeto import Projeto
class Empresa:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def criar_funcionario(self, nome):
        funcionario = Funcionario(id=len(self.funcionarios) + 1, nome=nome)
        self.funcionarios.append(funcionario)
        return funcionario

    def criar_projeto(self, nome):
        proneto = Projeto(id=len(self.projetos) + 1, nome=nome)
        self.projetos.append(proneto)


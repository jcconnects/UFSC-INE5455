
from funcionario import Funcionario
from projeto import Projeto
class Empresa:
    def __init__(self, nome) -> None:
        if not nome:
            raise ValueError("O nome da empresa não pode ser vazio.")
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def criar_funcionario(self, nome):
        funcionario = Funcionario(id=len(self.funcionarios) + 1, nome=nome)
        self.funcionarios.append(funcionario)
        return funcionario

    def criar_projeto(self, nome):
        if not nome:
            raise ValueError("O nome do projeto não pode ser vazio.")
        proneto = Projeto(id=len(self.projetos) + 1, nome=nome)
        self.projetos.append(proneto)


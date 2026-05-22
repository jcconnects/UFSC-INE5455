
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
        if not nome:
            raise ValueError("O nome do funcionário não pode ser vazio.")
        funcionario = Funcionario(id=len(self.funcionarios) + 1, nome=nome)
        self.funcionarios.append(funcionario)
        return funcionario

    def criar_projeto(self, nome):
        if not nome:
            raise ValueError("O nome do projeto não pode ser vazio.")
        projeto = Projeto(id=len(self.projetos) + 1, nome=nome)
        self.projetos.append(projeto)
        return projeto

    def assinar_funcionario_a_projeto(self, funcionario, projeto):
        funcionario = next((f for f in self.funcionarios if f.id == funcionario.id), None)
        projeto = next((p for p in self.projetos if p.id == projeto.id), None)
        
        if funcionario is None:
            raise ValueError("Funcionário não encontrado na empresa.")
        if projeto is None:
            raise ValueError("Projeto não encontrado na empresa.")
        if funcionario in projeto.funcionarios:
            raise ValueError("Funcionário já está associado ao projeto.")

        projeto.funcionarios.append(funcionario)
        funcionario.projetos.append(projeto)

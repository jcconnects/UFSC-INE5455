class Empresa:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.funcionarios = []

    def incluir_funcionario(self, nome):
        self.funcionarios.append(nome)

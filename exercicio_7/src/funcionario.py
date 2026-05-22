class Funcionario:
    def __init__(self, id, nome) -> None:
        self.id = id
        self.nome = nome
        self.projetos = []
        self.ocorrencias = []

    def ocorrencias_ativas(self):
        return [o for o in self.ocorrencias if o.estado]
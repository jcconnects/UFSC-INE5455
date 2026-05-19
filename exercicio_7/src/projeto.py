from src.ocorrencia import Ocorrencia


class Projeto:
    def __init__(self, id, nome) -> None:
        self.id = id
        self.nome = nome
        self.funcionarios = []
        self.ocorrencias = []
    
    def criar_ocorrencia(self, tipo, prioridade, resumo, responsavel):
        ocorrencia = Ocorrencia(
            id=len(self.ocorrencias) + 1,
            tipo=tipo,
            prioridade=prioridade,
            resumo=resumo,
            responsavel=responsavel,
            projeto=self.id
        )
        self.ocorrencias.append(ocorrencia)

        funcionario = next((f for f in self.funcionarios if f.id == responsavel), None)
        funcionario.ocorrencias.append(ocorrencia)

        return ocorrencia

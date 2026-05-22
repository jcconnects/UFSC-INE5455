from src.ocorrencia import Ocorrencia, PrioridadeOcorrencia, TipoOcorrencia


class Projeto:
    def __init__(self, id, nome) -> None:
        self.id = id
        self.nome = nome
        self.funcionarios = []
        self.ocorrencias = []
    
    def criar_ocorrencia(self, tipo, prioridade, resumo, responsavel):
        if tipo not in TipoOcorrencia:
            raise ValueError("Tipo de ocorrência inválido.")
        if prioridade not in PrioridadeOcorrencia:
            raise ValueError("Prioridade de ocorrência inválida.")
        if not resumo:
            raise ValueError("O resumo da ocorrência não pode ser vazio.")
        if responsavel not in self.funcionarios:
            raise ValueError("Funcionário responsável não está associado ao projeto.")
        if len(responsavel.ocorrencias_ativas()) >= 10:
            raise ValueError("O funcionário responsável já tem 10 ocorrências atribuídas.")

        ocorrencia = Ocorrencia(
            id=len(self.ocorrencias) + 1,
            tipo=tipo,
            prioridade=prioridade,
            resumo=resumo,
            responsavel=responsavel,
            projeto=self
        )
        self.ocorrencias.append(ocorrencia)

        funcionario = next((f for f in self.funcionarios if f == responsavel), None)
        funcionario.ocorrencias.append(ocorrencia)

        return ocorrencia

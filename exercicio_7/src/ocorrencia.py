from enum import Enum


class TipoOcorrencia(Enum):
    TAREFA = 0
    BUG = 1
    REFATORACAO = 2


class PrioridadeOcorrencia(Enum):
    BAIXA = 0
    MEDIA = 1
    ALTA = 2


class Ocorrencia:
    def __init__(self, id, tipo, prioridade, resumo, responsavel, projeto) -> None:
        self.id = id
        self.tipo = tipo
        self.prioridade = prioridade
        self.resumo = resumo
        self.responsavel = responsavel
        self.projeto = projeto
        self.estado = True  # Aberta por padrão

    def fechar(self):
        if not self.estado:
            raise ValueError("Ocorrência já está fechada.")
        self.estado = False

    def mudar_responsavel(self, novo_responsavel):
        if not self.estado:
            raise ValueError("Não é possível mudar responsável de ocorrência fechada.")
        if novo_responsavel is None:
            raise ValueError("Novo responsável não pode ser nulo.")
        if len(novo_responsavel.ocorrencias_ativas()) >= 10:
            raise ValueError("O novo responsável já tem 10 ocorrências atribuídas.")
        if novo_responsavel not in self.projeto.funcionarios:
            raise ValueError(
                "Novo responsável não está associado ao projeto da ocorrência."
            )

        self.responsavel.ocorrencias.remove(self)
        self.responsavel = novo_responsavel
        novo_responsavel.ocorrencias.append(self)

    def modificar_prioridade(self, nova_prioridade):
        if not self.estado:
            raise ValueError(
                "Não é possível modificar prioridade de ocorrência fechada."
            )
        self.prioridade = nova_prioridade

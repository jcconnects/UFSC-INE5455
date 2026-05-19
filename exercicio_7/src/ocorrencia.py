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
        self.estado = True       # Aberta por padrão

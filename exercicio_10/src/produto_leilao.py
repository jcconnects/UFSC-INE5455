from produto import Produto
from lance import Lance
from usuario import Usuario

# TODO - atualizar a data utilizando o datetime

class ProdutoLeilao(Produto):
    def __init__(self, nome, descricao, valor_lance_minimo, leiloador):
        super().__init__(nome, descricao)
        self.__valor_lance_minimo = valor_lance_minimo
        self.__leiloador = leiloador
        self.__lances_efetuados = []
        self.__data_limite = 0
        self.__comprador = ''

    @property
    def data_limite(self):
        return self.__data_limite

    @data_limite.setter
    def data_limite(self, data_limite):
        self.__data_limite = data_limite

    @property
    def valor_lance_minimo(self):
        return self.__valor_lance_minimo

    @property
    def lances_efetuados(self):
        return self.__lances_efetuados

    def adiciona_lance(self, lance):
        self.__lances_efetuados.append(lance)

    def data_do_produto_expirou(self, data_hoje):
        return data_hoje > self.__data_limite

    @property
    def leiloador(self):
        return self.__leiloador

    @leiloador.setter
    def leiloador(self, leiloador):
        self.__leiloador = leiloador

    @property
    def comprador(self):
        return self.__comprador

    @comprador.setter
    def comprador(self, comprador):
        self.__comprador = comprador

    def verifica_lances_efetuados_por_um_usuario(self, cpf):
        retorno_de_lances = []
        for lance in self.__lances_efetuados:
            if cpf == lance.dono.cpf:
                retorno_de_lances.append(lance)
        return retorno_de_lances

    def get_valor_ultimo_lance(self):
        try:
            ultimo_lance = self.__lances_efetuados[len(self.__lances_efetuados)-1]
            return ultimo_lance.valor
        except Exception:
            return 0.0

    def get_lance_mais_recente(self):
        try:
            return self.__lances_efetuados[len(self.__lances_efetuados)-1]
        except Exception:
            return Lance(0.0, Usuario('', ''))

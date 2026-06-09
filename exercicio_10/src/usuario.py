class Usuario:
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = ''
        self.__email = ''
        self.__bens_ofertados = []
        self.__bens_comprados = []

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def get_bens_comprados(self):
        return self.__bens_comprados

    def adiciona_bem_comprado(self, produto_leilao):
        self.__bens_comprados.append(produto_leilao)

    def get_bens_ofertados(self):
        return self.__bens_ofertados

    def adiciona_bem_ofertado(self, produto_leilao):
        self.__bens_ofertados.append(produto_leilao)

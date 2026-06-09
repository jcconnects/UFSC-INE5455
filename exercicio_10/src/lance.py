class Lance:
    def __init__(self, valor, dono):
        self.__valor = valor
        self.__dono = dono
        self.__produto = None

    @property
    def valor(self):
        return self.__valor

    @property
    def dono(self):
        return self.__dono

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto):
        self.__produto = produto

    def __str__(self):
        return 'Lance no produto:  ' + self.__produto.nome

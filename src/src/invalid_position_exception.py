class InvalidPositionException(Exception):

    def __init__(self):
        self.message = 'Posicao invalida.'
        # super().__init__(self.message)

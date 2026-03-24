from enum import Enum


class Moeda(Enum):

    BRL = ("R$", 100)
    USD = ("$",  100)
    CHF = ("Fr", 100)

    def simbolo(self):
        return self.value[0]

    def base_fracionaria(self):
        return self.value[1]



class Dinheiro:

    def __init__(self, moeda : Moeda, inteiro : int, fracionado : int):
        if inteiro >= 0 and fracionado >= 0:
            self.__moeda = moeda
            self.__inteiro = inteiro
            self.__fracionado = fracionado
            self.__normalizar()
        else:
            raise ValueError()

    @property
    def moeda(self) -> Moeda :
        return self.__moeda

    @property
    def inteiro(self):
        return self.__inteiro

    @property
    def fracionado(self):
        return self.__fracionado

    def __normalizar(self):
        soma = self.obter_quantia_em_escala()
        base_fracionaria = self.moeda.base_fracionaria()
        self.__inteiro = (soma - soma % base_fracionaria) / base_fracionaria
        self.__fracionado = soma % base_fracionaria

    def obter_quantia_em_escala(self):
        return abs(self.__inteiro) * self.__moeda.base_fracionaria() + abs(self.__fracionado)

    def zero(self):
        return self.inteiro == 0 and self.fracionado == 0

    def formatar_sem_moeda(self):
        return '{0},{1:02d}'.format(int(self.inteiro), int(self.fracionado))

    def formatar_com_moeda(self):
        return '{0},{1:02d} {2}'.format(int(self.inteiro), int(self.fracionado), self.moeda.name)

    def formatado(self):
        if self.zero():
            return self.formatar_sem_moeda()
        else:
            return self.formatar_com_moeda()

    def positivo(self):
        return ValorMonetario(self.moeda).somar(self)

    def negativo(self):
        return ValorMonetario(self.moeda).subtrair(self)

    def __eq__(self, other):
        if isinstance(other, Dinheiro):
            mesma_moeda = self.moeda == other.moeda
            mesmo_valor = (self.inteiro == other.inteiro) and (self.fracionado == other.fracionado)
            return self.zero() or (mesmo_valor and mesma_moeda)
        return super == other

    def __str__(self):
        return self.formatado()




class ValorMonetario:

    def __init__(self, moeda, valor = 0):
        self.__moeda = moeda
        self.__sinal = 1 if valor >= 0 else -1

        valor = abs(valor) # ACRESCENTEI

        self.__quantia = Dinheiro(moeda, 0, valor)

    def validar_moeda(self, quantia_somada):
        if self.__moeda != quantia_somada.moeda:
            raise Exception("moedas incompativeis")

    def somar(self, quantia_somada):
        self.validar_moeda(quantia_somada)
        valor = self.__quantia.obter_quantia_em_escala() * self.__sinal + quantia_somada.obter_quantia_em_escala()
        return ValorMonetario(self.__moeda, valor)

    def subtrair(self, quantia_subtraida):
        self.validar_moeda(quantia_subtraida)
        valor = self.__quantia.obter_quantia_em_escala() * self.__sinal - quantia_subtraida.obter_quantia_em_escala()
        return ValorMonetario(self.__moeda, valor)

    def obter_quantia(self):
        return self.__quantia

    def negativo(self):
        return self.__sinal < 0

    def zero(self):
        return self.__quantia.obter_quantia_em_escala() == 0

    def formatado(self):
        if self.zero():
            return self.formatar_sem_sinal()
        else:
            return self.formatar_com_sinal()

    def formatar_sem_sinal(self):
        return self.__quantia.formatado()

    def formatar_com_sinal(self):
        if (self.negativo()):
            return self.formatar_negativo()
        else:
            return self.formatar_positivo()

    def formatar_positivo(self):
        return "+" + self.__quantia.formatado()

    def formatar_negativo(self):
        return "-" + self.__quantia.formatado()

    def __eq__(self, other):
        if isinstance(other, ValorMonetario):
            iguais_zero = self.zero() and other.zero()
            iguais_com_mesma_moeda = self.__sinal.__eq__(other.__sinal) and \
                                     self.__quantia.__eq__(other.__quantia) and \
                                     self.__moeda.__eq__(other.__moeda)
            return iguais_zero or iguais_com_mesma_moeda
        return super == other

    def __str__(self):
        return self.formatado()


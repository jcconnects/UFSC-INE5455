from usuario import Usuario
from produto_leilao import ProdutoLeilao
from lance import Lance

class MercadoLeilao:
    def __init__(self):
        self.__usuarios = {}
        self.__produtos_em_leilao = []
        self.__produtos_vendidos = []
        self.__produtos_vencidos_e_nao_vendidos = []

    # TODO - atualizar a data utilizando o datetime


    # USUARIOS

    def existe_usuario(self, cpf):
        return self.__usuarios.get(cpf) != None

    def __remove_caracteres(self, str_cpf):
        for caracter in str_cpf:
            if caracter not in '0123456789':
                str_cpf = str_cpf.replace(caracter, '')
        return str_cpf

    def __calculo_com_cpf(self, cpf):
        dig_gerado = 0
        mult = len(cpf) + 1
        for caracter in cpf:
            dig_gerado += int(caracter) * mult
            mult -= 1
        if dig_gerado%11 < 2:
            dig_gerado = 0
        else:
            dig_gerado = 11 - dig_gerado % 11
        return str(dig_gerado)

    def is_cpf(self, str_cpf):
        if str_cpf == None:
            return False
        else:
            cpf = self.__remove_caracteres(str_cpf)
            if len(cpf) != 11:
                return False
            cpf_gerado = cpf[0:9]
            cpf_gerado = cpf_gerado + self.__calculo_com_cpf(cpf_gerado)
            cpf_gerado = cpf_gerado + self.__calculo_com_cpf(cpf_gerado)
            if cpf_gerado != cpf:
                return False
            else:
                return True

    def cadastra_usuario(self, nome, endereco, email, cpf):
        if self.existe_usuario(cpf):
            raise Exception('O usuario ja existe.')
        elif not self.is_cpf(cpf):
            raise Exception('CPF invalido: ' + cpf)
        else:
            usuario = Usuario(cpf, nome)
            usuario.endereco = endereco
            usuario.email = email
            self.__usuarios.update({cpf : usuario})

    def get_usuarios_cadastrados(self):
        lista_usuarios_cadastrados = self.__usuarios.copy()
        return lista_usuarios_cadastrados

    def get_usuario_por(self, cpf):
        usuario = self.__usuarios.get(cpf)
        if usuario == None:
            raise Exception("O usuario nao esta cadastrado.")
        return usuario


# PRODUTOS

    def __existe_em_produtos_em_leilao(self, nome):
        for produto in self.__produtos_em_leilao:
            if produto.nome.casefold() == nome.casefold():
                return True
        return False

    def __existe_em_produtos_vendidos(self, nome):
        for produto in self.__produtos_vendidos:
            if produto.nome.casefold() == nome.casefold():
                return True
        return False

    def __existe_em_produtos_vencidos_e_nao_vendidos(self, nome):
        for produto in self.__produtos_vencidos_e_nao_vendidos:
            if produto.nome.casefold() == nome.casefold():
                return True
        return False

    def existe_produto(self, nome):
        return self.__existe_em_produtos_em_leilao(nome) or self.__existe_em_produtos_vendidos(nome) \
            or self.__existe_em_produtos_vencidos_e_nao_vendidos(nome)

    def cadastra_produto(self, nome, descricao, lance_minimo, cpf_leiloador, data_limite):
        if not self.existe_produto(nome) and self.existe_usuario(cpf_leiloador):
            leiloador = self.__usuarios.get(cpf_leiloador)
            produto = ProdutoLeilao(nome, descricao, lance_minimo, leiloador)
            produto.data_limite = data_limite
            self.__produtos_em_leilao.append(produto)
            leiloador.adiciona_bem_ofertado(produto)
        else:
            raise Exception("O produto ja existe ou o leiloador nao esta cadastrado.")

    def __atualiza_lista_de_produtos(self, data_hoje):
        lista_para_remover = []
        for produto in self.__produtos_em_leilao:
            quantidade_lances = len(produto.lances_efetuados)
            if produto.data_do_produto_expirou(data_hoje) and quantidade_lances > 0:
                self.__produtos_vendidos.append(produto)
                cpf_dono_do_lance = produto.get_lance_mais_recente().dono.cpf
                comprador = self.__usuarios.get(cpf_dono_do_lance)
                comprador.adiciona_bem_comprado(produto)
                produto.comprador = comprador
                lista_para_remover.append(produto)
            elif produto.data_do_produto_expirou(data_hoje) and quantidade_lances == 0:
                self.__produtos_vencidos_e_nao_vendidos.append(produto)
                lista_para_remover.append(produto)
        for produto in lista_para_remover:
            self.__produtos_em_leilao.remove(produto)

    def get_produtos_em_leilao(self, data_hoje):
        self.__atualiza_lista_de_produtos(data_hoje)
        lista_produtos_em_leilao = self.__produtos_em_leilao.copy()
        return lista_produtos_em_leilao

    def get_produtos_vencidos_e_nao_vendidos(self, data_hoje):
        self.__atualiza_lista_de_produtos(data_hoje)
        lista_produtos_vencidos = self.__produtos_vencidos_e_nao_vendidos.copy()
        return lista_produtos_vencidos

    def get_produtos_vendidos(self, data_hoje):
        self.__atualiza_lista_de_produtos(data_hoje)
        lista_produtos_vendidos = self.__produtos_vendidos.copy()
        return lista_produtos_vendidos


# LANCES

    def __pesquisa_indice_produto_em_leilao_via_nome(self, nome):
        tamanho_lista = len(self.__produtos_em_leilao)
        for indice in range(tamanho_lista):
            if self.__produtos_em_leilao[indice].nome.casefold() == nome.casefold():
                return indice
        raise Exception("Nao existe produto cadastrado com esse nome.")

    def da_lance(self, nome_produto, cpf_comprador, valor_lance, data_hoje):
        self.__atualiza_lista_de_produtos(data_hoje)
        comprador = self.get_usuario_por(cpf_comprador)
        lance = Lance(valor_lance, comprador)
        produto = self.__produtos_em_leilao[self.__pesquisa_indice_produto_em_leilao_via_nome(nome_produto)]
        valor_lance_minimo = produto.valor_lance_minimo
        valor_lance_atual = produto.get_valor_ultimo_lance()
        if self.existe_usuario(cpf_comprador) and valor_lance >= valor_lance_minimo and valor_lance > valor_lance_atual:
            produto.adiciona_lance(lance)
            lance.produto = produto
        else:
            raise Exception("O valor do lance eh inferior ao necessario ou o comprador nao esta cadastrado.")

    def __retorna_todos_lances_efetuados_em_produtos_em_leilao(self):
        lista_lances = []
        for produto in self.__produtos_em_leilao:
            lances = produto.lances_efetuados
            for lance in lances:
                lista_lances.append(lance)
        return lista_lances

    def __retorna_todos_lances_efetuados_em_produtos_vendidos(self):
        lista_lances = []
        for produto in self.__produtos_vendidos:
            lances = produto.lances_efetuados
            for lance in lances:
                lista_lances.append(lance)
        return lista_lances

    def retorna_todos_os_lances_efetuados(self):
        lista_com_todos_lances = self.__retorna_todos_lances_efetuados_em_produtos_em_leilao() + \
                                 self.__retorna_todos_lances_efetuados_em_produtos_vendidos()
        return lista_com_todos_lances

    def __retorna_lances_de_um_usuario_em_produtos_ainda_em_leilao(self, cpf):
        lista_lances = []
        for produto in self.__produtos_em_leilao:
            lista_lances += produto.verifica_lances_efetuados_por_um_usuario(cpf)
        return lista_lances

    def __retorna_lances_de_um_usuario_em_produtos_vendidos(self, cpf):
        lista_lances = []
        for produto in self.__produtos_vendidos:
            lista_lances += produto.verifica_lances_efetuados_por_um_usuario(cpf)
        return lista_lances

    def retorna_lances_de_um_usuario(self, cpf):
        if not self.existe_usuario(cpf):
            raise Exception("O usuario nao esta cadastrado.")
        lista_lances = self.__retorna_lances_de_um_usuario_em_produtos_ainda_em_leilao(cpf) + \
                       self.__retorna_lances_de_um_usuario_em_produtos_vendidos(cpf)
        return lista_lances

    def __retorna_produtos_em_leilao_por_um_usuario(self, cpf):
        lista_produtos = []
        for produto in self.__produtos_em_leilao:
            if produto.leiloador.cpf == cpf:
                lista_produtos.append(produto)
        return lista_produtos

    def __retorna_produtos_vendidos_por_um_usuario(self, cpf):
        lista_produtos = []
        for produto in self.__produtos_vendidos:
            if produto.leiloador.cpf == cpf:
                lista_produtos.append(produto)
        return lista_produtos

    def __retorna_produtos_vencidos_mas_nao_vendidos_por_usuario(self, cpf):
        lista_produtos = []
        for produto in self.__produtos_vencidos_e_nao_vendidos:
            if produto.leiloador.cpf == cpf:
                lista_produtos.append(produto)
        return lista_produtos

    def retorna_produtos_de_um_leiloador(self, cpf, data_hoje):
        self.__atualiza_lista_de_produtos(data_hoje)
        if not self.existe_usuario(cpf):
            raise Exception("O usuario nao esta cadastrado.")
        return self.__retorna_produtos_em_leilao_por_um_usuario(cpf) + \
            self.__retorna_produtos_vendidos_por_um_usuario(cpf) + \
            self.__retorna_produtos_vencidos_mas_nao_vendidos_por_usuario(cpf)

    def __deu_lance_no_produto(self, cpf, produto_leilao):
        lances = self.retorna_todos_os_lances_efetuados()
        for lance in lances:
            if lance.dono.cpf.casefold() == cpf.casefold():
                return True
        return False

    def __get_produtos_em_leilao_que_deu_lance(self, cpf):
        lista_produtos = []
        for produto in self.__produtos_em_leilao:
            if self.__deu_lance_no_produto(cpf, produto):
                lista_produtos.append(produto)
        return lista_produtos

    def __get_produtos_vendidos_que_deu_lance(self, cpf):
        lista_produtos = []
        for produto in self.__produtos_vendidos:
            if self.__deu_lance_no_produto(cpf, produto):
                lista_produtos.append(produto)
        return lista_produtos

    def get_produtos_que_deu_lance(self, cpf, data_hoje):
        self.__atualiza_lista_de_produtos(data_hoje)
        if not self.existe_usuario(cpf):
            raise Exception("O usuario nao esta cadastrado.")
        return self.__get_produtos_em_leilao_que_deu_lance(cpf) + self.__get_produtos_vendidos_que_deu_lance(cpf)

    def possui_usuario(self):
        return len(self.__usuarios) != 0

    def possui_produto(self):
        if len(self.__produtos_em_leilao) == 0 and \
            len(self.__produtos_vendidos) == 0 and \
            len(self.__produtos_vencidos_e_nao_vendidos) == 0:
            return False
        else:
            return True

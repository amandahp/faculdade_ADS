# busca metodos e atributos da classe mro

class TV:                                                   #classe # noqa
    def __init__(self, tela, resolucao, fabricante, preco): #funcao # noqa
        self.tela = tela
        self.resolucao = resolucao
        self.fabricante = fabricante
        self.__preco = preco
        self.fotos = []
        self.descricao = f'TV {resolucao} {tela}"  - {fabricante}'

    def atualizar_preco(self, novo_preco):
        self.__preco = novo_preco

    def editar_fotos(self):
        pass

    def editar_descricao(self):
        pass

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco


print(TV.mro())

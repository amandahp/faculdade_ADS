# Getter e setter
# Getter: abrir atributo para leitura
# Setter:  abrir o atributo para escrita

# from modulo_validacao import valida_autorizacao

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

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        # senha = input("Digite a senha de autorizacao: ")
        # if not valida_autorizacao(senha):
        # return
        self.__preco = novo_preco


tv_1 = TV(43, "FullHD", 'Samsung', 2400)
tv_2 = TV(50, "4K", "LG", 3200)

print("fim")


print(f'Preço antigo: R$ {tv_1.get_preco():.2f}')
tv_1.set_preco(2160)
print(f'Preço novo: R$ {tv_1.get_preco():.2f}')

class TV:
    def __init__(self):
        self.tela = 43
        self.resolucao = "Full HD"


tv_1 = TV()
tv_2 = TV()
print("fim")


# id: retorna o numero de identificacao criado na memoria
print(id(tv_1))
print(id(tv_2))

# self
# Recebe uma copia da referencia para o objeto a partir do qual e chamado


class TV2:
    def __init__(self):
        self.tela = 56
        self.resolucao = "FullHD"
        self.id = id(self)


tv_3 = TV2()
tv_4 = TV2()
print(f'ID de tv_1: {id(tv_3)}')
print(f'ID de tv_4: {id(tv_4)}')

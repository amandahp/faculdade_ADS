# def black_jack():
#     soma = 0
#     while soma < 21:
#         carta = int(input('Digite o valor da carta: '))
#         soma += carta
#         if carta < 21 and soma < 21:
#             resposta = str(input('Deseja adicionar outra carta? '))
#             if resposta == 'Sim' or resposta == 'sim':
#                 carta
#             else:
#                 break
#     print(f'A soma das cartas é: {soma}')


# black_jack()


def black_jack():
    soma = 0
    while soma < 21:
        carta = int(input('Digite o valor da carta: '))
        soma += carta
        if soma < 21:
            resposta = str(input('Deseja adicionar outra carta? '))
            if resposta == 'Sim' or resposta == 'sim':
                continue
            else:
                break
    print(f'A soma das cartas é: {soma}')


black_jack()

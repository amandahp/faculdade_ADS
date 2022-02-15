# Modo de depuração do vscode funciona como 'prints'. Nesse modo selecionamos


# pontos de parada ao longo do código

def dobrar(x):
    return 2 * x


def triplicar(x):
    triplo = 3 * x
    return triplo


n1 = float(input('Digite um número:'))
dobro = dobrar(n1)
print(f'O dobro é: {dobro}')
print(f'O triplo é: {triplicar(n1)}')

# Em caso de duvida, ler capitulo 2.2 de POO
# Ler recomendacoes PEP 8
# Instalação dos pacotes de verificação das


# recomendacoes do PEP 8 > pacote flake8^5
# $ python3 -m pip install flake8
# python3 -m pip isntall pep8-naming
# ver capitulo 2.3 de POO

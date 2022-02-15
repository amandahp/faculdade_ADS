# Desempacotamento de sequências
# é uma forma de operador os itens de uma sequencia
# a diferentes variaveis

a, b = [1, 3]
print(a)
print(b)

# Lista

lista = [('a', 1), ('b', 2), ('c', 8)]

# for

for item in lista:
    print(f'{item} --> {item[0]}: {item[1]}')

# para acessar a letra e o numero, em cada item, precisamos
# usar os indices

for letra, numero in lista:
    print(f'{letra}:{numero}')

# Desempacotamento de uma funcao


def teste_desempacotamento(a, b, c):
    print(f'{a=}, {b=}, {c=}')


sequencia = 1, 5, 8
print(teste_desempacotamento(*sequencia))

# ver pq aparece none

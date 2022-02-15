# 1) Estruturas de seleção:
# em Python é feita com o comando if, seguido de uma
# condição.
# if <condicao>:
# <bloco de codigo>

# comparação: usar if not flag

# if e else
# if <condicao>:
# <bloco de codigo se verdadeiro>
# else:
# <bloco de codigo se falso>

# elif = contração dos comandos else + if
# tem como objetivo reduzir uma identeção excessiva

# if <condicao C1>:
# <bloco de código se verdadeiro>
# else:
# if <condicao C2>:
# <bloco de codigo se C1 verdadeiro e C2 falsa>
# else:
# <bloco se C1 e C2 falsas>

# =

# if <condicao C1>:
# <bloco de codigo se verdadeiro>
# elif <condicao c2>:
# <bloco de codigo se C1 verdadeiro e C2 falso>
# else:
# <bloco de codigo se C1 e C2 falsas>

# Exemplos

x = int(input('Por favor insira um valor inteiro: '))
print(f'Você digitou: {x}')

if x < 0:
    x = 0
    print('Valor inválido, alterado para zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Unitário')
else:
    print('Maior que um')


# 2) Estruturas de repetição: indefinidas e definidas

# Indefinidas:
# Dependemos da availiação de uma condição,
# dessa maneira, não sabemos quantas vezes a instrução
# sera executada.
# As estruturas de repetição indefinidas são feitas com
# o comando while
# while <condicao>:
# <bloco de codigo>

# é parecido com if, entretnato, após a execucao do bloco de
# codigo, o while ira reavaliar a condicao e o processo
# se repete, enquanto a condicao for True

soma = 0

while soma < 21:
    carta = int(input('Digite um valor da carta: '))
    soma += carta

print(f'Seu resultado é {soma}')

# Definidas
# são feitas com o comando for
# for <variavel> in <sequencia>:
# <bloco de codigo>

lista = ['a', 1, True, 3.5]
for valor in lista:
    print(f'valor: {valor}, do tipo: {type(valor)}')

print('----\nfim')

for i in range(7):
    print(i)
lista_2 = ['b', 3, False, 5.5]
for i in range(len(lista_2)):
    print(i, lista_2[i], type(lista_2[i]))

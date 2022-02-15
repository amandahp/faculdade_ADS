# Tuplas
# estruturas de dados lineares, ordenadas, heterogenas,
# no entanto, são imutáveis
# Em python as tuplas são definidas por um par de parenteses e virgula

tupla = (1, 10, 16)
tupla_vazia = ()

# Para definir uma tupla com um único elemento, devemos colocar uma ,

e_uma_tupla = (1,)
nao_e_uma_tupla = (1)

# Ao separamos elementos com virgula, tbm criaremos um tupla
nova_tupla = 1, 5, 9
print(nova_tupla)

# Métodos: somente metodos que n modificam a tupla
# acessar valor da tupla
print(nova_tupla[1])

# concatenar duas tuplas
print(tupla + nova_tupla)

# metodos de tupla, servem para strings
value = 'cavalo'
print(value[3])

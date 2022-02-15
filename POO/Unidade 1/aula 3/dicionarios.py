# Dicionarios
# Estrutura de mapeamento, ou seja, cria uma associacao entre dois objetos

dicionario_vazio = {}
notas = {'Jack': 8.3, 'Anna': 4.5, 'Renan': 0}

lista_notas = [('Jack', 8.3), ('Anna', 4.5), ('Renan', 0)]
notas_2 = dict(lista_notas)

if notas_2 == notas:
    print('Iguais')
else:
    print('Diferentes')

# as chaves em um dicionario precisam ser unicas
# exemplo

# exemplon = {'Joana': 3.4, 'Lucia': 6.7, 'Joana': 6.8}
# print(exemplon)

# o valor do segundo, sobreescreve o valor do primeiro

# Acessar o valor de um dicionario

# print(exemplon['Joana'])
# # sem a chave no dicionario
# print(exemplon('Amanda'))


# Acessando o valor por get
# dicionario.get(key, default=None)

notas_3 = {'Jack': 8.3, 'Anna': 4.5, 'Renan': 0}
print(notas_3.get('Maria'))
print(notas_3.get('Maria', 'Nao ha correspondecia'))

# Inserir um valor em um dicionario
# podemos atribuir o valor diretamente a uma chave

notas_3['Amanda'] = 10.0
print(notas_3)

notas_3['Anna'] = 9.0
print(notas_3)

# Metodo update

inteiros = {}
inteiros.update({1: 'um', 2: 'dois'})
print(inteiros)

inteiros.update([(3, 'três'), (4, 'quatro')])
print(inteiros)

# Uniao de dicionarios
# utiliza-se caractere barra |
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
print(d1 | d2)

# Excluir um item de um dicionario

# del
del inteiros[2]
print(inteiros)

# .pop
print(inteiros.pop(9, 'Chave nao encontrada'))
print(inteiros)

# Operacoes pertencentes em um dicionario

print(5 not in inteiros)
print('Julia' in notas)

# Para acessar um elemento de uma lista,
# usamos um par de colchetes, com índice do elemento em questão

inteiros = [1, 10, 50]
print(inteiros[0])

diversos = ['Renan', 9, 50.9, True]
print(diversos[3])
print(diversos[-1])

# Substituir um item da lista
# Atribuir um elemento ao um elemento existente

compras = ['mamão', 'banana', 'aveia', 'leite', 'farinha']
print(compras)
compras[0] = 'melão'
print(compras)

# Inserir um item em uma dada posição
# Para inserir um novo item na lista, usamos o método insert
# lista.insert(indice, 'item')

compras.insert(1, 'pão')
print(compras)

# Remover um item da lista
# Existem três formas de remover um item da lista:
# 1 -> Comando del

del compras[-1]
print(compras)

# 2 -> método pop

compras.pop(3)
print(compras)

# se nenhum argumento for passado no método pop, ele remove o ultimo item
compras.pop()
print(compras)

# 3 -> método remove
# recebe um valor e faz a busca na lista, removendo o primeiro item que
# corresponde ao valor repassado

compras.remove('pão')
print(compras)


# Acrescentar um item ao final da lista
# método append, que recebe um objeto e adiciona ao final da lista

compras.append('bacon')
print(compras)

# exercicios

# 1)

compras.append(['sofá', 'luz', 'geladeira'])
print(compras)

# adiciona outro array dentro do array

# 2) extend

compras.extend(['sofá', 'luz', 'geladeira'])
print(compras)

# adiciona somente os intens da lista

# Concatenar duas listas

print(compras + inteiros)
# + concatenção = cria uma nova lista
# += adiciona os novos itens a lista principal, semelhante ao extend

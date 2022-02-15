# Operador de pertencimento pode ser usado em todos os
# tipos de sequencia

tupla = (1, 10, 6)
compras = ['banana', 'leite', 'aveia', 'pão']
texto = 'Olá mundo!'

print(1 in tupla)
print('banana' in compras)
print('m' in texto)

print(40 not in tupla)
print('M' not in texto)
# python case_sensitive
print('arroz' not in compras)

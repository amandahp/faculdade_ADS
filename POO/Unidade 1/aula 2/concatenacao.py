# Strings literais formatadas ou f-strings

texto = f'4 + 7 = {4 + 7}, certo?'
print(texto)

salario = 3500.0
print(f'20% a mais em R$ {salario} dará R$ {salario*1.2}')

# Para formatar um dado tipo float, podemos usar o seguinte padrāo de

# formataçāo: f'{<valor>:<colunas>.<decimais>f}'

pi = 3.14159265
print(f'{pi:f}')


# sem especificar a quantidade de casas decimais


print(f'{pi:.3f}')
# especifica a quantidade de casas decimais e realiza o arredondamento

# na última casa decimal


print(f'{pi:7.3f}')
# 7 colunas totais, 3 casas decimais

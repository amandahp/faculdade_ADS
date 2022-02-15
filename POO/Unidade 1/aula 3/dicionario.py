# Metodos especiais para iterar sobre um dicionario

notas = {'Jack': 3.0, 'Luana': 5.7, 'Renato': 8.0}

for chave in notas:
    print(chave, notas[chave])

# Metodo dict.keys().dict.values() e dict.items()

print(list(notas.keys()))
print(list(notas.values()))
print(list(notas.items()))

for nome, nota in notas.items():
    print(nome, nota)

dic = {
    "alimentos": {
        "pizzas": [ "margueritta", "mussarella",
                    "frango com catupiry", "portuguesa"],
        "bolos": ("floresta negra",
                  "red velvet",
                  "de laranja",
                  "dá vó"),
        "sobremesas": ["brigadeiros",
                       "cocada",
                       "sorvete"],
        "calorias": {
            "leite": 129, "fatia de pizza": 320,
            "agua": 0, "maça": 95
        }
    },
    "linguagens": [
        {"nome": "javascript", "criação": 1996,
         "paradigma": ["eventos", "funcional"]},
        {"nome": "python", "criação": 1991,
         "paradigma": ["orientada a objetos", "estruturada"]},
        {"nome":"haskell", "criação": 1990,
         "paradigma": ["funcional"]}
    ]
}

# #1. Quantas chaves tem o dicionario dic?
print("r1", len(dic))

# #2. dic['linguagens'] é uma tupla, um dicionario ou uma lista?
print("r2", type(dic['linguagens']))

# #3. Como eu faço para mostrar todos os bolos?
alimentos = dic['alimentos']
print("r3", alimentos['bolos'])

# #4. Qual é o tipo da lista de todos os bolos?
# Tupla
print("r4", type(dic['alimentos']['bolos']))

#5. O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("r5", dic["linguagens"][0]['criação'])

#6 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("r6", dic["linguagens"][2] == "haskell")

#7 O  que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("r7", dic["alimentos"]["pizzas"][2] == "mussarella")

#8 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("r8", 1996 in dic['linguagens'][0].values())

#9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("r9", "criação" in dic['linguagens'][0].keys())

#r10 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("r10", "pudim" in dic["alimentos"]["sobremesas"])

#10 Escreva uma função "mais velha" que
# recebe um dicionário como dic e
# retorna (isso é diferente de imprimir!) a linguagem de programação mais velha da nossa lista
def mais_velha(dic):
    lista_linguagens = dic['linguagens']
    ling_velha = lista_linguagens[0]
    for linguagem in lista_linguagens:
        if linguagem['criacao'] < ling_velha['criacao']:
            ling_velha = linguagem
    return ling_velha


#11 Escreva uma função que retorna uma lista (sem repetições) de paradigmas de linguagens de programação
def todos_paradigmas(dic):
    lista_linguagens = dic['linguagens']
    paradigmas = []
    for linguagem in lista_linguagens:
        paradigmas_da_linguagem = linguagem['paradigma']
        for p in paradigmas_da_linguagem:
            if p not in paradigmas:
                paradigmas.append(p)
    return paradigmas
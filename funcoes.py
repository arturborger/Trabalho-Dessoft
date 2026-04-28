import random

def rolar_dados(quantidade):
    dados = []
    for i in range(quantidade):
        dados.append(random.randint(1, 6))
    return dados

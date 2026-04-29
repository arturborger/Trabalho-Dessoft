import random

def rolar_dados(quantidade):
    dados = []
    for i in range(quantidade):
        dados.append(random.randint(1, 6))
    return dados
def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados.pop(dado_para_guardar)
    dados_no_estoque.append(dado)
    return [dados_rolados, dados_no_estoque]
def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque.pop(dado_para_remover)
    dados_rolados.append(dado)
    return [dados_rolados, dados_no_estoque]
def calcula_pontos_regra_simples(dados):
    pontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in dados:
        pontos[dado] += dado
    return pontos
def calcula_pontos_soma(dados):
    total = 0
    for dado in dados:
        total += dado
    return total
def calcula_pontos_sequencia_baixa(dados):
    sequencias = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]
    for sequencia in sequencias:
        encontrou = True
        for numero in sequencia:
            if numero not in dados:
                encontrou = False
        if encontrou:
            return 15
    return 0
def calcula_pontos_sequencia_alta(dados):
    sequencias = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6]
    ]
    for sequencia in sequencias:
        encontrou = True
        for numero in sequencia:
            if numero not in dados:
                encontrou = False
        if encontrou:
            return 30
    return 0
def calcula_pontos_full_house(dados):
    contagem = {}
    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1
    trinca = False
    par = False
    for valor in contagem.values():
        if valor == 3:
            trinca = True
        elif valor == 2:
            par = True
    if trinca and par:
        total = 0
        for dado in dados:
            total += dado
        return total
    return 0
def calcula_pontos_quadra(dados):
    for i in range(1, 7):
        total = 0
        for j in range(len(dados)):
            if dados[j] == i:
                total += 1
        if total >= 4:
            soma = 0
            for k in range(len(dados)):
                soma += dados[k]
            return soma
    return 0
def calcula_pontos_quina(dados):
    for i in range(1, 7):
        total = 0
        for j in range(len(dados)):
            if dados[j] == i:
                total += 1
        if total >= 5:
            return 50
    return 0
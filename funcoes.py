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
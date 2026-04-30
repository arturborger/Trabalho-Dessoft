from funcoes import *

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    jogada_feita = False

    while not jogada_feita:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        while True:
            opcao = input(">")
            if opcao in ("0", "1", "2", "3", "4"):
                break
            print("Opção inválida. Tente novamente.")

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input(">"))
            resultado = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input(">"))
            resultado = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            print("Digite a combinação desejada:")
            combinacao_valida = False
            while not combinacao_valida:
                categoria = input(">")
                todos = dados_rolados + dados_guardados

                if categoria in cartela['regra_avancada']:
                    if cartela['regra_avancada'][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(todos, categoria, cartela)
                        combinacao_valida = True
                        jogada_feita = True

                elif categoria in ["1", "2", "3", "4", "5", "6"]:
                    if cartela['regra_simples'][int(categoria)] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(todos, int(categoria), cartela)
                        combinacao_valida = True
                        jogada_feita = True

                else:
                    print("Combinação inválida. Tente novamente.")

pontuacao = 0
pontos_simples_total = 0

for i in range(1, 7):
    if cartela['regra_simples'][i] != -1:
        pontuacao += cartela['regra_simples'][i]
        pontos_simples_total += cartela['regra_simples'][i]

for chave in cartela['regra_avancada']:
    if cartela['regra_avancada'][chave] != -1:
        pontuacao += cartela['regra_avancada'][chave]

if pontos_simples_total >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")

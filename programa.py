import funcoes
import random
cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
dados_guardados = []
qnt_de_dados = 5
dados = []
rerrolar = 0
dados = funcoes.rolar_dados(qnt_de_dados)
funcoes.imprime_cartela(cartela_de_pontos)
i = 0
while i < 12:
    print(f"Dados rolados: {dados}")
    print(f"Dados guardados: {dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    ação = input()
    possibilidades = ['0', '1', '2', '3', '4']
    while ação not in possibilidades:
        print("Opção inválida. Tente novamente.")
        ação = input()
    if ação == '1':
        print("Digite o índice do dado a ser guardado (0 a 4):")
        guardar = int(input())
        qnt_de_dados = qnt_de_dados - 1
        dados_atu = funcoes.guardar_dado(dados, dados_guardados, guardar)
        dados_guardados = dados_atu[1]
        dados = dados_atu[0]
    elif ação == '2':
        print("Digite o índice do dado a ser removido (0 a 4):")
        remover = int(input())
        qnt_de_dados = qnt_de_dados + 1
        dados_atu = funcoes.remover_dado(dados, dados_guardados, remover)
        dados_guardados = dados_atu[1]
        dados = dados_atu[0]
    elif ação == '3':
        if rerrolar >= 2:
            print("Você já usou todas as rerrolagens.")
        else:
            dados = funcoes.rolar_dados(qnt_de_dados)
            rerrolar += 1
    elif ação == '4':
        funcoes.imprime_cartela(cartela_de_pontos)
    elif ação == '0':
        validacao_jogada = False
        print("Digite a combinação desejada:")
        todos_dados = []
        for j in range(len(dados)):
            todos_dados.append(dados[j])
        for w in range(len(dados_guardados)):
            todos_dados.append(dados_guardados[w])
        while validacao_jogada != True:
            jogada = input()
            lista = ["1", "2", "3", "4", "5", "6"]
            if jogada in lista:
                jogada = int(jogada)
            if jogada in cartela_de_pontos['regra_simples']:
                if cartela_de_pontos['regra_simples'][jogada] == -1:
                    pontos = funcoes.faz_jogada(todos_dados, jogada, cartela_de_pontos)
                    qnt_de_dados = 5
                    dados = funcoes.rolar_dados(qnt_de_dados)
                    dados_guardados = []
                    rerrolar = 0
                    i += 1
                    validacao_jogada = True
                else:
                    print("Essa combinação já foi utilizada.")
            elif jogada in cartela_de_pontos['regra_avancada']:
                if cartela_de_pontos['regra_avancada'][jogada] == -1:
                    pontos = funcoes.faz_jogada(todos_dados, jogada, cartela_de_pontos)
                    qnt_de_dados = 5
                    dados = funcoes.rolar_dados(qnt_de_dados)
                    dados_guardados = []
                    rerrolar = 0
                    i += 1
                    validacao_jogada = True
                else:
                    print("Essa combinação já foi utilizada.")
            else:
                print("Combinação inválida. Tente novamente.")  
pontuação_total_simples = 0
pontuação_total_avancado = 0
for regra, combinacoes in cartela_de_pontos.items():
    if regra == 'regra_simples':
        for combi, ponto in combinacoes.items():
            pontuação_total_simples += ponto
    elif regra == 'regra_avancada':
        for combi, ponto in combinacoes.items():
            pontuação_total_avancado += ponto
if pontuação_total_simples >= 63:
    pontuação_total_simples += 35
pontuação_total = pontuação_total_avancado + pontuação_total_simples
funcoes.imprime_cartela(cartela_de_pontos)
print(f"Pontuação total: {pontuação_total}")
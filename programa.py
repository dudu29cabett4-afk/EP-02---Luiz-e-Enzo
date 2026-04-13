import funcoes
import random
dados_guardados = []
qnt_de_dados = 5
dados = []
for i in range(qnt_de_dados):
    dados.append(random.randint(1,6))
for i in range(12):
    print(f"Dados rolados: {dados}")
    print(f"Dados guardados: {dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    ação = int(input())
    if ação == 1:
        print("Digite o índice do dado a ser guardado (0 a 4):")
        guardar = int(input())
        qnt_de_dados = qnt_de_dados - 1
        dados_atu = funcoes.guardar_dado(dados, dados_guardados, guardar)
        dados_guardados = dados_atu[1]
        dados = dados_atu[0]
    elif ação == 2:
        print("Digite o índice do dado a ser removido (0 a 4):")
        remover = int(input())
        qnt_de_dados = qnt_de_dados + 1
        dados_atu = funcoes.remover_dado(dados, dados_guardados, remover)
        dados_guardados = dados_atu[1]
        dados = dados_atu[0]
    elif ação == 3:
        print("Digite a combinação desejada:")
        

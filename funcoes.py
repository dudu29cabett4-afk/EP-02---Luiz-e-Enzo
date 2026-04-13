# Exercício 1

import random

def rolar_dados(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(1,6))
    return lista
# -------------------------------------------------------------
# Exercício 2

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    novos_dados = []
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            novos_dados.append(dados_rolados[i])
    resp = [novos_dados, dados_no_estoque]
    return resp

# -------------------------------------------------------------
# Exercício 3

def remover_dado(lista_dados_rolados, lista_dados_estoque, n_indice):
    novo_estoque = []
    lista = []
    for i in range(len(lista_dados_estoque)):
        if i == n_indice:
            lista_dados_rolados.append(lista_dados_estoque[i])
        else:
            novo_estoque.append(lista_dados_estoque[i])
    lista.append(lista_dados_rolados)
    lista.append(novo_estoque)
    return lista
# -------------------------------------------------------------
# Exercício 4
def calcula_pontos_regra_simples(lista_dados):
    pontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(len(lista_dados)):
        if lista_dados[i] == 1:
            pontos[1] += 1
        elif lista_dados[i] == 2:
            pontos[2] += 2
        elif lista_dados[i] == 3:
            pontos[3] += 3
        elif lista_dados[i] == 4:
            pontos[4] += 4
        elif lista_dados[i] == 5:
            pontos[5] += 5
        elif lista_dados[i] == 6:
            pontos[6] += 6
    return pontos

# -------------------------------------------------------------
# Exercício 5
def calcula_pontos_soma(lista_dados):
    soma = 0
    for i in range(len(lista_dados)):
        soma += lista_dados[i]
    return soma

# -------------------------------------------------------------
# Exercício 6
def calcula_pontos_sequencia_baixa(lista_dados):
    lista_dados = sorted(set(lista_dados))
    if len(lista_dados) < 4:
        return 0
    for i in range(len(lista_dados) - 3):
        sequencia = lista_dados[i:i+4]
        if sequencia == list(range(sequencia[0], sequencia[0] + 4)):
            return 15
    return 0

# -------------------------------------------------------------
# Exercício 7
def calcula_pontos_sequencia_alta(lista_dados):
    lista_dados = sorted(set(lista_dados))
    if len(lista_dados) < 5:
        return 0
    for i in range(len(lista_dados) - 4):
        sequencia = lista_dados[i:i+5]
        if sequencia == list(range(sequencia[0], sequencia[0] + 5)):
            return 30
    return 0
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
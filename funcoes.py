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
    lista = []
    dado_removido = lista_dados_estoque.pop(n_indice)
    lista_dados_rolados.append(dado_removido)
    lista.append(lista_dados_rodados)
    lista.append(lista_dados_estoque)
    return lista

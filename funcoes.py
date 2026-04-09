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
    validação = False
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    for i in range(len(dados_rolados)):
        if dados_rolados[i] != dados_rolados[dado_para_guardar] or validação == True:
            novos_dados.append(dados_rolados[i])
        else:
            validação = True
    resp = [novos_dados, dados_no_estoque]
    return resp
import pandas as pd

def mergesort(lista, inicio=0, fim=None, key=lambda x: x):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio, key)
        mergesort(lista, meio, fim, key)
        merge(lista, inicio, meio, fim, key)


def merge(lista, inicio, meio, fim, key):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0

    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1
        elif key(left[top_left]) <= key(right[top_right]):
            lista[k] = left[top_left]
            top_left += 1
        else:
            lista[k] = right[top_right]
            top_right += 1

dados = pd.read_csv('exoplanets_new.csv')
dados_colunas = dados.loc[:, ['pl_name', 'disc_year']]
lista_dados = list(zip(dados_colunas['pl_name'], dados_colunas['disc_year']))

mergesort(lista_dados, key=lambda x: x[1])

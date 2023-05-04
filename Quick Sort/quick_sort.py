import pandas as pd
import time
import sys
sys.setrecursionlimit(35000)

def quicksort(lista, start=0, end=None, key=lambda x: x):
    if end is None:
        end = len(lista) - 1

    while True:
        if end - start < 1:
            return

        p = partition(lista, start, end, key)

        if p - start < end - p:
            quicksort(lista, start, p - 1, key)
            start = p + 1
        else:
            quicksort(lista, p + 1, end, key)
            end = p - 1

def partition(lista, start, end, key):
    pivot = lista[end]
    i = start
    for j in range(start, end):
        if key(lista[j]) <= key(pivot):
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[end] = lista[end], lista[i]
    return i

df = pd.read_csv('exoplanets_new.csv')
dados_colunas = df.loc[:, ['pl_name', 'disc_year']]
lista_tuplas = list(zip(dados_colunas['pl_name'], dados_colunas['disc_year']))

t0 = time.perf_counter()
quicksort(lista_tuplas, key=lambda x: x[1]) 
t1 = time.perf_counter()
total_time = t1 - t0

print(total_time)

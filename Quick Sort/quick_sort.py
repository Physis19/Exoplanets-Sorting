import pandas as pd

def quicksort(lista, start = 0, end = None, key=lambda x: x):
    if end is None:
        end = len(lista) - 1

    if start < end:
        p = partition(lista, start, end, key)
        quicksort(lista, start, p-1, key)
        quicksort(lista, p+1, end, key)

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
dados_colunas = df.loc[0:996, ['pl_name', 'disc_year']]
lista_tuplas = list(zip(dados_colunas['pl_name'], dados_colunas['disc_year']))

quicksort(lista_tuplas, key=lambda x: x[1]) 

#df_ord = pd.DataFrame(lista_tuplas, columns=['Exoplanet Name', 'Discovered Year'])

#df_ord.to_csv('Ordered_data.csv', index=False)

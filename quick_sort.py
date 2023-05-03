import pandas as pd
import sys
sys.setrecursionlimit(1000)

def quicksort(lista, start = 0, end = None, depth = None):
	if end is None:
		end = len(lista) - 1
	if depth is None:
		depth = len(lista) * 2
	if start < end and depth > 0:
		p = partition(lista, start, end)
		quicksort(lista, start, p-1, depth - 1)
		quicksort(lista, p+1, end, depth + 1)

def partition(lista, start, end):
	pivot = lista[end]
	i = start
	for j in range(start, end):
		if lista[j] <= pivot:
			lista[j], lista[i] = lista[i], lista[j]
			i += 1
	lista[i], lista[end] = lista[end], lista[i]
	return i

dados = pd.read_csv('exoplanets_new.csv')
dados_colunas = dados.loc[:, ['pl_name', 'disc_year']]
lista_tuplas = list(zip(dados_colunas['pl_name'], dados_colunas['disc_year']))

original_list_size = len(lista_tuplas)

quicksort(lista_tuplas, 900)
qtd_add = original_list_size - len(lista_tuplas)

for i in range(qtd_add):
	lista_tuplas.append((None, None))

print(lista_tuplas)
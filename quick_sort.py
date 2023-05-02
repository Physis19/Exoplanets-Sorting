import pandas as pd

def quicksort(lista, inicio = 0, fim = None):
	if fim is None:
		fim = len(lista) - 1
	if inicio < fim:
		p = partition(lista, inicio, fim)
		quicksort(lista, inicio, p-1)
		quicksort(lista, p+1, fim)

def partition(lista, inicio, fim):
	pivot = lista[fim]
	i = inicio
	for j in range(inicio, fim):
		if lista[j] <= pivot:
			lista[j], lista[i] = lista[i], lista[j]
			i += 1
	lista[i], lista[fim] = lista[fim], lista[i]
	return i

'''
dados = pd.read_csv('exoplanets_new.csv')
dados_colunas = dados.loc[:, ['pl_name', 'disc_year']]
lista_tuplas = list(zip(dados_colunas['pl_name'], dados_colunas['disc_year']))
'''

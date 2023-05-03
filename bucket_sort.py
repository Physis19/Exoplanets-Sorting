import pandas as pd

dados = pd.read_csv('https://raw.githubusercontent.com/Physis19/Exoplanets-Sorting/main/exoplanets_new.csv')

colunas = dados.loc[:, ['pl_name', 'disc_year']]
lista_tuplas = list(zip(colunas['pl_name'], colunas['disc_year']))

def calculate_bucket():
    valorMax = max(lista_tuplas, key=lambda x: x[1])
    valorMin = min(lista_tuplas, key=lambda x: x[1])

    intervalo = 10

    num_bucket = int(((valorMax[1] - valorMin[1]) / intervalo) + 1)

    return num_bucket


def bucket_sort(array):
    valorInicial = 1990

    num_bucket = calculate_bucket()

    buckets = [[] for x in range(num_bucket)]

    for year in array:
        index = (year[1] - valorInicial) // 10
        buckets[index].append(year)


    for x, bucketList in enumerate(buckets):
        buckets[x] = sorted(bucketList, key=lambda x: x[1])
    
    sortedBuckets = []

    for bucket in buckets:
        sortedBuckets.extend(bucket)

    return sortedBuckets

print(bucket_sort(lista_tuplas))
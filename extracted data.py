import pandas as pd
import numpy as np

dados = pd.read_csv('exoplanets_new.csv', usecols=[6])
array_dados = dados.values
exoplanets_years = pd.DataFrame(array_dados, columns=['Years'])
exoplanets_years.to_csv('exoplanets_years.csv')
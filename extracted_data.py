import pandas as pd


dados = pd.read_csv(f'exoplanets_new.csv')
dados_colunas = dados.loc[:, ['pl_name', 'disc_year']]
lista_tuplas = list(zip(dados_colunas['pl_name'], dados_colunas['disc_year']))



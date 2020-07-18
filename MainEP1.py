# Descricao: Este codigo ira armazenar os locais distintos da pesquisa de origem-destino
# de Sao Paulo em estruturas de dados e computara quais os frequentadores de cada local


import pandas as pd
from classes.Local import Local
from classes.Frequentador import Frequentador
from datetime import datetime
import xlrd
start_execucao = datetime.now()

### INICIALIZACAO DE LEITURA DO ARQUIVO DE DADOS

# Abaixo acontece a leitura do excel e captacao das colunas interessantes a este problema
file_path = 'dados/OD_2017.csv'

origem = pd.read_csv(file_path, encoding="UTF8", sep=",", usecols=['ID_PESS', 'CO_O_X', 'CO_O_Y'])
origem.rename(columns={'CO_O_X': 'CO_X', 'CO_O_Y': 'CO_Y'}, inplace=True)
destino = pd.read_csv(file_path, encoding="UTF8", sep=",", usecols=['ID_PESS', 'CO_D_X', 'CO_D_Y'])
destino.rename(columns={'CO_D_X': 'CO_X', 'CO_D_Y': 'CO_Y'}, inplace=True)

# Juntamos locais de origem e destino em um dataframe pandas so e excluimos locais duplicados
coordenadas_df = origem.append(destino, ignore_index=False, sort=False)
coordenadas_df = coordenadas_df.loc[coordenadas_df['CO_X'] != 0].drop_duplicates()
print(coordenadas_df)

# Vamos utilizar estruturas de listas e de dicionarios para armazenar os locais.
# O dicionario sera um auxiliador para que seja possivel consultar o local a partir
# de uma string formada por suas coordenadas

locais_list = []
locais_dict = {}
num_linhas = 0

start_add_local = datetime.now()
for index, row in coordenadas_df.iterrows():
    coordenadas = str(row['CO_X']) + "_" + str(row['CO_Y'])
    if coordenadas not in locais_dict:
        local = Local(row['CO_X'], row['CO_Y'])
        locais_dict.update({coordenadas: local})
        locais_list.append(local)
    else:
        local = locais_dict[coordenadas]

    frequentador = Frequentador(row['ID_PESS'])
    local.adicionar_frequentador(frequentador)
    num_linhas += 1

# Abaixo ocorre a geracao de um log para registrar quantos frequentadores cada local possui
arquivo_locais = open('Locais.txt', 'a')
for local in locais_list:
    txt_local_linha = f'coordenadas: ({local.coordenada_x} , {local.coordenada_y}); ' \
        f'frequentadores: {len(local.frequentadores)}\n'
    arquivo_locais.write(txt_local_linha)

### FINALIZACAO DO CODIGO
print(f"Locais: {len(locais_list)} | Linhas: {num_linhas}")
end_add_local = datetime.now()
runtime_add_local = (end_add_local - start_add_local).total_seconds() / 60
print(f'Locais runtime: {runtime_add_local} min')
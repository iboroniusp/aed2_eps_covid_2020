import pandas as pd

original_file = 'dados/OD_2017.csv'

def get_cenario1_df():
    origem = pd.read_csv(original_file, encoding="UTF8", sep=",", usecols=['ID_PESS', 'CO_O_X', 'CO_O_Y'])
    origem.rename(columns={'CO_O_X': 'CO_X', 'CO_O_Y': 'CO_Y'}, inplace=True)
    destino = pd.read_csv(original_file, encoding="UTF8", sep=",", usecols=['ID_PESS', 'CO_D_X', 'CO_D_Y'])
    destino.rename(columns={'CO_D_X': 'CO_X', 'CO_D_Y': 'CO_Y'}, inplace=True)

    # Juntamos locais de origem e destino em um dataframe pandas so e excluimos locais duplicados
    coordenadas_df = origem.append(destino, ignore_index=False, sort=False)

    # Não estamos considerando lugares cuja coordenada é 0, pois significa que o entrevistado não foi a nenhum lugar
    coordenadas_df = coordenadas_df.loc[coordenadas_df['CO_X'] != 0].drop_duplicates()
    return coordenadas_df

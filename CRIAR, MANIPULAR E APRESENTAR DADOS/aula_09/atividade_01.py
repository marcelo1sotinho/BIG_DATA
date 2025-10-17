import pandas as pd
import numpy as np 

try:
    print('obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep= ';', encoding= 'iso-8859-1')

    df_ocorrencias = df_ocorrencias[['munic','estelionato']]

    df_estelionato = df_ocorrencias.groupby('munic').sum(['estelionato']).reset_index()
    # print(df_estelionato)

except Exception as e:
    print(f"Erro ao obter dados: {e}")

try:
     print('Obtendo informações sobre o padrão de roubo de veículos...')

     array_estelionato = np.array(df_estelionato['estelionato'])

     # Obtendo medidas centrais
     media_estelionato = np.mean(array_estelionato)
     mediana_estelionato = np.median(array_estelionato)
     distancia = abs((media_estelionato - mediana_estelionato) / mediana_estelionato) * 100

     print(30 * '=')
     print('Medidas de Tendência Central')
     print(f'Média de roubos: {media_estelionato:.2f}')
     print(f'Médiana de roubos: {mediana_estelionato}')
     print(f'Distancia entre média e mediana: {distancia}')

    # Obtendo os quartis
     q1 = np.quantile(array_estelionato,0.25)
     q2 = np.quantile(array_estelionato,0.50)
     q3 = np.quantile(array_estelionato,0.75)

     print('\nMedidas de Posição')
     print(30*'=')
     print(f'Q1: {q1}')
     print(f'Q2: {q2}')
     print(f'Q3: {q3}')
     
     df_estelionato_menores = df_estelionato[df_estelionato['estelionato'] < q1]
     df_estelionato_maiores = df_estelionato[df_estelionato['estelionato'] > q3]

     print('\nMunicipios com menores números de Estelionatos')
     print(70 *'=')
     print(df_estelionato_menores.sort_values(by='estelionato', ascending= True))
     
     print('\nMunicipios com maiores números de Estelionatos')
     print(70 *'=')
     print(df_estelionato_maiores.sort_values(by='estelionato', ascending= False))

     iqr = q3 - q1

     limite_superior = q3 + (iqr * 1.5)
     limite_infeior = q1 - (iqr * 1.5)

     print('\nMedidas de Posição')
     print(30 *"=")
     print(f'IQR: {iqr}')
     print(f'Limite Superior: {limite_superior}')
     print(f'Limite inferior {limite_infeior}')

     df_estelionato_maiores_outliers = df_estelionato[df_estelionato['estelionato'] > limite_superior]
     df_estelionato_menores_outliers = df_estelionato[df_estelionato['estelionato'] < limite_infeior]

     if len(df_estelionato_maiores_outliers) == 0:
         print('Não há valores muito acima da média')
     else:
         print('\nEstelionatos acima da média')
         print(30*'=')
         print(df_estelionato_maiores.sort_values(by='estelionato', ascending=False))
     
     if len(df_estelionato_menores_outliers) == 0:
         print('\nNão há valores muito abaixo da média')
     else:
         print('\nEstelionatos abaixo da média')
         print(30*'=')
         print(df_estelionato_menores.sort_values(by='estelionato', ascending=True))

         

except Exception as e:
    print(f'Erro ao obter as medidas: {e}')




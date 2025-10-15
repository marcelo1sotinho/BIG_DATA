import pandas as pd 
import numpy as np

# Conectando
try:
    print('Obtendo os dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    # print(df_ocorrencias.head())  # 5 primeiras linhas

    # Delimitando as variáveis
    df_ocorrencias = df_ocorrencias[['munic', 'roubo_veiculo']]
    # print(df_ocorrencias)

    # Totalizando as variáveis por municípios
    df_roubo_veiculo = df_ocorrencias.groupby('munic').sum(['roubo_veiculo']).reset_index()
    # print(df_roubo_veiculo)

except Exception as e:
    print(f"Erro ao obter dados: {e}")


# Obtendo as medidas
try:
    print('Obtendo informações sobre o padrão de roubo de veículos...')
    # import numpy as np
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # Obtendo medidas centrais
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    # distancia < 10% => dados simétrico | Média tende a ser confiável
    # distancia entre 25% e 10% => dados assimétricos moderado | Média pode não ser a melhor medida. Média pode estar sofrendo influência de valores extremos.
    # distancia > 25% | dados assimétrico forte | Média sofrendo influência de valores extremos.
    # Multiplica por 100 para obter o percentual
    distancia = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo) * 100

    print(30*"=")
    print('Medidas de Tendência Central')
    print(f'Média de roubos: {media_roubo_veiculo:.2f}')
    print(f'Mediana dos roubos de veículos: {mediana_roubo_veiculo}')
    print(f'Distânia entre média e mediana: {distancia}')

    # Obtendo os Quartis
    q1 = np.quantile(array_roubo_veiculo, 0.25)
    q2 = np.quantile(array_roubo_veiculo, 0.50)  # É o mesmo da Mediana
    q3 = np.quantile(array_roubo_veiculo, 0.75)

    # print()
    # print(30*"=")
    print('\nMedidas de Posição')
    print(30*"=")
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q1: {q3}')

    # Obtendo os municípios com maiores e menores números de roubos
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMunicípios com Menores números de Roubos')
    print(70*"=")
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))
    
    print('\nMunicípios com Maiores números de Roubos')
    print(70*"=")
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))  

except Exception as e:
    print(f'Erro ao obter as medidas: {e}')
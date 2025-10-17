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
    print(df_roubo_veiculo)



except Exception as e:
    print(f"Erro ao obter dados: {e}")

try:
    print('Obtendo Informação sobre o padrão de roubo de veículos...')
    
    # Obtendo medidas centrais
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    
    media_rooubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_rooubo_veiculo = np.median(array_roubo_veiculo)
    
    # Distancia < 10% => dados simétricos | Média tende a ser confiavel
    # Distancia < 25% e 10% => dados assimétricos | Média não confiavel. Média pode estar sofrendo influência de valores extremos.
    # Distancia > 25% | Dados assimetricos forte | Média sofrendo influência de valores extremos.
    # Multiplica por 100 para obter o percentual 
    distancia = abs((media_rooubo_veiculo - mediana_rooubo_veiculo) / mediana_rooubo_veiculo) * 100

    print(30*'=')
    print('Medidas de Tenêndecia Central')
    print(f'Média de roubos {media_rooubo_veiculo:,.2f}')
    print(f'Mediana dos roubos de veículos: {mediana_rooubo_veiculo}')
    print(f'Disatancia entre média e mediana: {distancia:,.2f}%')

    # Obtendo quartil 
    q1 = np.quantile(array_roubo_veiculo, 0.25)
    q2 = np.quantile(array_roubo_veiculo, 0.50)
    q3 = np.quantile(array_roubo_veiculo, 0.75)

    print('\nMedidas de Posição')
    print(30 *"=")
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    
    # Obtendo os municipios com maiores e menores
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMunicipios com menores números de roubos')
    print(70*'=')
    print(df_roubo_veiculo_menores.sort_values(by= 'roubo_veiculo', ascending=True))
    
    print('\nMunicipios com maiores números de roubos')
    print(70*'=')
    print(df_roubo_veiculo_maiores.sort_values(by= 'roubo_veiculo', ascending=False))

    #   OUTLIERS

    # Intervalo InterQuartil (IQR)
    # Q3 - Q1 
    # É a amplitude dos dados mais centrais
    # Ignora os valores os valores extremos.
    # Não sofre influência dos valores extremos
    # Quanto mais perto de Zero, mais homgênio são os dados.
    # Quanto mais perto de q3, mais heterogênio são os dados.
    iqr = q3 - q1
    
    # Para identificar os outliers (Achar os limtes: Superior e Inferior)
    limite_inferior = q1 - (1.5 * iqr)
    limite_superior = q3 + (1.5 * iqr)

    print('\nMedidas de Posição')
    print(30 *"=")
    print(f'IQR: {iqr}')
    print(f'Limite Superior: {limite_superior}')
    print(f'Limite Inferior: {limite_inferior}')

    # Descobrindo os outliers
    # Filtrando os dataframes com mais e menos roubos
    # Utilizando os limites calculados (superior e inferior)
    
    # Outliers Inferiores
    # Municípios com roubos abaixo do limete inferior
    df_roubo_veiculo_menores_outliers = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]
    
    # Outliers Superiore
    # Municípios com roubos acima do limite superior
    df_roubo_veiculo_maiores_outliers = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]
    
    # Printando Outliers inferiores
    print('\nMunicípios com Outliers Inferiores')
    print(30 *"=")
    if len(df_roubo_veiculo_menores_outliers) == 0:
        print('Não exitem outliers inferiores')
    else:
        print(df_roubo_veiculo_menores_outliers.sort_values(by= 'roubo_veiculo', ascending= True))
    
    # Printando Outliers superiores
    print('\nMunicípios com Outliers Superiores')
    print(30 *"=")
    if len(df_roubo_veiculo_maiores_outliers) == 0:
        print('Não exitem outliers superiores')
    else:
        print(df_roubo_veiculo_maiores_outliers.sort_values(by= 'roubo_veiculo', ascending= False))




except Exception as e:
    print(f'Erro ao obter as medidas {e}')

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

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


#Plotagem Gráfico com Matplotlib
try:
    plt.subplots(2,2, figsize=(16, 10))
    plt.suptitle('Analise de dados - Roubo de Veículos')
    
    # Posição 1 -Boxplot
    plt.subplot(2, 2, 1)
    plt.boxplot(array_roubo_veiculo, vert=False,showmeans=True)

    # Posição 2 - Medida
    plt.subplot(2, 2, 2)
    plt.title('Medidas Estatística')
    plt.text(0.1, 0.9, f'Limite inferior: {limite_inferior}')
    plt.text(0.1, 0.8, f'Q1: {q1}')
    plt.text(0.1, 0.7, f'Mediana: {q2}')
    plt.text(0.1, 0.6, f'Q3: {q3}')
    plt.text(0.1, 0.5, f'Média: {media_rooubo_veiculo:,.2f}')
    plt.text(0.1, 0.4, f'Limite superior: {limite_superior}')
    plt.text(0.1, 0.3, f'Distancia, Média e Mediana : {distancia:,.2f}')
    plt.text(0.1, 0.2, f'Intervalo interquartil : {iqr}')
    plt.xticks([]) # Não impreme o Eixo x do grafico
    plt.yticks([]) # Não impreme o Eixo y do grafico

    # Posição 3 - Outliers Inferiores
    plt.subplot(2, 2, 3)
    plt.title('Outliers Inferiores')
    
    if not df_roubo_veiculo_menores_outliers.empty:
        dados_inferiores = df_roubo_veiculo_menores_outliers.sort_index(by= 'roubo_veiculo', ascending=True)
    
        plt.barh(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'])
    else:
        plt.text(0.5, 0.5, f'Sem outliers inferiores', ha='center', va='center')
        plt.title('Outliers Inferiores')
        plt.xticks([])
        plt.yticks([])
    
    

    # Posição 4
    plt.subplot(2, 2, 4)
    plt.title('Outliers Superiores')

    if not df_roubo_veiculo_maiores_outliers.empty:
        dados_supreiores = df_roubo_veiculo_maiores_outliers.sort_values(by= 'roubo_veiculo', ascending=False)
    
        barras = plt.barh(dados_supreiores['munic'], dados_supreiores['roubo_veiculo'])
        plt.bar_label(barras,fmt='%.0f', label_type= 'edge', fontsize = 10)
    
    else:
        plt.text(0.5, 0.5, f'Sem outliers superiores', ha='center', va='center')
        plt.title('Outliers superiores')
        plt.xticks([])
        plt.yticks([])


    plt.show()


except Exception as e:
    print(f'Erro na plotagem do Gráfico:{e}')
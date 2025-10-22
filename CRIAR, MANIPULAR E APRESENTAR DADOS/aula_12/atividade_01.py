import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

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



#Plotagem Gráfico com Matplotlib

try:
    plt.subplots(2,2, figsize= (16, 10))
    plt.suptitle('Analise de dados- Estelionato')

    # Posição 1
    plt.subplot(2,2,1)
    plt.boxplot(array_estelionato, vert=False, showbox=True)

    # Posição 2 Media
    plt.subplot(2,2,2)
    plt.title('Medidadas Estatística')
    plt.text(0.1, 0.9, f'Limite inferior: {limite_infeior}')
    plt.text(0.1, 0.8, f'Q1: {q1}')
    plt.text(0.1, 0.7, f'Mediana: {q2}')
    plt.text(0.1, 0.6, f'Q3: {q3}')
    plt.text(0.1, 0.5, f'Média: {media_estelionato:,.2f}')
    plt.text(0.1, 0.4, f'Limite superior: {limite_superior}')
    plt.text(0.1, 0.3, f'Distancia, Média e Mediana : {distancia:,.2f}')
    plt.text(0.1, 0.2, f'Intervalo interquartil : {iqr}')
    plt.xticks([]) # Não impreme o Eixo x do grafico
    plt.yticks([]) # Não impreme o Eixo y do grafico

     # Posição 3 - Outliers Inferiores
    plt.subplot(2, 2, 3)
    plt.title('Outliers Inferiores')
    
    if not df_estelionato_menores_outliers.empty:
        dados_inferiores = df_estelionato_maiores_outliers.sort_index(by= 'estelionato', ascending=True)
    
        plt.barh(dados_inferiores['munic'], dados_inferiores['estelionato'])
    else:
        plt.text(0.5, 0.5, f'Sem outliers inferiores', ha='center', va='center')
        plt.title('Outliers Inferiores')
        plt.xticks([])
        plt.yticks([])
    
    

    # Posição 4
    plt.subplot(2, 2, 4)
    plt.title('Outliers Superiores')

    if not df_estelionato_maiores_outliers.empty:
        dados_supreiores = df_estelionato_maiores_outliers.sort_values(by= 'estelionato', ascending=False)
    
        barras = plt.barh(dados_supreiores['munic'], dados_supreiores['estelionato'])
        plt.bar_label(barras,fmt='%.0f', label_type= 'edge', fontsize = 10)
    
    else:
        plt.text(0.5, 0.5, f'Sem outliers superiores', ha='center', va='center')
        plt.title('Outliers superiores')
        plt.xticks([])
        plt.yticks([])


    plt.show()


















except Exception as e:
    print(f'Erro na plotagem Gráfica {e}')
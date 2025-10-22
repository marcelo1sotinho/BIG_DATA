import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

try:
    print('Obtendo os dados...')
    ENDERECO_DADOS = 'BaseDados_Vendas.csv'

    df_vendas = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='UTF-8')
    # print(df_vendas.head())
    df_vendas = df_vendas[['Produto','Preco Vendido','Loja']]
    df_produto = df_vendas.groupby('Produto').sum(['Preco Vendido']).reset_index()
    # print(df_produto)
    

except Exception as e:
    print('Erro ao obter dados: {e}')

try:
    print('Obtendo as medidas')

    array_preco_vendido = np.array(df_produto['Preco Vendido'])

    # Medidas de Tendência Central
    media_preco_vendido = np.mean(array_preco_vendido)
    mediana_preco_vendido = np.median(array_preco_vendido)
    distancia = abs(((media_preco_vendido - mediana_preco_vendido) / mediana_preco_vendido)) *100

    print('\nMEDIDAD DE TENDÊNCIA CENTRAL')
    print(30*'=')
    print(f'Média de Produtos Vendidos: {media_preco_vendido}')
    print(f'Mediana de Produtos Vendidos: {mediana_preco_vendido}')
    print(f'Distancia entre média e mediana: {distancia}')

    # Medidas de posição "Quartis"
    q1 = np.percentile(array_preco_vendido, 25)
    q2 = np.percentile(array_preco_vendido, 50)
    q3 = np.percentile(array_preco_vendido, 75)

    print('\nMedidas de posição "Quartis": ')
    print(50*'=')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')

    maximo = np.max(array_preco_vendido)
    minimo = np.min(array_preco_vendido)
    amplitude_total = maximo - minimo

    # Filtrando conjuntos maiores e menores
    df_produto_menores = df_produto[df_produto['Preco Vendido'] < q1]
    df_produto_maiores = df_produto[df_produto['Preco Vendido'] > q3]

    print('\nProdutos com maiores vendas')
    print(50*'=')
    print(df_produto_maiores.sort_values(by='Preco Vendido', ascending= False))
    print('\nProdutos com menores vendas')
    print(50*'=')
    print(df_produto_menores.sort_values(by='Preco Vendido', ascending= True))

    # IQR E LIMITES
    iqr = q3 - q1
    limite_superior = q3 + (iqr *1.5)
    limite_inferior = q1 - (iqr *1.5)

    print('\nLimites - Medidas de Posição')
    print(50*'=')
    print(f'IQR: {iqr}')
    print(f'Limite superior: {limite_superior:,.2f}')
    print(f'Limite inferior: {limite_inferior:,.2f}')

    # OUTLIERS
    df_produto_outliers_inferiores = df_produto[df_produto['Preco Vendido'] < limite_inferior]
    df_produto_outliers_superiores = df_produto[df_produto['Preco Vendido'] > limite_superior]
    
    print('\nMunicipios com outliers inferiores')
    print(50*'=')
    if df_produto_outliers_inferiores.empty:
        print('Não exitem outliers inferiores')
    else:
        print(df_produto_outliers_inferiores.sort_values(by='Preco Vendido',ascending=True))
    
    print('\nMunicipios com outliers Superiores')
    print(50*'=')
    if df_produto_outliers_superiores.empty:
        print('Não exitem outliers supeiores')
    else:
        print(df_produto_outliers_superiores.sort_values(by='Preco Vendido',ascending=True))
    
    variancia = np.var(array_preco_vendido)
    desvio_padrao = np.std(array_preco_vendido)
    coef_variacao = (desvio_padrao/media_preco_vendido) * 100
    distancia_var_media = variancia /(media_preco_vendido ** 2)

except Exception as e:
    print(f'Erro ao obter as medidas {e}')

try:
    print('\nPRINTANDO AS MEDIDAS: ')
    print(30*'-')
    print(f'Limite Inferior: {limite_inferior} ')
    print(f'Mínimo: {minimo} ')
    print(f'1º Quartil: {q1}')
    print(f'2º Quartil: {q2}')  # Mediana
    print(f'3º Quartil: {q3}')
    print(f'IQR: {iqr}')
    print(f'Máximo: {maximo}')
    print(f'Limite Superior: {limite_superior}')

    print('\nOUTRAS AS MEDIDAS: ')
    print(30*'-')
    print(f'Média: {media_preco_vendido:,.3f}')
    print(f'Mediana: {mediana_preco_vendido:,.3f}')
    print(f'Distância Média e Mediana: {distancia}')
    print(f'Amplitude Total: {amplitude_total}')
    print(f'Desvio Padrão: {desvio_padrao:,.2f}')
    print(f'Coeficiente de Variação: {desvio_padrao:,.2f}%')
    print(f'Variancia: {variancia:.2f}')
    print(f'Distancia entre variancia e média: {distancia_var_media:.2f}')

    print('')
except Exception as e:
    print(f'Erro ao printar as medidas: {e}')
    exit()

try:
    plt.subplots(2,2,figsize=(16,10))
    plt.suptitle('Analise de Dados - Venda de Produtos')

    # Posição 1
    plt.subplot(2,2,1)
    plt.boxplot(array_preco_vendido, vert=False, showmeans=True)

    # Posição 2
    plt.subplot(2,2,2)
    plt.suptitle('Medidas Estatistica')
    plt.text(0.1, 0.9, f'Limite inferior: {limite_inferior}', fontsize=10)
    plt.text(0.1, 0.8, f'Q1: {q1}',fontsize=10)
    plt.text(0.1, 0.7, f'Mediana: {q2}',fontsize=10)
    plt.text(0.1, 0.6, f'Q3: {q3}',fontsize=10)
    plt.text(0.1, 0.5, f'Média: {media_preco_vendido:,.2f}',fontsize=10)
    plt.text(0.1, 0.4, f'Limite superior: {limite_superior}',fontsize=10)
    plt.text(0.1, 0.3, f'Distancia, Média e Mediana : {distancia:,.2f}',fontsize=10)
    plt.text(0.1, 0.2, f'Intervalo interquartil : {iqr}',fontsize=10)

    plt.text(0.5, 0.9, f'Maximo: {maximo}', fontsize=10)
    plt.text(0.5, 0.8, f'Minímo: {minimo}', fontsize=10)
    plt.text(0.5, 0.7, f'Amplitude total: {amplitude_total}',fontsize=10)
    plt.text(0.5, 0.6, f'Variancia: {variancia}', fontsize=10)
    plt.text(0.5, 0.5, f'Dista. variancia e Média: {distancia_var_media}', fontsize=10)
    plt.text(0.5, 0.4, f'Desvio Padrão: {desvio_padrao}', fontsize=10)
    plt.text(0.5, 0.3, f'Coeficiente de Variação: {coef_variacao}', fontsize=10)
    
    plt.xticks([])
    plt.yticks([])
    
    # Posição 3
    plt.subplot(2,2,3)
    plt.title('Outliers Infeiores')

    if not df_produto_outliers_inferiores.empty:
        dados_inferiores = df_produto_outliers_inferiores.sort_values(by='Preco Vendido',ascending=True)
 
        plt.barh(dados_inferiores['Produto'], dados_inferiores['Preco Vendido'])
    else:
        plt.text(0.5, 0.5, f'Sem outliers inferiores', ha='center', va='center')
        plt.title('Outliers Inferiores')
        plt.xticks([])
        plt.yticks([])
    
    # Posição 4
    plt.subplot(2,2,4)
    plt.title('Outliers Supreiores')

    if not df_produto_outliers_superiores.empty:
        dados_supreiores = df_produto_outliers_superiores.sort_values(by='Preco Vendido',ascending=True)
 
        barras = plt.barh(dados_supreiores['Produto'], dados_supreiores['Preco Vendido'])
        plt.bar_label(barras,fmt='%.0f', label_type= 'edge', fontsize = 8)
    else:
        plt.text(0.5, 0.5, f'Sem outliers inferiores', ha='center', va='center')
        plt.title('Outliers Inferiores')
        plt.xticks([])
        plt.yticks([])
    


    plt.show()







except Exception as e:
    print(f'Erro na plotagem Gráfica {e}')
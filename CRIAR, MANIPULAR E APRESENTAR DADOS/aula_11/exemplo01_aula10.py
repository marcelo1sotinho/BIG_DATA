# from utils import limpar_nome_municipio
# pip install matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


try:
    print("Obtendo dados...")
    ENDERECO_DADOS = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"

    # Buscar a base de dados CSV online do site ISP (Instituto de Segurança Pública)
    # encoding='iso-8859-1' - Codificação dos caracteres com acentuação
    # outras opções: utf-8, iso-8859-1, latin1, cp1252
    # encodings principais: https://docs.python.org/3/library/codecs.html#standard-encodings
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Demilitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_ocorrencias = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Totalizar roubo de veiculo por municipio (agrupar e somar)
    # reset_index(), traz de volta os índices, que numera as colunas
    df_roubo_veiculo = df_ocorrencias.groupby('munic').sum(['roubo_veiculo']).reset_index()

    # Printando as linhas iniciais com o método head() apenas para ver se os dados
    # foram obtidos corretamente
    print(df_roubo_veiculo.head())

except Exception as e:
    print(f"Erro ao obter dados: {e}")
    exit()


# Inicando a obtenção das medidas fundamentadas em estatística descritiva
try:
    print('Obtendo informações sobre padrão de roubo de veículos...')

    # Numpy
    # Uso do ARRAY
    # Array faz parte da biblioteca numpy
    # Array é uma estrutura de dados que armazena uma coleção de dados
    # https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html
    # pip install numpy
    # import numpy as np
    # NumPy significa numerical python e tem como objetivo adicionar suporte
    # para arrays e matrizes multidimensionais, juntamente com uma grande
    # coleção de funções matemáticas de alto nível.
    # OBS:
    # Uso do array significa ganho computacional
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # //////////////// MEDIDAS DE TENDÊNCIA CENTRAL ////////////////////
    # Obtendo média de roubo_veiculo
    media_roubo_veiculo = np.mean(array_roubo_veiculo)

    # Obtendo mediana de roubo_veiculo
    # Mediana é o valor que divide a distribuição em duas partes iguais
    # (50% dos dados estão abaixo e 50% acima)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    # ##### INTERPRETAÇÃO: (Distânicia entre Média e Mediana)
    # A distância entre a média e a mediana é uma medida de assimetria
    # A distância é obtida dividindo a diferença entre a Média e Mediana pela mediana.
    # A distância é dada em porcentagem
    # Exemplo: 0.1 significa 10%
    # Se a distância for menor que 10%, a distribuição tende a ser simétrica.
    # Se a distância for maior que 10%  e menor ou igual a 25%, a distribuição
    # tende a ser assimétrica moderada. Pode ser, que a média esteja sofrendo
    # influência de valores extremos da distribuição.
    # Se a distância for maior que "25%", a distribuição tende a ser
    # assimétrica forte. A tendência é, que neste caso, a média esteja
    # sofrendo influência de valores extremos.
    distancia = abs(((media_roubo_veiculo-mediana_roubo_veiculo) / mediana_roubo_veiculo)) * 100

    print('\nMEDIDAS DE TENDÊNCIA CENTRAL')
    print(30*'-')
    print(f'Média de roubo de veículos: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veículos: {mediana_roubo_veiculo}')
    print(f'Distância entre média e mediana: {distancia:.3f}')


    # //////////////////////// QUARTIS ////////////////////////////
    # Os quartis são os valores que dividem a distribuição em 4 partes iguais.
    # O quartil é uma medida de posição, que indica a posição de um valor em
    # O primeiro quartil (Q1) é o valor que divide a distribuição em 25% e 75%.
    # O segundo quartil (Q2) é o valor que divide a distribuição em 50% e 50%.
    # OBSEVAÇÃO: O Q2 é a mesma coisa que a Mediana.
    # O terceiro quartil (Q3) é o valor que divide a distribuição em 75% e 25%.
    # relação a uma distribuição.

    # ###### INTERPRETAÇÃO (QUARTIS Q1, Q2, Q3)
    # 25% dos valores estão abaixo do Q1. Se 25% dos valores estão abaixo do
    # Q1, então 75% dos valores estão acima do Q1.
    # 50% dos valores estão abaixo do Q2, que é igual a Meidana. Se 50% dos
    # valores estão abaixo do Q2, então 50% dos valores estão acima do Q2.
    # 75% dos valores estão abaixo do Q3. Se 75% dos valores estão abaixo do
    # Q3, então 25% dos valores estão acima do Q3.
    q1 = np.quantile(array_roubo_veiculo, 0.25)  # Q1 é 25%
    q2 = np.quantile(array_roubo_veiculo, 0.50)  # Q2 é 50% (mediana)
    q3 = np.quantile(array_roubo_veiculo, 0.75)  # Q3 é 75%
    
    # Podemos cacular os Quartis fazendo uso de alguns métodos.
    # Os métodos mais comuns são: 'weibull', 'linear' ou 'hazen'.
    # OBS: SÓ USE OS MÉTODOS, SE VOCÊ SOUBER O QUE ESTÁ FAZENDO, CASO
    # CONTRÁRIO, FAÇA COMO NO EXEMPLO ACIMA, SEM USO DOS MÉTODOS.
    # EXEMPLO DE CÁLCUL DOS QUARTIS FAZENDO USO DOS MÉTODOS:
    # q1 = np.quantile(array_roubo_veiculo, 0.25, method='weibull') # Q1 é 25%
    # q2 = np.quantile(array_roubo_veiculo, 0.50, method='weibull') # Q2 é 50% (mediana)
    # q3 = np.quantile(array_roubo_veiculo, 0.75, method='weibull') # Q3 é 75%
    print('\nMedidas de posição "Quartis": ')
    print(30*'-')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')

    # ////////// OUTRAS /////////
    maximo = np.max(array_roubo_veiculo) # Posição
    minimo = np.min(array_roubo_veiculo) # Posição
    # Quanto mais próximo do máximo, mais diperso é o conjunto
    # Quanto mais próximo do mínimo, mais homogênio é o conjunto
    # Indica Variabilidade dos Dados
    amplitude_total = maximo - minimo

    # ####### FILTRANDO O CONJUNTO DE DADOS:
    # OBTENDO OS MUNÍCIPIOS COM MAIORES E MONORES NÚMEROS DE ROUBOS DE VEÍCULOS
    # Filtramos os registros do DataFrame df_roubo_veiculo para achar os
    # municípios     # com menores e maiores números de roubos de veículos.
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMunicípios com Menores números de Roubos: ')
    print(70*'-')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))
    print('\nMunicípios com Maiores números de Roubos:')
    print(45*'-')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))

    # ////////////////////////// OUTLIERS /////////////////////////////////
    # # Outliers são valores discrepantes. São valores que estão muito abaixo
    # ou acima dos demais valores do conjunto de dados.
    # Indicam pontos fora do padrão esperado (muito altos ou muito baixos).
    # Servem para identificar possíveis erros, exceções ou casos raros.
    # 1º Calcular IQR
    # 2º Calcular os Limites (Superiores e Infeirores)
    # 3º Filtrar os dados superiores e inferiores aos limites
    # para achar os outliers

    # IQR - (Intervalo interquartil)
    # É a diferença entre Q3 e Q1. Subtração de q3 - q1
    # É a amplitude do intervalo dos 50% dos dados mais centrais
    # Ela ignora os valores extremos.
    # Não sofre a interferência dos valores extremos.
    # Quanto mais próximo de zero, mais homogêneo são os dados.
    # Quanto mais próximo do q3, mais heterogêneo são os dados.
    iqr = q3 - q1

    # Limite superior
    # Vai identificar os outliers acima de q3
    limite_superior = q3 + (1.5 * iqr)

    # Limite inferior
    # Vai identificar os outliers abaixo de q1
    limite_inferior = q1 - (1.5 * iqr)

    # MOSTRANDO AS MEDIDAS ORDENDADAS / ORGANIZADAS
    print('\nLimites - Medidas de Posição')
    print(45*'-')
    print(f'IQR: {iqr}')
    print(f'Limite inferior: {limite_inferior}')
    print(f'Limite superior: {limite_superior}')

    # ###### OUTLIERS
    # Obtendo os ouliers inferiores
    # Filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo
    # abaixo limite inferior (OUTLIERS INFERIORES)
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    # Obtendo os ouliers superiores
    # Filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo
    # acima de limite superior (OUTLIERS SUPERIORES)
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    print('\nMunicípios com outliers inferiores: ')
    print(45*'-')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!')
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True))

    print('\nMunicípios com outliers superiores: ')
    print(45*'-')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print('Não existe outliers superiores!')
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()

try:
    print('Calculando medidas de variabilidade')
    variancia = np.var(array_roubo_veiculo)
    desvio_padrao = np.std(array_roubo_veiculo)
    coef_variacao = (desvio_padrao / media_roubo_veiculo) * 100
    distancia_var_media = variancia /(media_roubo_veiculo ** 2)

except Exception as e:
    print(f'Erro ao calcular as medidas de variabilidade. {e}')

# Printando as Medidas
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
    print(f'Média: {media_roubo_veiculo:,.3f}')
    print(f'Mediana: {mediana_roubo_veiculo}')
    print(f'Distância Média e Mediana: {distancia:,.4f}%')
    print(f'Amplitude Total: {amplitude_total}')
    print(f'Desvio Padrão: {desvio_padrao:,.2f}')
    print(f'Coeficiente de Variação: {desvio_padrao:,.2f}%')
    print(f'Variancia: {variancia:.2f}')
    print(f'Distancia entre variancia e média: {distancia_var_media:.2f}')

except Exception as e:
    print(f'Erro ao printar as medidas: {e}')
    exit()


# PLOTANDO GRÁFICO COM A BIBLIOTECA MATPLOTLIB
try:
    # É necessário importar:
    # import matplotlib.pyplot as plt   
    plt.subplots(2, 2, figsize=(16, 10))
    plt.suptitle('Análise de roubo de veículos no RJ')

    # POSIÇÃO 01
    # BOXPLOT
    plt.subplot(2, 2, 1)  
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=True)
    plt.title("Boxplot dos Dados")

    # POSIÇÃO 02
    # MEDIDAS
    # Exibição de informações estatísticas
    plt.subplot(2, 2, 2)
    plt.title('Medidas Estatísticas')
    plt.text(0.1, 0.9, f'Limite inferior: {limite_inferior}', fontsize=10)
    plt.text(0.1, 0.8, f'Minimo: {minimo}', fontsize=10)
    plt.text(0.1, 0.7, f'Q1: {q1}', fontsize=10)
    plt.text(0.1, 0.6, f'Mediana: {mediana_roubo_veiculo}', fontsize=10)
    plt.text(0.1, 0.5, f'Q3: {q3}', fontsize=10)
    plt.text(0.1, 0.4, f'Média: {media_roubo_veiculo:.3f}', fontsize=10)
    plt.text(0.1, 0.3, f'Máximo: {maximo}', fontsize=10)
    plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=10)

    plt.text(0.5, 0.9, f'Distância Média e Mediana: {distancia:.4f}', fontsize=10)
    plt.text(0.5, 0.8, f'IQR: {iqr}', fontsize=10)
    plt.text(0.5, 0.7, f'Amplitude Total: {amplitude_total}', fontsize=10)
    plt.text(0.5, 0.6, f'Variancia: {variancia:,.2f}', fontsize=10)
    plt.text(0.5, 0.5, f'Dista. Variancia e Média: {distancia_var_media}', fontsize=10)
    plt.text(0.5, 0.4, f'Desvio padrão: {desvio_padrao:,.2f}', fontsize=10)
    plt.text(0.5, 0.3, f'Coeficiente de Variação: {coef_variacao:,.2f}', fontsize=10)
    


    # POSIÇÃO 03
    # OUTLIERS INFERIORES
    plt.subplot(2, 2, 3)
    plt.title('Outliers Inferiores')
    # Se o DataFrame do outliers não estiver vazio
    if not df_roubo_veiculo_outliers_inferiores.empty:
        dados_inferiores = df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True) #crescente
        # Gráfico de Barras
        plt.barh(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'])
    else:
        # Se não houver outliers
        plt.text(0.5, 0.5, 'Sem Outliers Inferiores', ha='center', va='center', fontsize=12)
        plt.title('Outilers Inferiores')
        plt.xticks([])
        plt.yticks([])

    # POSIÇÃO 04
    # OUTLIERS SUPERIORES
    plt.subplot(2, 2, 4)
    plt.title('Outliers Superiores')
    if not df_roubo_veiculo_outliers_superiores.empty:
        dados_superiores = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=True)

        # Cria o gráfico e guarda as barras
        barras = plt.barh(dados_superiores['munic'], dados_superiores['roubo_veiculo'], color='black')
        # Adiciona rótulos nas barras
        plt.bar_label(barras, fmt='%.0f', label_type='edge', fontsize=8, padding=2)

        # Diminui o tamanho da fonte dos eixos
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)

        plt.title('Outliers Superiores')
        plt.xlabel('Total Roubos de Veículos')
    else:
        # Se não houver outliers superiores, exibe uma mensagem no lugar.
        plt.text(0.5, 0.5, 'Sem outliers superiores', ha='center', va='center', fontsize=12)
        plt.title('Outliers Superiores')
        plt.xticks([])
        plt.yticks([])

    # Ajusta os espaços do layout para que os gráficos não fiquem espremidos
    plt.tight_layout()
    # Mostra a figura com os dois gráficos
    plt.show()

except Exception as e:
    print(f'Erro ao plotar {e}')
    exit()
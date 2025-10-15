import numpy as np 
import pandas as pd 

df = pd.read_excel('vendas_roupas.xlsx')

array_faturamento = np.array(df['Faturamento Total (R$)'])

# Medidas de Tendêndicia central ou de Posição
media_faturamento = np.mean(array_faturamento)
mediana_faturamento = np.median(array_faturamento)

print(30 * '=')
print(f'MEDIDAS DE TENDÊNCIA CENTRAL')
print(F'Média faturamento: {media_faturamento}')
print(F'Mediana faturamento: {mediana_faturamento}')

# Obentendo os Quartis
q1 = np.quantile(array_faturamento, 0.25)
q2 = np.quantile(array_faturamento, 0.50)
q3 = np.quantile(array_faturamento, 0.75)

print(30 * '=')
print('QUARTIS')
print(f'Q1: 25% {q1}')
print(f'Q2: 50% {q2}')
print(f'Q3: 75% {q3}')

#  Menores faturamento
df_menores_faturamento = df[df['Faturamento Total (R$)'] < q1]

print('\n PRODUTOS COM MENORES FATURAMENTOS')
print(df_menores_faturamento)

#Produtos Organizados
print(df_menores_faturamento[['Produto','Faturamento Total (R$)']].sort_values(by = 'Faturamento Total (R$)', ascending = False))
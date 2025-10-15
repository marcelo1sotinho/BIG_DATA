import numpy as np 
import pandas as pd 

df = pd.read_excel('vendas_eletronicos.xlsx')
# print(df.head())
# print(df.columns)

array_faturamento = np.array(df['Faturamento Total (R$)'])

# Medidas Centrais
media = np.mean(array_faturamento)
mediana = np.median(array_faturamento)

print('=======================================')
print("CALCULO DAS MEDIDAS CENTRAIS")
print(f'\nA média de faturamento é {media:,.2f}')
print(f'A mediana de faturamento é {mediana:,.2f}')

#Calculo dos quartis
q1 = np.quantile(array_faturamento, 0.25)
q2 = np.quantile(array_faturamento, 0.50)
q3 = np.quantile(array_faturamento, 0.75)

df_maiores_faturamento = df[df['Faturamento Total (R$)'] > q3 ]

print('\n=======================================')
print('Produtos com maiores faturamentos'.upper())
print(f"\n{df_maiores_faturamento[['Produto','Faturamento Total (R$)']].sort_values(by = 'Faturamento Total (R$)', ascending = False)}")

print('\n=======================================')
print('QUARTIS DOS TOTAIS DE VENDAS')
print(f"\n25% dos produtos faturam até Q1: {q1:,.2f}")
print(f"50% dos produtos faturam até Q2: {q2:,.2f}")
print(f"75% dos produtos faturam até Q3: {q3:,.2f}")
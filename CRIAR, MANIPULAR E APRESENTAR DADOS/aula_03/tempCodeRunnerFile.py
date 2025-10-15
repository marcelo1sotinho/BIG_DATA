import numpy as np 
import pandas as pd 

df = pd.read_excel('vendas_eletronicos.xlsx')
print(df.head())
print(df.columns)

array_faturamento = np.array(df['Faturamento Total (R$)'])

media = np.mean(array_faturamento)
mediana = np.median(array_faturamento)

print(f'A média de faturamento é {media:,.2f}')
print(f'A mediana de faturamento é {mediana:,.2f}')

q1 = np.quantile(array_faturamento, 0.25)
q2 = np.quantile(array_faturamento, 0.50)
q3 = np.quantile(array_faturamento, 0.75)

df_maiores_faturamento = df[df['Faturamento Total (R$)'] > q3 ]
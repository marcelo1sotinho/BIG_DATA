# pip install openpyx

import pandas as pd 

# Lendo arquivo do Excel
df =  pd.read_excel('vendas_eletronicos.xlsx')

print(df)
print(df.head())
print(df.columns) # Imprime as colunas

# Maior valor
print(f'Maior valor: {df["Faturamento Total (R$)"].max()}')

# Menor valor
print(f'Menor valor: {df["Faturamento Total (R$)"].min()}')

# Total de Unidades
print(f'Total de Unidades {df["Unidades Vendidas"].sum()}')

#Média dos preços
print(f'Média dos preços {df["Preço por Unidade (R$)"].mean()}')

# Valores acima de 60 mil
print(f'Valore > 60 mil\n {df[df["Faturamento Total (R$)"]> 60000]}')


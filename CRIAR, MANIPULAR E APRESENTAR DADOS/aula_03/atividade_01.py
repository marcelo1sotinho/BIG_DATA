import pandas as pd 

#Carregar os dados da planilha 
df = pd.read_excel('vendas_roupas.xlsx')

# Exibir as 10 primeiras linhas
print(df.head(10))

# Calcular o total de quantidade de vendas
print(f'\nTotal de vendas: {df["Unidades Vendidas"].sum()}')

# Encontrar o valor médio dos preços por unidade
print(f'Média do preços: {df["Preço por Unidade (R$)"].mean()}')

# Descobrir o maior faturamento total entreo os produtos
print(f'Maior faturamento: {df["Faturamento Total (R$)"].max()}')

# Identificar o menor faturamento total entre os produtos
print(f'Menor faturamento: {df["Faturamento Total (R$)"].min()}')

#  Identificar os produtos com classificação de nível de satisfação baixo
print(f'\nNível de satisfação baixo: \n{df[df["Satisfação"] == "Baixo" ]}')



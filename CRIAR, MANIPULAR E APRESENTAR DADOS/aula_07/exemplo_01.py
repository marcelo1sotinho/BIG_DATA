from sqlalchemy import create_engine 
import pandas as pd 
import numpy as np

host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_produtos_eco2025'

#URL de conexão
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Recebendo os dados do banco de dados
df_estoque = pd.read_sql('tb_produtos',engine)

# print(df_estoque.head())

df_estoque['total estoque R$'] = df_estoque['preco'] * df_estoque['quantidade']

print(df_estoque[['produto', 'total estoque R$']])

valor_financeiro = df_estoque['total estoque R$'].sum()

print()
print(45*'/')
print(F'Valor financeiro dos produtos: {valor_financeiro:,.2f}')
print(45*'/')

# Parte 2
array_estoque = np.array(df_estoque['total estoque R$'])

media = np.mean(array_estoque)
mediana = np.median(array_estoque)

print()
print(45*'=')
print('MEDIDAS DE TÊNDENCIAS CENTREAIS')
print(F'Media dos totais Financeiros {media:,.2f}')
print(F'Mediana dos totais Financeiros {mediana:,.2f}')
print(45*'=')
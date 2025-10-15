import pandas as pd 

# lista
lista_estoque = [15, 30 , 10, 25]

# serie do Pandas
serie_pandas = pd.Series(lista_estoque)

print('Lista')
print(lista_estoque)

print('\nSerie do Pandas')
print(serie_pandas)

#Acesso pelo índice na posição 2 
print(f'Posição 2: {serie_pandas[2]}') 

# Acesso Mútiplo Valores
print(f'Posição 1 e 3: {serie_pandas[[1, 3]].values}') 

#Filtrando os menores ou iguais a 20 
print('Filtrando os menores ou iguais a 20: ')
print(serie_pandas[serie_pandas <= 20]) 

#Cálculos com Séries 
print('Acresentando 10 nos valores da Séries')
print(serie_pandas + 10)


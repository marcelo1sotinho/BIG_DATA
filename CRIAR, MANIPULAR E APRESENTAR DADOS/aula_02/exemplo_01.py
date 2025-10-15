import pandas as pd

data = {
    'Nome' : ['Ana', 'João', 'Maria'],
    'Idade': [23, 35, 29],
    'Gênero' : ['F', 'M', 'F'],
    'Altura': [1.70, 1.80, 1.65]

}

#Criando um Datafrane a partir do dicionário 'data
# o DataFrame organiza os dados em uma tabela
df = pd.DataFrame(data)

print(f'\n {df}')

print(30 * '=')
print('Variaveis Quantitativas')
print('Idades')
print(data['Idade'])

print('Alturas')
print(data['Altura'])

# Variáveis Qualitativas
print(30 * '=')
print('Exibindo Gênero')
print(df['Gênero'])


import pandas as pd 


#Criando uma lista de quantidade em estoque para difrentes produtos
produtos = ['Notebook', 'Smatphone', 'Tablet','Smartwatch', 'Câmera']
quantidade_estoque = [40,72,50,29,23]

#Criando um série no Pandas 
estoque =pd.Series(quantidade_estoque, index = produtos)

#Exbindo a série
print('Série Estoque de Produtos: ')
print(estoque)

#Selecionando um valor específico pelo índice
print('\nQuantidade de notebook em estoque: ')
print(estoque['Notebook'])

# Selecionando múltiplo valores
print('n\Estoque de Notebook e Câmera: ')
print(estoque[['Notebook', 'Câmera']].values)

#Filtrando com estoque abaixo de 50
print('\nProdutos com estoque abaixo de 50 unidades:')
print(estoque[estoque < 50])

#Operação aritimética aumentar o estoque em 5 unidades
print('\nAumentando o estoque em 5 unidades para todos os produtos: ')
print(estoque + 5)

#incluindo um valor nulo para simular a falta de dados
estoque.loc['Headohone'] = None
print('\nEstoque como um valor nulo (Headphone): ')
print(estoque)

#Operações Aritméticas entre Séries
#Criando outra série com preços dos produtos
precos = pd.Series([3500, 2500, 1200, 900, 2500],index = produtos)

# Calculadora o valor total do estoque (preço * quantidade)
print('\nValor total do estoque po produto (preço* quantidade)')
print(precos * estoque)

import pymysql
from sqlalchemy import create_engine, text

# Variáveis de conexão
host = 'localhost' #127.0.0.1 = máquina atual
user = 'root'
password = 'root'
database = 'bd_vendas_eco2025' #nome do banco de dados

# URL de conexão com o banco de dados
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

with engine.connect() as conexao:
    query = 'SELECT * FROM vendas'
    resultado = conexao.execute(text(query))

    for i in resultado:
        print(f'Produto: {i[0]}, Data da venda: {i[1]}, Categoria: {i[2]}, Loja: {i[3]}, Valor: {i[4]}')

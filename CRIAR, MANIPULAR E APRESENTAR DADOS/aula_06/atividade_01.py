import pymysql
from sqlalchemy import create_engine, text

host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_vendas_eco2025'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

with engine.connect() as conexao:
    query = 'SELECT * FROM importacao'
    resultado = conexao.execute(text(query))

    for i in resultado:
        print(f'Nome_produto: {i[0]}, Categoria: {i[1]}, Loja: {i[2]}, Qtd_Vendida: {i[3]}, Preco: {i[4]}')

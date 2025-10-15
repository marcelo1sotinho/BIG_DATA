/*SELECT* FROM vendas;

SELECT produto, valor , datavenda FROM vendas;

SELECT categoria FROM vendas;

SELECT datavenda FROM vendas WHERE datavenda >= '2024-01-01';

SELECT produto, valor FROM vendas WHERE valor > 100;

CREATE TABLE Produtos (
	ID INT auto_increment PRIMARY KEY,
    NOME VARCHAR(200),
    PRECO DECIMAL(10,2),
    ESTOQUE INT 
);

INSERT INTO produtos(NOME, PRECO, ESTOQUE)
VALUES('Creme dental', 5.99, 50),
('Arorz', 5.00, 20),
('Feijão', 6.00, 35); 

DELETE FROM produtos WHERE ID = 1;

UPDATE produtos 
SET nome = 'Oléo', PRECO = 7.99
WHERE ID = 4;*/

SELECT * FROM produtos;
CREATE SCHEMA loja;
USE loja;

CREATE TABLE utilizadores (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_cadastro DATETIME
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_utilizador INTEGER NOT NULL,
    data_pedido DATETIME,
    valor_total DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (id_utilizador) REFERENCES utilizadores(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
PRAGMA foreign_keys = ON;

CREATE TABLE utilizadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_cadastro TEXT DEFAULT (DATE('now')),
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_utilizador INTEGER NOT NULL,
    data_pedido TEXT DEFAULT (DATETIME('now')),
    valor_total DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (id_utilizador) REFERENCES utilizadores(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
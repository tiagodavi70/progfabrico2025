import sqlite3

conn = sqlite3.connect("exemplo.sqlite")
cursor = conn.cursor()

def criarTabelas():
    with open("createDB.sql") as f:
        scriptSQL = "".join(f.readlines())
        cursor.executescript(scriptSQL)

        conn.commit()
        conn.close()

def popularTabelas():
    with open("update.sql") as f:
        scriptSQL = "".join(f.readlines())
        cursor.executescript(scriptSQL)

        conn.commit()
        conn.close()

def selecionarUtilizadores():
    linhas = cursor.execute("SELECT nome from utilizadores")
    linhas = linhas.fetchall()
    
    conn.commit()
    
    return linhas

def adicionarPedidos(valores):
    
    cursor.executemany("INSERT INTO pedidos(id_utilizador, valor_total) VALUES (?, ?)", valores)
    conn.commit()

def selecionarPedidos():
    linhas = cursor.execute("SELECT * FROM pedidos")
    linhas = linhas.fetchall()

    conn.commit()

    return linhas

if __name__ == "__main__":
    #criarTabelas()
    #popularTabelas()
    resultado = selecionarUtilizadores()
    print(resultado)

    valoresAdicionar = [[1, 750.0], [2, 8.0], [4, 900.0]]
    adicionarPedidos(valoresAdicionar)
    print(selecionarPedidos())
    conn.close()
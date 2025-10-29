

import datetime

class Produto():

    def __init__(self, nome, preco, tipo):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo

    def __str__():
        return f"{self.nome} | {self.preco} | {self.tipo}"

class Venda():

    def __init__(self, produto):
        self.produto = produto
        self.precoVenda = produto.preco
        self.dataVenda = datetime.date

opcao = 0
produtos = []
vendas = []
while opcao != 5:

    opcao = int(input("Entra com tua opção: \n1 - Cadastrar\n2 - Editar\n3- Vender\n4 - Relatorio\n5 - Sair\n"))
    if opcao == 1:
        nome = input("Entra com o nome do produto: ")
        preco = float(input("Entra com o preço do produto: "))
        tipo = input("Entra com o tipo do produto: ")

        produto = Produto(nome, preco, tipo)
        produtos.append(produto)

    elif opcao == 2:
        
        for i in range(produtos):
            print(f"{i+1} - {produtos[i]}")
        indice = int(input("Entra com o Id do produto: "))

        produtoSelecionado = produtos[indice - 1]
        novoNome = input(f"Entra com o novo nome ({produtoSelecionado["nome"]}):")
        produtoSelecionado.nome = novoNome
    
    elif opcao == 3:
        
        for i in range(produtos):
            print(f"{i+1} - {produtos[i]}")
        indice = int(input("Entra com o Id do produto: "))

        produtoSelecionado = produtos[indice - 1]
        venda = Venda(produtoSelecionado)
        vendas.append(venda)
    
    elif opcao == 4:
        # valor total ganho e a média por tipo de produto
        valorTotal = 0
        for v in vendas:
            valorTotal = valorTotal + v.precoVenda
        
        print(f"Total: {valorTotal}")

        tipos = []
        for p in produtos:
            if not p["tipo"] in tipos:
                tipos.append(p.tipo)
        
        for t in tipos:
            soma = 0
            contador = 0
            for v in vendas:
                if v.tipo == t:
                    soma += v.preco
                    contador += 1
            media = soma / contador
            print(f"Média de {tipo}: {media}")
        
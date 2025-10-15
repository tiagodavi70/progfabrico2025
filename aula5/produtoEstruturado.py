'''

Escreva um script quer faça o controle de estoque de uma loja. Em um menu deve ter as opções:

    cadastrar produto
    editar produto

    vender pruduto

    gerar relatório


Na opção de cadastro o usuário deve entrar com:

    nome do produto

    preço
    tipo


Para cada produto cadastrado deve ser gerado um código.

Na opção de editar deve permitir atualização do nome do produto.

Na opção vender produto deve registrar uma venda do produto.
E na opção gerar relatório deve mostrar o valor total ganho e a média por tipo de produto.

'''

def listarProdutos(itens):
    for p in itens:
        print(f"{p["id"]} - {p["nome"]} | {p["preco"] | p["tipo"]}")

opcao = 0
produtos = []
vendas = []
while opcao != 5:

    opcao = int(input("Entra com tua opção: \n1 - Cadastrar\n2 - Editar\n3- Vender\n4 - Relatorio\n5 - Sair\n"))
    if opcao == 1:
        nome = input("Entra com o nome do produto: ")
        preco = float(input("Entra com o preço do produto: "))
        tipo = input("Entra com o tipo do produto: ")

        produtos.append({"nome": nome, "preco": preco, "tipo": tipo, "id": len(produtos) + 1 })

    elif opcao == 2:
        listarProdutos(produtos)
        indice = int(input("Entra com o Id do produto: "))
        produtoSelecionado = produtos[indice - 1]
        novoNome = input(f"Entra com o novo nome ({produtoSelecionado["nome"]}):")
        produtoSelecionado["nome"] = novoNome
    
    elif opcao == 3:
        listarProdutos(produtos)
        indice = int(input("Entra com o Id do produto: "))
        produtoSelecionado = produtos[indice - 1]
        vendas.append(produtoSelecionado)
    
    elif opcao == 4:
        # valor total ganho e a média por tipo de produto
        valorTotal = 0
        for v in vendas:
            valorTotal = valorTotal + v["preco"]
        
        print(f"Total: {valorTotal}")

        tipos = []
        for p in produtos:
            if not p["tipo"] in tipos:
                tipos.append(p["tipo"])
        
        for t in tipos:
            soma = 0
            contador = 0
            for v in vendas:
                if v["tipo"] == t:
                    soma += v["preco"]
                    contador += 1
            media = soma / contador
            print(f"Média de {tipo}: {media}")
        
from Contacto import Contacto

def listarContactos():
    for contacto in contactos:
        print(contacto)

contactos = []
cadastro = True

while cadastro:
    opcao = input("Entra com a opção:\n1 - Cadastrar\n2 - Remover\n3 - Listar\n4 - buscar\n5 - Sair")
    opcao = int(opcao)
    if opcao == 1:
        nome = input("Entra com o nome: ")
        telefone = input("Entra com o telefone: ")
        email = input("Entra com o email: ")
        contactos.append(Contacto(nome, telefone, email))
    elif opcao == 2:
        listarContactos()
        nomeApagar = input("Entra com o nome para apagar: ")

        # del list(filter(lambda x: x.nome == nomeApagar, contactos))[0]

        for i in range(len(contactos)):
            if nomeApagar == contactos[i].nome:
                del contactos[i]
    elif opcao == 3:
        listarContactos()
    elif opcao == 4:
        busca = input("Entra com o termo de busca")
        for contacto in contactos:
            if contacto.buscar(busca):
                print(contacto)
    elif opcao == 5:
        cadastro = False
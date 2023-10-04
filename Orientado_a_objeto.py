def cadatrsr_cliente(clientes,nome,email,telefone):
    cliente = {
        'Nome' :nome,
        'Email' : email,
        'Telefone' : telefone
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    print("*************************************")
    print("\n")

def imprimir_cliente(clientes):
    for indice,cliente in enumerate(clientes):
        print(f"ID cliente {indice+1}")
        print(f"Nome {cliente['Nome']}")
        print(f"Email {cliente['Email']}")
        print(f"Telefone {cliente['Telefone']}")
        print("Cliente cadastrado com sucesso!")
        print("*************************************")
        print("\n")


clientes=[]
nome = input("Digite o nome: ")
email = input("Digite o email: ")
telefone = input("Digite o telefone: ")
cadatrsr_cliente(clientes,nome,email,telefone)
imprimir_cliente(clientes)
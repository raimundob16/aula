def cadastra_produto(produtos, nome, valor, quantidade, frete, imposto1, imposto2, imposto3, margem,custo,valor_venda):
    produto = {
        'Nome': nome,
        'Valor': valor,
        'Quantidade': quantidade,
        'Frete': frete,
        'Imposto1': imposto1,
        'Imposto2': imposto2,
        'Imposto3': imposto3,
        'Margem': margem,
        'Custo': custo,
        'Valor_venda': valor_venda  
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")
    print("*************************************")
    print("\n")

def imprimir_produto(produto):
    for indice, produto in enumerate(produto):
        print(f"ID Produto {indice + 1}")
        print(f"Nome {produto['Nome']}")
        print(f"Valor {produto['Valor']}")
        print(f"Quantidade {produto['Quantidade']}")
        print(f"Frete {produto['Frete']}")
        print(f"Imposto1 {produto['Imposto1']}")
        print(f"Imposto2 {produto['Imposto2']}")
        print(f"Imposto3 {produto['Imposto3']}")
        print(f"Margem {produto['Margem']}")
        print(f"Custo {produto['Custo']}")
        print(f"Valor da venda {produto['Valor_venda']}")
        print("*************************************")
        print("\n")

def atualizar_produto(produtos, indice, nome, valor, quantidade, frete, imposto1, imposto2, imposto3, margem,):
    if indice >= 0 and indice < len(produtos):
        produtos[indice]['Nome'] = nome
        produtos[indice]['Valor'] = valor
        produtos[indice]['Quantidade'] = quantidade
        produtos[indice]['Frete'] = frete
        produtos[indice]['Imposto1'] = imposto1
        produtos[indice]['Imposto2'] = imposto2
        produtos[indice]['Imposto3'] = imposto3
        produtos[indice]['Margem'] = margem
        print("Produto atualizado com sucesso!")
        print("*************************************")
        print("\n")

produtos = []

while True:
    print("1 Cadastrar produto")
    print("2 Imprimir produtos")
    print("3 Atualizar produto")
    print("4 Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do produto: ")
        valor = float(input("Digite o Valor do produto: "))
        quantidade = int(input("Digite a Quantidade: "))
        frete = float(input("Digite o Valor do frete: "))
        margem = float(input("Digite a Margem de lucro: "))
        imposto1 = float(input("Digite o Imposto 1: "))
        imposto2 = float(input("Digite o Imposto 2: "))
        imposto3 = float(input("Digite o Imposto 3: "))

        imposto1 = (valor * imposto1) / 100
        imposto2 = (valor * imposto2) / 100
        imposto3 = (valor * imposto3) / 100
        frete = frete / quantidade
        custo = valor + frete + imposto1 + imposto2 + imposto3
        valor_venda = custo + (custo * (margem / 100))

        cadastra_produto(produtos, nome, valor, quantidade, frete, imposto1, imposto2, imposto3, margem,valor_venda,custo)

    elif opcao == '2':
        imprimir_produto(produtos)

    elif opcao == '3':
        indice = int(input("Digite o ID do produto a ser atualizado: "))
        if 0 <= indice - 1 < len(produtos):
            nome = input("Digite o novo nome do produto: ")
            valor = float(input("Digite o novo Valor do produto: "))
            quantidade = float(input("Digite a nova Quantidade: "))
            frete = float(input("Digite o novo Valor do frete: "))
            margem = float(input("Digite a nova Margem de lucro: "))
            imposto1 = float(input("Digite o novo Imposto 1: "))
            imposto2 = float(input("Digite o novo Imposto 2: "))
            imposto3 = float(input("Digite o novo Imposto 3: "))

            imposto1 = (valor * imposto1) / 100
            imposto2 = (valor * imposto2) / 100
            imposto3 = (valor * imposto3) / 100
            frete= frete / quantidade
            custo = valor + frete+ imposto1 + imposto2 + imposto3
            valor_venda = custo + (custo * (margem / 100))

            atualizar_produto(produtos, indice - 1, nome, valor, quantidade, frete, imposto1, imposto2, imposto3)

    elif opcao == '4':
        break

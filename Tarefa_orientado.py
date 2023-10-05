def cadastra_produto(produtos,nome,valor,quantidade,frete,imposto1,imposto2,imposto3,margem,valor_custo,valor_venda):
    produto={
                'Nome' : nome,
                'Valor' : valor,
                'Quantidade' : quantidade,
                'Frete' : frete,
                'Imposto1' : imposto1,
                'Imposto2' : imposto2,
                'Imposto3' : imposto3,
                'Margem' : margem,
                'Valor_custo' : valor_custo,
                'Valor_venda' : valor_venda
            }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")
    print("*************************************")
    print("\n")

def imprimir_produto(produto):
    for indice,produto in enumerate(produto):
        print(f"ID Produto {indice+1}")
        print(f"Nome {produto['Nome']}")
        print(f"Valor {produto['Valor']}")
        print(f"Qantidade {produto['Qantidade']}")
        print(f"Frete {produto['Frete']}")
        print(f"Imposto1 {produto['Imposto1']}")
        print(f"Imposto2 {produto['Imposto2']}")
        print(f"Imposto3 {produto['Imposto3']}")
        print(f"Margem {produto['margem']}")
        print(f"Valor_custo {produto['valor_custo']}")
        print(f"Valor_venda {produto['valor_venda']}")
        print("Produto cadastrado com sucesso!")
        print("*************************************")
        print("\n")

def atualizar_produto(produtos,nome,valor,quantidade,frete,imposto1,imposto2,imposto3,margem,valor_custo,valor_venda):
    if indice >= len(produtos) and indice < len(produtos):
        produtos[indice]['Nome'] = nome
        produtos[indice]['Valor'] = valor
        produtos[indice]['Frete'] = frete
        produtos[indice]['Quantidade'] = quantidade
        produtos[indice]['Imposto1'] = imposto1
        produtos[indice]['Imposto2'] = imposto2
        produtos[indice]['Imposto3'] = imposto3
        produtos[indice]['Margem'] = margem
        produtos[indice]['Valor_custo'] = valor_custo
        produtos[indice]['Valor_venda'] = valor_venda
        print("Produto atualizado com sucesso!")
        print("*************************************")
        print("\n")

while True:
    print("1 cadstra de produto")
    print("2 Imprimir")
    print("3 Atualizar")
    print("4 sair")

    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        nome = int("Digite o nome do produto: ")
        valor = input("digite o Valor do produto: ")
        quantidade = input("digite a Quantidade: ")
        frete = input("digite o Valor do frete: ")
        margens_lucro = input("digite a Margem de lucro: ")
        imposto1 = input("digite o Imposto 1: ")
        imposto2 = input("digite o imposto 2: ")
        imposto3 = input("digite o imposto 3: ")
        margens_lucro = input("digite a margem de lucro: ")

        imposto1 = (valor * imposto1)/100
        imposto2 = (valor * imposto2)/100
        imposto3 = (valor * imposto2)/100
        frete = frete/quantidade
        custo = valor + frete + imposto1 + imposto2 + imposto3
        valor_venda = custo + (custo*(margens_lucro / 100))

        nome.append(nome)
        valor.append(valor)
        quantidade.append(quantidade)
        frete.append(frete)
        margens_lucro.append(margens_lucro)
        imposto1.append(imposto1)
        imposto2.append(imposto2)
        imposto3.append(imposto3)

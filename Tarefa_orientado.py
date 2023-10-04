while True:
    print("1 cadstra de produto")
    print("2 Imprimor")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        def cadstro_de_produto(produtos,nome,valor,quantidade,frete,imposto1,imposto2,imposto3,margem):
            produto={
                'Nome' : nome,
                'Valor' : valor,
                'Quantidade' : quantidade,
                'Frete' : frete,
                'Imposto1' : imposto1,
                'Imposto2' : imposto2,
                'Imposto3' : imposto3
                'Margem' : margem
            }
            icms = (valor * icms)/100
            ipi = (valor * ipi)/100
            cofis = (valor * cofis)/100
            frete = frete/quantidade
            custo = valor + frete + icms + ipi + cofis
            valor_venda = custo + (custo*(margem / 100))
            produto.append(produto)
            print("Produto cadastrado com sucesso!")
            print("*************************************")
            print("\n")
    elif opcao == "2":
        def imprimir_cliente(clientes):
            for indice,produto in enumerate(produtos):
                print(f"ID Produto {indice+1}")
                print(f"Nome {produto['Nome']}")
                print(f"Valor {produto['Valor']}")
                print(f"Qantidade {produto['Qantidade']}")
                print(f"Frete {produto['Frete']}")
                print(f"Imposto1 {produto['Imposto1']}")
                print(f"Imposto2 {produto['Imposto2']}")
                print(f"Imposto3 {produto['Imposto3']}")
                print("Produto cadastrado com sucesso!")
                print("*************************************")
                print("\n")
    
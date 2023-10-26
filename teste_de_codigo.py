import csv



# Cadastra o produto
def cadastra_produto(produtos, nome, valor, quantidade, frete, imposto1, imposto2, imposto3, margem):
    custo = valor + frete + (valor * imposto1) + (valor * imposto2) + (valor * imposto3)
    valor_venda = custo / (1 - margem)
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

# Salvar no CSV
def salvar_produtos(produtos):
    with open('arquivos.csv', mode='w', newline='') as arquivos_csv:
        writer = csv.writer(arquivos_csv)
        writer.writerow(["Nome", "Valor", "Quantidade", "Frete", "Imposto1", "Imposto2", "Imposto3", "Margem", "Custo", "Valor_venda"])
        for produto in produtos:
            writer.writerow([produto['Nome'], produto['Valor'], produto['Quantidade'], produto['Frete'], produto['Imposto1'], produto['Imposto2'], produto['Imposto3'], produto['Margem'], produto['Custo'], produto['Valor_venda'])

def deletar_produto(produtos, indice):
    if 0 <= indice < len(produtos):
        del produtos[indice]
        print("Produto deletado com sucesso!")
    else:
        print("Produto não encontrado, tente novamente.")

produtos = []

while True:
    opc = int(input(f"Bem-vindo ao sistema ESTOQUE, escolha uma opção: \n"
                    "1 - Cadastrar produto: \n"
                    "2 - Imprimir produtos cadastrados: \n"
                    "3 - Deletar produto: \n"
                    "4 - Sair do sistema de estoque\n"))

    if opc == 1:
        nome = input("Digite o nome: ")
        valor = float(input("Digite o valor: "))
        quantidade = int(input("Digite a quantidade: "))
        frete = float(input("Digite o frete: "))
        imposto1 = float(input("Digite o imposto 1 (%): ")) / 100
        imposto2 = float(input("Digite o imposto 2 (%): ")) / 100
        imposto3 = float(input("Digite o imposto 3 (%): ")) / 100
        margem = float(input("Digite a margem (%): ")) / 100

        cadastra_produto(produtos, nome, valor, quantidade, frete, imposto1, imposto2, imposto3, margem)

    elif opc == 2:
        for produto in produtos:
            print(produto)

    elif opc == 3:
        indice = int(input("Digite o ID do produto que deseja deletar: "))
        deletar_produto(produtos, indice)

    elif opc == 4:
        break

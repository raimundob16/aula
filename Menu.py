nome = []
valores = []
quantidade = []
frete = []
margens_lucro = []
icms = []
ipi = []
cofis = []
custo = []
valor_venda = []

while True:
    print("1 cadstra de produto")
    print("2 cadstra de produto")
    print("3 cadstra de produto")
   
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("digite o nome do produto")
        valor = input("digite o nome do produto")
        quantidade = input("digite o nome do produto")
        frete = input("digite o nome do produto")
        margens_lucro = input("digite o nome do produto")
        icms = input("digite o nome do produto")
        ipi = input("digite o nome do produto")
        cofis = input("digite o nome do produto")

        icms = (valor * icms)/100
        ipi = (valor * ipi)/100
        cofis = (valor * cofis)/100
        frete = frete/quantidade
        custo = valor + frete + icms + ipi + cofis
        valor_venda = custo + (custo*(margens_lucro / 100))

        nome.append(nome)
        valor.append(valor)
        quantidade.append(quantidade)
        frete.append(frete)
        margens_lucro.append(margens_lucro)
        icms.append(icms)
        ipi.append(ipi)
        cofis.append(cofis)
        print("cadasto reslizado com maestria")
    elif opcao =="2":
        if not nome:
            print("não tem produtos cadastrado")
        for i in range (len(nome)):
            print( f"Nome do produto,{nome[i]}")
            print( f"Valor do produto,{valor[i]}")
            print( f"Frete do produto,{frete[i]}")
            print( f"icms do produto,{icms[i]}")
            print( f"ipi do produto,{ipi[i]}")
            print( f"Cofis do produto,{cofis[i]}")
            print( f"Custo do produto,{custo[i]}")
            print( f"Valor venda do produto,{valor_venda[i]}")
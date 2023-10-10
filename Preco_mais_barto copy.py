produtos = []
precos = []

for i in range(3):
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos.append(produto)
    precos.append(preco)

indice_mais_barato = 0

for i in range(1, len(precos)):
    if precos[i] < precos[indice_mais_barato]:
        indice_mais_barato = i

print("O produto mais barato é:", produtos[indice_mais_barato])
print("Preço:", precos[indice_mais_barato])

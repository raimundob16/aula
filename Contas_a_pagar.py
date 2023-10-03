# Cria um dicionário para armazenar as contas
contas = {}

# Loop para cadastrar as contas
while True:
    descricao = input("Digite a descrição da conta (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário deseja sair
    if descricao.lower() == 'sair':
        break
    
    data = input("Digite a data da conta (formato DD/MM/AAAA): ")
    valor = float(input("Digite o valor da conta: "))
    
    # Extrai o dia da data
    dia = data.split("/")[0]
    
    # Verifica se o dia já existe no dicionário
    if dia in contas:
        contas[dia].append((descricao, data, valor))
    else:
        contas[dia] = [(descricao, data, valor)]

# Imprime as contas acumuladas por dia
for dia, lista_contas in contas.items():
    print(f"Data: {dia}")
    total_dia = 0
    for conta in lista_contas:
        descricao, data, valor = conta
        print(f"  Descrição: {descricao}, Data: {data}, Valor: R${valor:.2f}")
        total_dia += valor
    print(f"  Total do Dia: R${total_dia:.2f}")
    print()

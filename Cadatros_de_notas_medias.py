
#foi acrescentado a opção de lista alunos que achei que criei interessante de ter

def cadastrar_aluno(alunos, nome, nota1, nota2, nota3, nota4, media):
    aluno = {
        'Nome': nome,
        'Nota1': nota1,
        'Nota2': nota2,
        'Nota3': nota3,
        'Nota4': nota4,
        'Media': media
    }
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")
    print("*************************************")


def imprimir_notas(alunos):
    for indice, aluno in enumerate(alunos):
        print(f"ID aluno {indice + 1}")
        print(f"Nome: {aluno['Nome']}")
        print(f"Nota1: {aluno['Nota1']}")
        print(f"Nota2: {aluno['Nota2']}")
        print(f"Nota3: {aluno['Nota3']}")
        print(f"Nota4: {aluno['Nota4']}")
        print(f"Media: {aluno['Media']}")
        print("*************************************")

def editar_notas(alunos, indice, nome, nota1, nota2, nota3, nota4, media):
    if indice >= 0 and indice < len(alunos):
        alunos[indice]['Nome'] = nome
        alunos[indice]['Nota1'] = nota1
        alunos[indice]['Nota2'] = nota2
        alunos[indice]['Nota3'] = nota3
        alunos[indice]['Nota4'] = nota4
        alunos[indice]['Media'] = media
        print("Notas atualizadas com sucesso!")
        print("*************************************")

def deletar_notas(alunos, indice):
    if indice >= 0 and indice < len(alunos):
        del alunos[indice]
        print("Aluno deletado com sucesso!")
        print("*************************************")


def calcular_media(aluno):
    return media

def alunos_aprovados(alunos):
    for aluno in alunos:
        if aluno['Media'] >= 7:
            print(f"Aluno {aluno['Nome']} aprovado com média {aluno['Media']}")
        else:
            print(f"Não temos alunos aprovados! ")
            print("*************************************")

def alunos_reprovados(alunos):
    for aluno in alunos:
        if aluno['Media'] < 7:
            print(f"Aluno {aluno['Nome']} reprovado com média {aluno['Media']}")
        else:
            print(f"Não temos alunos reprovados! ")
            print("*************************************")
def alunos_alunos(alunos):
    for aluno in alunos:
        if aluno:
            print(f"Aluno {aluno['Nome']} ")
        else:
            print(f"Não temos alunos para lista! ")
            print("*************************************")

alunos = []

while True:
    print("1 - Cadastrar aluno")
    print("2 - Editar notas")
    print("3 - Deletar aluno")
    print("4 - Imprimir notas")
    print("5 - Listar alunos aprovados")
    print("6 - Listar alunos reprovados")
    print("7 - Listar alunos")
    print("8 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        nota3 = float(input("Digite a nota 3: "))
        nota4 = float(input("Digite a nota 4: "))
        
        media = (nota1+nota2+nota3+nota4)/4
        cadastrar_aluno(alunos, nome, nota1, nota2, nota3, nota4, media)
    elif opcao == '2':
        indice = int(input("Digite o ID do aluno para editar as notas: "))
        if 0 <= indice - 1 < len(alunos):
            nome = input("Digite o novo nome do aluno: ")
            nota1 = float(input("Digite a nova nota 1: "))
            nota2 = float(input("Digite a nova nota 2: "))
            nota3 = float(input("Digite a nova nota 3: "))
            nota4 = float(input("Digite a nova nota 4: "))
           
            media = (nota1+nota2+nota3+nota4)/4
            editar_notas(alunos, indice - 1, nome, nota1, nota2, nota3, nota4, media)
        else:
            print("Aluno não encontrado.")
    elif opcao == '3':
        indice = int(input("Digite o ID do aluno para deletar: "))
        if 0 <= indice - 1 < len(alunos):
            deletar_notas(alunos, indice - 1)
        else:
            print("Aluno não encontrado.")
    elif opcao == '4':
        imprimir_notas(alunos)
    elif opcao == '5':
        alunos_aprovados(alunos)
    elif opcao == '6':
        alunos_reprovados(alunos)
    elif opcao == '7':
        alunos_alunos(alunos)
    elif opcao == '8':
        break
    else:
        print("Opção inválida. Tente novamente.")




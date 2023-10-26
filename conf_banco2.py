import mysql.connector

config = mysql.connector.connect (
     host = "127.0.0.1",
     user = "root",
     password = "root",
     database= "emprestimo"
)

cursor = config.cursor()

def criar_cliente(nome, telefone, email):
    sql = "INSERT INTO cliente (nome, telefone, email) VALUES (%s, %s, %s)"
    val = (nome, telefone, email)
    cursor.execute(sql, val)
    config.commit()
    print("Cliente cadastrado com sucesso!")

def listar_cliente():
    cursor.execute("SELECT * FORM CLIENTE")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)

def atualizar_cliente(id_cliente, nome, telefoe, email):
    sql = "UPDATE cliente set nome = %s, telefone = %s, email = %s  WHERE id_cliente = %s"
    val = (nome, telefoe, email, id_cliente)
    cursor.execute(sql, val)
    config.commit()
    print("Cliente atualizado com sicesso! ")

def deletar_cliente(id_cliente):
    sql = "DELETE FROM cliente WHERE id_cliente = %s"
    val = (id_cliente,)
    cursor.execute(sql, val)
    config.commit()
    print("Cliente Deletado !")

while True:
    print("1 cadstra de cliente: ")
    print("2 cadstra de livro: ")
    print("3 cadstra de editora: ")
    print("4 cadstra de altor: ")
    print("5 Lista cliente: ")
    print("6 atualizar Cliente: ")
    print("7 deletar Cliente")
    print("8 sair ")
   
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
       
        nome= input("Digite o nome do cliete: ")
        telefone = input("Digite o Telefone: ")
        email = input("Digite o E-mail: ")
        
        criar_cliente(nome, telefone, email)
    
    
    elif opcao == "5":
        listar_cliente

    elif opcao == "6":
        id_cliente = input("Digite o ID do cliente: ")
        nome= input("Digite o nome do cliete: ")
        telefone = input("Digite o Telefone: ")
        email = input("Digite o E-mail: ")
        atualizar_cliente (id_cliente, nome, telefone, email)

    elif opcao =="7":
        id_cliente= input("Digite o id do cliente")
        deletar_cliente(id_cliente)
   
    elif opcao =="8":
        break
import sqlite3

master_password = "master"

# Creating the connection to the db / Creating a db if it does not exist:
# Criando conexão com o bd / Criando um bd se ele não existir:
conexao = sqlite3.connect("passwords.db")


# Creating a Table users in db if it does not exist:
# Creando uma Tabela users no bd se ela não existir:
table_users = ("""CREATE TABLE IF NOT EXISTS users (
        service TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        perm_id INTEGER,
        FOREIGN KEY (perm_id) REFERENCES perm(id)
    );
""")

count = -1
b = 3
while count != 3:
    password = input("Enter your master password: ")
    if password == master_password:
        break
    elif b != 0:
        print(f"\nIncorrect password !(You have {b} more chances)\
 Try again please: \n")
        count = count + 1
        b = b - 1
        continue
    else:
        print('\nDue to many attempts the program will close!\
 Try again later.')
        exit()


# Handling the exception and presenting it at the terminal:
# Pegando a excessão e apresentando no terminal:
def menu():

    print("**********************************"),
    print("* 1 : Insert a new password      *"),
    print("* 2 : List saved services        *"),
    print("* 3 : Recover a password         *"),
    print("* 4 : Quit                       *"),
    print("**********************************")


# recovering password according to the informed service:
# Recuperando senha de acordo com o serviço informado:
def get_password(service):
    cursor.execute(f"""
        SELECT username, password FROM users
        WHERE service = '{service}'
    """)

    if cursor.rowcount == 0:
        print("Service not found!\
(Use the operation 'l' to view the services)")
    else:
        for user in cursor.fetchall():
            print(user)


# Inserting datas into the Table:
# Inserindo dados na tabela:
def insert_password(service, username, password):
    cursor.execute(f"""
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    """)
    conexao.commit()


# Showing registered services:
# Mostrando serviços cadastrados:
def show_services():
    cursor.execute("""
        SELECT service FROM users
    """)
    for service in cursor.fetchall():
        print(service)


# Trying to connect to the db:
# Tentando conectar ao bd:
try:
    cursor = conexao.cursor()
    cursor.execute(table_users)
except EnvironmentError as e:
    print(f'Error: {e}')


# Receiving the user's choise:
# Recebendo a escolha do usuario:
while True:
    menu()
    user_op = input("Select the desired operation: ")

    if user_op == "1":
        service = input("Insert the service: ")
        username = input("Insert the user's name: ")
        password = input("Insert now the desired password: ")
        print("\nSENHA CADASTRADA COM SUCESSO! \n\n")
        insert_password(service, username, password)
    elif user_op == "2":
        show_services()
        break
    elif user_op == "3":
        service = input("Inform the service to recover\
 the corresponding password: ")
        get_password(service)
    elif user_op == "4":
        break
    else:
        print("\nOpção inválida! Tente Novamente..")
        continue

conexao.close()

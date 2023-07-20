import os

database = []


def create_client():
    os.system("clear")
    print("-------------Cadastrar cliente --------------")
    username = input("Nome: ")
    address = input("Endereço: ")
    birthday = input("Data de nascimento (DD/MM/YYYY): ")
    database.append([username, address, birthday])
    print("---------------------------------------------")


def list_client_by_name():
    print("---------------------------------------------")
    print("listing client...")
    print("---------------------------------------------")


def list_all_clients():
    os.system("clear")
    print("------------- CLIENTES ATIVOS --------------")
    print(database)
    print("------------- CLIENTES ATIVOS --------------")
    option = input("Deseja Voltar ao menu principal? s/n")


def update_client_by_name():
    print("---------------------------------------------")
    print("updating client...")
    print("---------------------------------------------")


def delete_client_by_name():
    print("---------------------------------------------")
    print("deleting client...")
    print("---------------------------------------------")


while True:
    os.system("clear")
    print("---------------------------------------------")
    print("[1] - Cadastrar ...")
    print("[2] - Lista por nome ...")
    print("[3] - Listar todos clientes...")
    print("[4] - Atualizar por nome ...")
    print("[5] - Deletar por nome ...")
    print("[0] - Sair ...")
    print("---------------------------------------------")
    option = input("Opção: ")  # str

    if int(option) == 1:
        create_client()
    if int(option) == 3:
        list_all_clients()

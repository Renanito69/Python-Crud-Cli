from time import sleep
import os
import colorama as color


def limpar():
    os.system('cls')


def salvar(lista):
    with open("lista.txt", "w") as arquivo:
        for item in lista:
            arquivo.write(item + "\n")


def carregar():
    if not os.path.exists("lista.txt"):
        return []

    nova_lista = []
    with open("lista.txt", "r") as arquivo:
        for item in arquivo:
            nova_lista.append(item.strip())
    return nova_lista


def buscar_item(lista, nomeBuscar):
    for nome in lista:
        if nomeBuscar in nome:
            print(nome)


def adicionar_item(lista, palavra):

    if palavra in lista:
        print("Esse item ja existe")
    else:
        lista.append(palavra)
        print(color.Fore.GREEN + "Item adicionado")
        salvar(lista)
        sleep(1)


def editar_item(lista):
    for num, item in enumerate(lista):
        print(f"{num+1} - {item}")
    option = int(input("Qual item deseja editar: (escolha a numeração)"))
    novoOpition = str(input("Qual o novo item deseja adicionar: "))
    antigo = lista[option - 1]
    lista[option - 1] = novoOpition
    salvar(lista)
    print(f"O item editado:", color.Fore.YELLOW +
          f"'{antigo}'", "->", color.Fore.GREEN + f"'{novoOpition}'")
    sleep(1)


def remover_item(lista, remover_item):
    print(f"Item ", color.Fore.YELLOW +
          f"'{lista[remover_item-1]}'", "removido da lista")
    lista.pop(remover_item-1)
    print(color.Fore.RED + "Item Removido")
    sleep(0.8)
    return salvar(lista)


def exibindo_menu():
    print('''
░██████╗░███████╗██████╗░███████╗███╗░░██╗░█████╗░██╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝░██╔════╝██╔══██╗██╔════╝████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██████╔╝█████╗░░██╔██╗██║██║░░╚═╝██║███████║██║░░██║██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██╔══██╗██╔══╝░░██║╚████║██║░░██╗██║██╔══██║██║░░██║██║░░██║██╔══██╗
╚██████╔╝███████╗██║░░██║███████╗██║░╚███║╚█████╔╝██║██║░░██║██████╔╝╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

░█████╗░██████╗░██╗░░░██╗██████╗░
██╔══██╗██╔══██╗██║░░░██║██╔══██╗
██║░░╚═╝██████╔╝██║░░░██║██║░░██║
██║░░██╗██╔══██╗██║░░░██║██║░░██║
╚█████╔╝██║░░██║╚██████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═════╝░
''')


def exibir_escolhas():
    print("0 - Sair e Salvar")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Listar item")
    print("4 - Recarregar lista")
    print("5 - Buscar item")
    print("6 - Editar a lista")


def escolher_opcao(lista):
    option = int(input("Escolha uma opção: "))
    if option == 1:
        print("Adicionar:", end='')
        palavra = str(input(color.Fore.YELLOW + " ")).lower()
        adicionar_item(lista, palavra=palavra)
    elif option == 2:
        for num, item in enumerate(lista):
            print(f"{num+1} - {item}")

        escolha = int(input("Em qual posiçao esta o item que quer remover? "))
        remover_item(lista, escolha)
    elif option == 3:
        for num, item in enumerate(lista):
            print(f"{num+1} - {item}")
        sleep(2)
    elif option == 4:
        lista = carregar()
        print(color.Fore.GREEN + "Lista Carregada!")
        sleep(0.7)
    elif option == 5:
        nome_Busca = str(input("Buscar: "))
        buscar_item(lista, nome_Busca)
    elif option == 6:
        editar_item(lista)
    elif option == 0:
        print(color.Fore.GREEN + "Salvando")
        sleep(2)
        print(color.Fore.RED + "Saindo")
        sleep(1)
        return lista, True
    return lista, False


def main(lista):
    color.init(autoreset=True)

    exibindo_menu()
    exibir_escolhas()
    return escolher_opcao(lista)


# Programa principal
if __name__ == '__main__':
    lista = carregar()
    while True:
        lista, sair = main(lista)
        if sair:
            break

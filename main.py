from time import sleep
import os


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
        print("Item adicionado")


def editar_item(lista):
    for num, item in enumerate(lista):
        print(f"{num+1} - {item}")
    option = int(input("Qual item deseja editar: (escolha a numeração)"))
    novoOpition = str(input("Qual o novo item deseja adicionar: "))
    antigo = lista[option - 1]
    lista[option - 1] = novoOpition
    print(f"O item editado: '{antigo}' -> '{novoOpition}'")
    return


lista = carregar()

while True:
    print('''
    0 - Sair e Salvar
    1 - Adicionar item
    2 - Remover item
    3 - Listar item
    4 - Recarregar lista
    5 - Buscar item
    6 - Editar a lista''')

    option = int(input("Escolha uma opção: "))

    if option == 1:
        palavra = str(input("Adicionar: "))
        adicionar_item(lista, palavra=palavra)

    elif option == 2:
        escolha = int(input("Em qual posiçao esta o item que quer remover? "))
        lista.pop(escolha-1)

    elif option == 3:
        for num, item in enumerate(lista):
            print(f"{num+1} - {item}")
        sleep(3)
    elif option == 4:
        lista = carregar()
        print("Lista Carregada!")
    elif option == 5:
        nome_Busca = str(input("Buscar: "))
        buscar_item(lista, nome_Busca)
    elif option == 6:
        editar_item(lista)
    elif option == 0:
        print("Salvando")
        # verificacao_lista(lista)
        salvar(lista)
        sleep(2)
        print("Saindo")
        sleep(1)
        break

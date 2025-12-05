🚀 Python CRUD CLI — Agenda de Contatos no Terminal

Um projeto simples e funcional em Python, utilizando listas, dicionários, funções,
looping principal, e limpeza do terminal, para criar uma agenda de contatos via CLI.

Ideal para iniciantes que querem treinar CRUD, organização de código,
e interação com o usuário no terminal.

📌 Funcionalidades

✔ Adicionar contatos

✔ Listar contatos

✔ Buscar contatos por nome

✔ Remover contatos

✔ Interface limpa com ASCII Art

✔ Menu interativo

✔ Tratamento de erros (inputs inválidos)

✔ Armazenamento em memória (lista)

🧠 O que esse projeto treina?

Manipulação de listas e dicionários

Construção de menus interativos

Funções bem separadas (clean code)

Entrada de dados pelo terminal

Estrutura de loop principal (while True)

Tratamento de exceções com try/except

Organização de um CRUD completo

Perfeito para quem está aprendendo:

📘 Python básico → intermediário

📌 Estruturas de dados

🔁 Fluxo lógico

🖼 Exemplo do Menu

1 - Adicionar contato

2 - Remover contato

3 - Listar todos os contatos

4 - Buscar contatos

0 - Sair

📁 Estrutura do Código

Python-Crud-Cli/

│

├── agenda.py     # código principal

└── README.md     # documentação (este arquivo)

▶ Como executar

Certifique-se de ter Python 3 instalado:

python --version


Execute o script:

python agenda.py


O menu será exibido automaticamente no terminal.

📚 Código Principal (simplificado)

    lista_contatos = list()

    while True:

      print("1 - Adicionar contato")
      print("2 - Remover contato")
      print("3 - Listar todos os contatos")
      print("4 - Buscar contatos")
      print("0 - Sair")

      option = int(input("Escolha: "))

      if option == 1:
          adicionar_contatos(lista_contatos)
      elif option == 2:
          remover_contato(lista_contatos)
      elif option == 3:
          listar_contato(lista_contatos)
      elif option == 4:
          buscar_contato(lista_contatos)
      elif option == 0:
          break

🔧 Melhorias Futuras (sugestões)

💾 Persistência em arquivo (JSON ou TXT)

🖥️ Versão com interface Tkinter

🚀 Porta para API com Flask/FastAPI

🔍 Melhor filtro de busca

✔️ Ordenação alfabética automática

🧑‍💻 Autor

Renan Cristian

Estudante de ADS e desenvolvedor em evolução 🚀

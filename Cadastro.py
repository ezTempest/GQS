def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Avaliar cadastro")
    print("6 - Sair")


def cadastrar_pessoa(nomes, idades, emails):
    """Cadastra uma nova pessoa no sistema."""
    global qtd

    if qtd >= 3:
        print("Limite de pessoas atingido.")
        return

    nome = input("Nome: ")

    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida.")
        return

    email = input("E-mail: ")

    if nome == "" or email == "":
        print("Nome e e-mail são obrigatórios.")
        return

    nomes.append(nome)
    idades.append(idade)
    emails.append(email)

    qtd += 1
    print("Pessoa cadastrada com sucesso.")


def consultar_pessoa(nomes, idades, emails):
    """Consulta uma pessoa pelo nome."""
    nomeBusca = input("Digite o nome para consultar: ")

    encontrado = False

    for i in range(len(nomes)):
        if nomes[i].lower() == nomeBusca.lower():
            print("-------------------------")
            print("Nome:", nomes[i])
            print("Idade:", idades[i])
            print("E-mail:", emails[i])
            print("-------------------------")
            encontrado = True

    if not encontrado:
        print("Pessoa não encontrada.")


def alterar_pessoa(nomes, idades, emails):
    """Altera os dados de uma pessoa cadastrada."""
    nomeBusca = input("Digite o nome da pessoa: ")

    for i in range(len(nomes)):
        if nomes[i].lower() == nomeBusca.lower():
            print("Pessoa encontrada.")

            novoNome = input("Novo nome: ")

            try:
                novaIdade = int(input("Nova idade: "))
            except ValueError:
                print("Idade inválida.")
                return

            novoEmail = input("Novo e-mail: ")

            nomes[i] = novoNome
            idades[i] = novaIdade
            emails[i] = novoEmail

            print("Dados alterados com sucesso.")
            return

    print("Pessoa não encontrada.")


def listar_pessoas(nomes, idades, emails):
    """Lista todas as pessoas cadastradas."""
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada.")
        return

    print("=========================")
    print(" PESSOAS CADASTRADAS")
    print("=========================")

    for i in range(len(nomes)):
        print("-------------------------")
        print("Nome:", nomes[i])
        print("Idade:", idades[i])
        print("E-mail:", emails[i])
        print("-------------------------")


def avaliar_cadastro(nomes, idades):
    """Avalia a quantidade de maiores e menores de idade."""
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada.")
        return

    maiores = 0
    menores = 0

    for idade in idades:
        if idade >= 18:
            maiores += 1
        else:
            menores += 1

    print("=========================")
    print(" AVALIAÇÃO DO CADASTRO")
    print("=========================")
    print("Total de pessoas:", len(nomes))
    print("Maiores de idade:", maiores)
    print("Menores de idade:", menores)

nomes = []
idades = []
emails = []
qtd = 0
op = 0
while op != 6:
    exibir_menu()
    op = int(input("Escolha uma opcao: "))
    if op == 1:
        cadastrar_pessoa(nomes, idades, emails)
    elif op == 2:
        consultar_pessoa(nomes, idades, emails)
    elif op == 3:
        alterar_pessoa(nomes, idades, emails)
    elif op == 4:
        listar_pessoas(nomes, idades, emails)
    elif op == 5:
        avaliar_cadastro(nomes, idades)
    elif op == 6:
        print("Saindo...")
    else: print("Opcao invalida")
print("Fim do programa")
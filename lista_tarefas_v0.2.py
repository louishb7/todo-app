tarefas = []


def exibir_cabecalho():
    print("~=" * 20)
    print(f"{'Sistema BunkerMode':^35}")
    print("~=" * 20)


def criar_tarefas():
    dados = {}
    dados["missao"] = input("Missão: ")
    while True:
        try:
            prioridade_temp = int(input("Nível de prioridade (1 a 3): "))

            if not 1 <= prioridade_temp <= 3:
                raise ValueError

            dados["prioridade"] = prioridade_temp
            break

        except ValueError:
            print("Entrada inválida! Escolha um número entre 1 a 3.")

    dados["descriçao"] = input("Informe a missão para o seu soldado: ")
    dados["status"] = "Aguardando Recruta"

    tarefas.append(dados.copy())
    dados.clear()
    print("--- Missão cadastrada com sucesso! ---")


def listar_tarefas():
    """
    => Função que permite listar tarefas e marcar elas como concluídas.
    """
    print(f"{' =>   OBJETIVOS DO DIA    <=':<20}")
    print("=" * 35)
    for index, item in enumerate(tarefas, start=1):
        if item["prioridade"] == 1:
            print(f"= > Faça!! Prioridade máxima. < =")
            print(f"{index}. {item['missao'].capitalize()}")
            print(f"-" * 35)

        elif item["prioridade"] == 2:
            print(f"Deve fazer!")
            print(f"{index}. {item['missao'].capitalize()}")
            print(f"-" * 35)

        else:
            print(f"Baixa prioridade.")
            print(f"{index}. {item['missao'].capitalize()}")
            print(f"-" * 35)

    try:
        escolha = int(input("Escolha uma missão para mais detalhes: "))
        if 1 <= escolha <= len(tarefas):
            detalhar = tarefas[escolha - 1]
            print("=" * 35)
            print(
                f"Missão => {detalhar['missao']}\nPrioridade => {detalhar['prioridade']}\n"
                f"Descrição => {detalhar['descriçao']}\nStatus => {detalhar['status']}"
            )
            print("=" * 35)

    except ValueError:
        print("Opção inválida!")


def remover_tarefas():
    for index, item in enumerate(tarefas, start=1):
        print(f"{index}. {item['missao'].capitalize()}")
    print("-" * 35)

    try:
        escolha = int(input("Escolha uma tarefa a ser removida."))
        if 1 <= escolha <= len(tarefas):
            removida = tarefas.pop(escolha - 1)
            print(f"Missão '{removida['missao']}'\nRemovida com sucesso!")

    except ValueError:
        print("Opção inválida!")


def exibir_relatorio():
    pass


def menu_principal():
    """
    => Função com o Menu principal do Programa.
    """
    while True:

        print("1. = > Adicionar tarefa")
        print("2. = > Listar tarefas/Marcar Concluído")
        print("3. = > Remover Tarefa")
        print("4. = > Relatório do dia")
        print("5. = > Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tarefas()
        elif opcao == "2":
            if not tarefas:
                print("Crie uma tarefa primeiro.")
            else:
                listar_tarefas()
        elif opcao == "3":
            if not tarefas:
                print("Crie uma tarefa primeiro.")
            else:
                remover_tarefas()
        elif opcao == "4":
            if not tarefas:
                print("Crie uma tarefa primeiro.")
            else:
                exibir_relatorio()
        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida! Escolha novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    exibir_cabecalho()
    menu_principal()

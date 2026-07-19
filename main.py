from inventario import InventarioTI
from modelos import (
    AplicacaoWeb,
    Notebook,
    Roteador,
    Servidor,
    TipoAtivo,
    Vulnerabilidade,
)

# ===================
# PROGRAMA PRINCIPAL
# ===================

inventario = InventarioTI()

inventario.carregar_json()

while True:
    print("-" * 30)
    print("INVENTÁRIO DE TI")
    print("-" * 30)

    print("""Escolha uma das opções abaixo:
[1] Cadastrar ativo
[2] Buscar ativo
[3] Atualizar ativo
[4] Remover ativo
[5] Adicionar vulnerabilidade
[6] Ver vulnerabilidades
[7] Listar ativos
[8] Encerrar o programa""")

    try:
        escolha = int(input("Indique a sua escolha: "))
    except ValueError:
        print("Opção inválida! Digite apenas números.")
        continue

    match escolha:

        # ==================================
        # 1 - CADASTRAR ATIVO
        # ==================================

        case 1:
            print("\nQual tipo de ativo deseja cadastrar?")
            print(f"[{TipoAtivo.NOTEBOOK.value}] Notebook")
            print(f"[{TipoAtivo.SERVIDOR.value}] Servidor")
            print(f"[{TipoAtivo.ROTEADOR.value}] Roteador")
            print(f"[{TipoAtivo.APLICACAO_WEB.value}] Aplicação Web")

            try:
                tipo = int(input("Escolha o tipo: "))
            except ValueError:
                print("Tipo inválido! Digite apenas números.")
                continue

            try:
                id_ativo = int(input("ID do ativo: "))
            except ValueError:
                print("O ID deve ser um número.")
                continue

            nome = input("Nome do ativo: ").strip()
            responsavel = input("Responsável: ").strip()
            setor = input("Setor: ").strip()

            if not nome or not responsavel or not setor:
                print("Erro: nome, responsável e setor não podem ficar vazios.")
                continue

            match tipo:
                case TipoAtivo.NOTEBOOK.value:
                    novo_ativo = Notebook(
                        id_ativo,
                        nome,
                        responsavel,
                        setor
                    )

                case TipoAtivo.SERVIDOR.value:
                    novo_ativo = Servidor(
                        id_ativo,
                        nome,
                        responsavel,
                        setor
                    )

                case TipoAtivo.ROTEADOR.value:
                    novo_ativo = Roteador(
                        id_ativo,
                        nome,
                        responsavel,
                        setor
                    )

                case TipoAtivo.APLICACAO_WEB.value:
                    novo_ativo = AplicacaoWeb(
                        id_ativo,
                        nome,
                        responsavel,
                        setor
                    )

                case _:
                    print("Tipo de ativo inválido!")
                    continue

            if inventario.cadastrar_ativo(novo_ativo):
                inventario.salvar_json()
                print("Ativo cadastrado com sucesso!")

        # ==================================
        # 2 - BUSCAR ATIVO
        # ==================================

        case 2:
            print("\nBuscar ativo por:")
            print("[1] ID")
            print("[2] Nome")

            opcao_busca = input("Escolha uma opção: ").strip()

            match opcao_busca:
                case "1":
                    try:
                        id_ativo = int(input("Informe o ID do ativo: "))
                    except ValueError:
                        print("O ID deve ser um número.")
                        continue

                    ativo = inventario.buscar_ativo(id_ativo)

                case "2":
                    nome = input("Informe o nome do ativo: ").strip()

                    if not nome:
                        print("O nome não pode ficar vazio.")
                        continue

                    ativo = inventario.buscar_ativo_nome(nome)

                case _:
                    print("Opção de busca inválida.")
                    continue

            if ativo:
                print(ativo)
            else:
                print("Ativo não encontrado.")

        # ==================================
        # 3 - ATUALIZAR ATIVO
        # ==================================

        case 3:
            try:
                id_ativo = int(
                    input("Informe o ID do ativo que deseja atualizar: ")
                )
            except ValueError:
                print("O ID deve ser um número.")
                continue

            nome = input("Novo nome do ativo: ").strip()
            responsavel = input("Novo responsável: ").strip()
            setor = input("Novo setor: ").strip()

            if not nome or not responsavel or not setor:
                print("Erro: os campos não podem ficar vazios.")
                continue

            if inventario.atualizar_ativo(
                id_ativo,
                nome,
                responsavel,
                setor
            ):
                inventario.salvar_json()

        # ==================================
        # 4 - REMOVER ATIVO
        # ==================================

        case 4:
            try:
                id_ativo = int(
                    input("Informe o ID do ativo que deseja remover: ")
                )
            except ValueError:
                print("O ID deve ser um número.")
                continue

            if inventario.remover_ativo(id_ativo):
                inventario.salvar_json()

        # ==================================
        # 5 - ADICIONAR VULNERABILIDADE
        # ==================================

        case 5:
            try:
                id_ativo = int(
                    input(
                        "Informe o ID do ativo que receberá "
                        "a vulnerabilidade: "
                    )
                )
            except ValueError:
                print("O ID deve ser um número.")
                continue

            ativo = inventario.buscar_ativo(id_ativo)

            if not ativo:
                print("Ativo não encontrado.")
                continue

            descricao = input(
                "Descrição da vulnerabilidade: "
            ).strip()

            categoria = input("Categoria: ").strip()
            severidade = input("Severidade: ").strip()
            status = input("Status: ").strip()

            if not descricao or not categoria or not severidade or not status:
                print("Erro: nenhum campo pode ficar vazio.")
                continue

            nova_vulnerabilidade = Vulnerabilidade(
                descricao,
                categoria,
                severidade,
                status
            )

            ativo.adicionar_vulnerabilidade(
                nova_vulnerabilidade
            )

            inventario.salvar_json()

            print("Vulnerabilidade adicionada com sucesso.")

        # ==================================
        # 6 - VER VULNERABILIDADES
        # ==================================

        case 6:
            try:
                id_ativo = int(input("Informe o ID do ativo: "))
            except ValueError:
                print("O ID deve ser um número.")
                continue

            ativo = inventario.buscar_ativo(id_ativo)

            if not ativo:
                print("Ativo não encontrado.")
                continue

            if not ativo.vulnerabilidades:
                print(
                    "Este ativo não possui vulnerabilidades cadastradas."
                )
            else:
                print(
                    f"\nVulnerabilidades do ativo {ativo.nome}:"
                )

                for vulnerabilidade in ativo.vulnerabilidades:
                    print(vulnerabilidade)

        # ==================================
        # 7 - LISTAR ATIVOS
        # ==================================

        case 7:
            inventario.listar_ativos()

        # ==================================
        # 8 - ENCERRAR
        # ==================================

        case 8:
            print("Encerrando o programa...")
            break

        # ==================================
        # OPÇÃO INVÁLIDA
        # ==================================

        case _:
            print("Opção inválida!")


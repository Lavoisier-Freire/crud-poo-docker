import json
from enum import Enum

# =========================
# DECLARAÇÃO DE CLASSES
# =========================


class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    APLICACAO_WEB = 4


class Vulnerabilidade:
    def __init__(self, descricao, categoria, severidade, status):
        self.descricao = descricao
        self.categoria = categoria
        self.severidade = severidade
        self.status = status

    def __str__(self):
        return (f'>> A vulnerabilidade "{self.descricao}" pertence à categoria "{self.categoria}",'
                f' com grau de severidade "{self.severidade}" e apresenta o status "{self.status}"')

    def to_dict(self):
        return {
            "descricao": self.descricao,
            "categoria": self.categoria,
            "severidade": self.severidade,
            "status": self.status
        }


class AtivoTI:
    def __init__(self, id_ativo, nome, responsavel, setor):
        self.id_ativo = id_ativo
        self.nome = nome
        self.responsavel = responsavel
        self.setor = setor
        self.vulnerabilidades = []

    def adicionar_vulnerabilidade(self, vulnerabilidade):  # > Method
        self.vulnerabilidades.append(vulnerabilidade)

    def __str__(self):
        return (f'>> O ativo "{self.nome}", apresenta ID "{self.id_ativo}"'
                f' e tem como responsável o(a) "{self.responsavel}", do setor "{self.setor}"')

    def to_dict(self):
        return {
            "id_ativo": self.id_ativo,
            "tipo": self.__class__.__name__,
            "nome": self.nome,
            "responsavel": self.responsavel,
            "setor": self.setor,
            "vulnerabilidades": [v.to_dict() for v in self.vulnerabilidades]
        }


class AtivoTI:
    def __init__(self, id_ativo, nome, responsavel, setor):
        self._id_ativo = id_ativo
        self._nome = nome
        self._responsavel = responsavel
        self._setor = setor
        self._vulnerabilidades = []

    # ==========================
    # GETTERS E SETTERS
    # ==========================

    @property
    def id_ativo(self):
        return self._id_ativo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, novo_responsavel):
        self._responsavel = novo_responsavel

    @property
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, novo_setor):
        self._setor = novo_setor

    @property
    def vulnerabilidades(self):
        return self._vulnerabilidades

    # ==========================
    # MÉTODOS
    # ==========================

    def adicionar_vulnerabilidade(self, vulnerabilidade):
        self._vulnerabilidades.append(vulnerabilidade)

    def __str__(self):
        return (f'>> O ativo "{self.nome}" apresenta ID "{self.id_ativo}" '
                f'e tem como responsável o(a) "{self.responsavel}", '
                f'do setor "{self.setor}".')

    def to_dict(self):
        return {
            "id_ativo": self.id_ativo,
            "tipo": self.__class__.__name__,
            "nome": self.nome,
            "responsavel": self.responsavel,
            "setor": self.setor,
            "vulnerabilidades": [
                vulnerabilidade.to_dict()
                for vulnerabilidade in self.vulnerabilidades
            ]
        }

class Notebook(AtivoTI):
    def __init__(self, id_ativo, nome, responsavel, setor):
        super().__init__(id_ativo, nome, responsavel, setor)

    def __str__(self):
        return (
            f'>> O notebook "{self.nome}" apresenta o ID "{self.id_ativo}" '
            f'e tem como responsável o(a) "{self.responsavel}", '
            f'do setor "{self.setor}".'
        )

class Servidor(AtivoTI):
    def __init__(self, id_ativo, nome, responsavel, setor):
        super().__init__(id_ativo, nome, responsavel, setor)

    def __str__(self):
        return (f'>> O servidor "{self.nome}" apresenta ID "{self.id_ativo}"'
                f'e tem como responsável o "{self.responsavel}", do setor "{self.setor}".')


class Roteador(AtivoTI):
    def __init__(self, id_ativo, nome, responsavel, setor):
        super().__init__(id_ativo, nome, responsavel, setor)

    def __str__(self):
        return (f'>> O roteador "{self.nome}", apresente ID "{self.id_ativo}"'
                f'e tem como responsável o "{self.responsavel}", do setor "{self.setor}".')


class AplicacaoWeb(AtivoTI):
    def __init__(self, id_ativo, nome, responsavel, setor):
        super().__init__(id_ativo, nome, responsavel, setor)

    def __str__(self):
        return (f'>> A aplicação web "{self.nome}", apresente ID "{self.id_ativo}",'
                f'e tem como responsável o(a) "{self.responsavel}", do setor "{self.setor}".')


class InventarioTI:
    def __init__(self):
        self.ativos = {}

    def cadastrar_ativo(self, ativo):
        if ativo.id_ativo in self.ativos:
            print("Erro: já existe um ativo cadastrado com esse ID.")
            return False

        self.ativos[ativo.id_ativo] = ativo
        return True

    def buscar_ativo(self, id_ativo):
        return self.ativos.get(id_ativo)

    def buscar_ativo_nome(self, nome):
        for ativo in self.ativos.values():
            if ativo.nome.lower() == nome.lower():
                return ativo

        return None

    def listar_ativos(self):
        if not self.ativos:
            print("Nenhum ativo cadastrado.")
            return

        for ativo in self.ativos.values():
            print(ativo)

    def remover_ativo(self, id_ativo):
        if id_ativo in self.ativos:
            del self.ativos[id_ativo]
            print("Ativo removido com sucesso.")
            return True

        print("Ativo não encontrado.")
        return False

    def atualizar_ativo(self, id_ativo, nome, responsavel, setor):
        ativo = self.buscar_ativo(id_ativo)

        if ativo:
            ativo.nome = nome
            ativo.responsavel = responsavel
            ativo.setor = setor
            print("Ativo atualizado com sucesso.")
            return True

        print("Ativo não encontrado.")
        return False

    def salvar_json(self):
        dados = []

        for ativo in self.ativos.values():
            dados.append(ativo.to_dict())

        with open("ativos.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def carregar_json(self):
        try:
            with open("ativos.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            for item in dados:
                tipo = item["tipo"]

                match tipo:
                    case "Notebook":
                        ativo = Notebook(
                            item["id_ativo"],
                            item["nome"],
                            item["responsavel"],
                            item["setor"]
                        )

                    case "Servidor":
                        ativo = Servidor(
                            item["id_ativo"],
                            item["nome"],
                            item["responsavel"],
                            item["setor"]
                        )

                    case "Roteador":
                        ativo = Roteador(
                            item["id_ativo"],
                            item["nome"],
                            item["responsavel"],
                            item["setor"]
                        )

                    case "AplicacaoWeb":
                        ativo = AplicacaoWeb(
                            item["id_ativo"],
                            item["nome"],
                            item["responsavel"],
                            item["setor"]
                        )

                    case _:
                        continue

                for vuln in item.get("vulnerabilidades", []):
                    vulnerabilidade = Vulnerabilidade(
                        vuln["descricao"],
                        vuln["categoria"],
                        vuln["severidade"],
                        vuln["status"]
                    )

                    ativo.adicionar_vulnerabilidade(vulnerabilidade)

                self.cadastrar_ativo(ativo)

        except FileNotFoundError:
            pass


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



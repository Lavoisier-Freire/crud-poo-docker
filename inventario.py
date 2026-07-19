import json

from modelos import (
    AplicacaoWeb,
    Notebook,
    Roteador,
    Servidor,
    Vulnerabilidade,
)

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
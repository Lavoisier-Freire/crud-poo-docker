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
                f' e tem como responsável o(a) "{self.responsavel}", '
                f' do setor "{self.setor}".')

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
            f' e tem como responsável o(a) "{self.responsavel}", '
            f' do setor "{self.setor}".'
        )

class Servidor(AtivoTI):
    def __init__(self, id_ativo, nome, responsavel, setor):
        super().__init__(id_ativo, nome, responsavel, setor)

    def __str__(self):
        return (f'>> O servidor "{self.nome}" apresenta ID "{self.id_ativo}"'
                f' e tem como responsável o "{self.responsavel}", do setor "{self.setor}".')


class Roteador(AtivoTI):
    def __init__(self, id_ativo, nome, responsavel, setor):
        super().__init__(id_ativo, nome, responsavel, setor)

    def __str__(self):
        return (f'>> O roteador "{self.nome}", apresenta ID "{self.id_ativo}"'
                f' e tem como responsável o "{self.responsavel}", do setor "{self.setor}".')


class AplicacaoWeb(AtivoTI):
    def __init__(self, id_ativo, nome, responsavel, setor):
        super().__init__(id_ativo, nome, responsavel, setor)

    def __str__(self):
        return (f'>> A aplicação web "{self.nome}", apresenta ID "{self.id_ativo}",'
                f' e tem como responsável o(a) "{self.responsavel}", do setor "{self.setor}".')

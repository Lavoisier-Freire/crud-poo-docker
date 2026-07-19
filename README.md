# Sistema de Inventário de TI

Projeto acadêmico desenvolvido durante a graduação em **Cibersegurança** na **Universidade Federal de Uberlândia (UFU)**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)

> Aplicação desenvolvida em **Python**, utilizando **Programação Orientada a Objetos (POO)**, persistência de dados em **JSON**, controle de versão com **Git e GitHub** e conteinerização com **Docker**.

---

## Objetivo do Projeto

Desenvolver um sistema para gerenciamento de ativos de Tecnologia da Informação (TI) e das vulnerabilidades associadas a esses ativos, aplicando conceitos de Programação Orientada a Objetos, persistência de dados em JSON e conteinerização com Docker.

---

## Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- JSON
- Docker
- Git
- GitHub

---

## Funcionalidades

- Cadastro de ativos de TI
- Busca de ativos por identificador (ID)
- Busca de ativos por nome
- Atualização de informações dos ativos
- Remoção de ativos
- Cadastro de vulnerabilidades
- Visualização das vulnerabilidades associadas
- Persistência automática dos dados em arquivo JSON

---

## Estrutura do Projeto

```text
.
├── main.py
├── inventario.py
├── modelos.py
├── ativos.json
├── Dockerfile
├── .gitignore
└── README.md
```

---

## Organização do Código

O projeto foi organizado em módulos para facilitar sua manutenção e reutilização:

- **main.py**: ponto de entrada da aplicação e interface com o usuário.
- **inventario.py**: gerenciamento do inventário e das operações sobre os ativos.
- **modelos.py**: definição das classes utilizadas pela aplicação.
- **ativos.json**: armazenamento persistente das informações cadastradas.

---

## Como Executar o Projeto

### Execução Local

Clone o repositório:

```bash
git clone git@github.com:Lavoisier-Freire/crud-poo-docker.git
```

Acesse a pasta do projeto:

```bash
cd crud-poo-docker
```

Execute a aplicação:

```bash
python main.py
```

### Execução com Docker

Construir a imagem:

```bash
docker build -t inventario-ti .
```

Criar e iniciar o contêiner:

```bash
docker run -dit --name inventario-ti-container inventario-ti
```

Executar a aplicação:

```bash
docker exec -it inventario-ti-container python main.py
```

Verificar os contêineres:

```bash
docker ps -a
```

---

## Conceitos Aplicados

Durante o desenvolvimento deste projeto foram aplicados os seguintes conceitos:

- Programação Orientada a Objetos (POO)
- Herança
- Encapsulamento
- Polimorfismo
- Persistência de dados em JSON
- Controle de versão com Git e GitHub
- Conteinerização com Docker

---

## Autor

**Lavoisier Freire**

Projeto desenvolvido durante a graduação em **Cibersegurança** na **Universidade Federal de Uberlândia (UFU)**.
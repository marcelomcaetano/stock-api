# API de Cadastro de Ações (Stock API)

## Descrição

Esta é uma API RESTful desenvolvida em Python com Flask para realizar o cadastro e gerenciamento de operações de compra de ações no mercado financeiro. Os dados são persistidos em um banco de dados SQLite.

A API segue as melhores práticas de desenvolvimento, incluindo uma arquitetura limpa, documentação automática com Swagger (OpenAPI) e conformidade com a PEP 8.

## Tecnologias Utilizadas

- Python 3.12.5
- Flask
- Flask-OpenAPI3 (para documentação Swagger)
- Flask-SQLAlchemy (para interação com o banco de dados)
- Pydantic (para validação de dados)
- SQLite

## Estrutura do Projeto

O projeto é organizado seguindo princípios de Clean Architecture para garantir a separação de responsabilidades e facilitar a manutenção:

- `app/database/models.py`: Define a estrutura da tabela de ações.
- `app/schemas/`: Contém os esquemas Pydantic para validação das requisições e formatação das respostas.
- `app/routes/stock.py`: Implementa os endpoints da API (`/stocks`).
- `run.py`: Ponto de entrada para executar a aplicação.

## Instalação e Execução

Siga os passos abaixo para configurar e executar o ambiente de desenvolvimento localmente.

### Pré-requisitos

- Python 3.12 ou superior
- `pip` (gerenciador de pacotes do Python)
- `virtualenv` (ferramenta para criação de ambientes virtuais)

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-seu-repositorio>
    cd stock-api
    ```

2.  **Crie e ative um ambiente virtual:**
    É uma forte recomendação usar ambientes virtuais para isolar as dependências do projeto.

    * **No Linux ou macOS:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    * **No Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    Este comando irá iniciar o servidor de desenvolvimento. O banco de dados `database.db` será criado automaticamente no primeiro acesso.
    ```bash
    python run.py
    ```

### Acessando a API

-   **Servidor da API:** `http://127.0.0.1:5000`
-   **Documentação Swagger (OpenAPI):** `http://127.0.0.1:5000/openapi`

A documentação interativa do Swagger permite que você visualize e teste todos os endpoints diretamente pelo navegador.
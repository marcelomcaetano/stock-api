import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_openapi3 import OpenAPI, Info
# ADIÇÃO: Importa a classe CORS da nova biblioteca
from flask_cors import CORS

# Define informações da API para a documentação Swagger.
info = Info(title="Stock API", version="1.0.0", description="API para cadastro de ações")

# Instancia o objeto OpenAPI, que é uma extensão do Flask.
app = OpenAPI(__name__, info=info)

# ADIÇÃO: Habilita o CORS para a aplicação.
# Por padrão, isso permite requisições de todas as origens para todas as rotas.
# Para desenvolvimento, isso é suficiente e seguro.
CORS(app)

# Configurações da aplicação.
# Define o caminho base do projeto.
basedir = os.path.abspath(os.path.dirname(__file__))
# Configura a URI do banco de dados SQLite.
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, '../database.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desativa o rastreamento de modificações do SQLAlchemy.

# Inicializa a extensão SQLAlchemy com a aplicação Flask.
db = SQLAlchemy(app)

# Importa a blueprint da API de 'stock' e a registra na aplicação.
from app.routes.stock import api as stock_api
app.register_api(stock_api)

# NOTA DE ARQUITETURA PARA PRODUÇÃO:
# Em um ambiente de produção, é mais seguro especificar quais origens são permitidas.
# Você substituiria 'CORS(app)' por algo como:
#
# cors = CORS(app, resources={
#     r"/stocks/*": {
#         "origins": ["http://meu-site-de-producao.com", "https://meu-site-de-producao.com"]
#     }
# })
#
# Isso garante que apenas o seu site oficial possa fazer requisições à sua API.

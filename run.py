# run.py

from app import app, db

# O bloco with app.app_context() garante que a aplicação Flask esteja
# configurada corretamente antes de interagir com o banco de dados.
# db.create_all() cria todas as tabelas definidas nos modelos (neste caso, a tabela 'stock')
# caso elas ainda não existam no banco de dados.
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento do Flask.
    # O modo debug=True ativa o recarregamento automático ao salvar arquivos e
    # exibe informações detalhadas de erro no navegador.
    # Em um ambiente de produção, debug deve ser False.
    app.run(debug=True)
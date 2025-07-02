from flask_openapi3 import APIBlueprint, Tag
from sqlalchemy.exc import IntegrityError

from app import db
from app.database.models import Stock
from app.schemas.stock import (
    StockCreateSchema,
    StockUpdateSchema,
    StockViewSchema,
    ListStockSchema,
    StockPathSchema,
    StockSearchSchema,
    present_stocks
)
from app.schemas.error import ErrorSchema

stock_tag = Tag(name="Stock", description="Cadastro e gerenciamento de compras de ações")
api = APIBlueprint('stock_api', __name__, url_prefix='/stocks', abp_tags=[stock_tag])


@api.post(
    '/',
    summary="Cadastra uma nova compra de ação",
    responses={"201": StockViewSchema, "400": ErrorSchema, "409": ErrorSchema}
)
def add_stock(body: StockCreateSchema):
    """ Adiciona uma nova compra de ação ao banco de dados. """
    stock = Stock(
        purchase_date=body.purchase_date,
        average_price=body.average_price,
        quantity=body.quantity,
        stock_code=body.stock_code.upper()
    )
    try:
        db.session.add(stock)
        db.session.commit()
        return stock.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return {"message": f"Ocorreu um erro inesperado: {e}"}, 400


@api.put(
    '/<int:stock_id>',
    summary="Atualiza uma operação de compra de ação existente",
    responses={"200": StockViewSchema, "404": ErrorSchema}
)
def update_stock(path: StockPathSchema, body: StockUpdateSchema):
    """
    Atualiza os dados de uma operação de compra de ação com base no ID fornecido.
    Apenas os campos fornecidos no corpo da requisição serão atualizados.
    """
    stock = db.get_or_404(Stock, path.stock_id)
    
    # O método 'dict' com exclude_unset=True garante que apenas os campos
    # que o cliente enviou serão considerados para a atualização.
    data = body.dict(exclude_unset=True)
    
    for key, value in data.items():
        setattr(stock, key, value)
        
    db.session.add(stock)
    db.session.commit()
    
    return stock.to_dict(), 200


@api.get(
    '/',
    summary="Lista todas as compras de ações cadastradas",
    responses={"200": ListStockSchema}
)
def get_all_stocks():
    """ Retorna uma lista de todas as compras de ações. """
    stocks = db.session.execute(db.select(Stock).order_by(Stock.purchase_date.desc())).scalars().all()
    if not stocks:
        return {"stocks": []}, 200
    return present_stocks(stocks)


@api.get(
    '/search',
    summary="Busca por operações de uma ação específica",
    description="Filtra as operações de compra pelo código da ação fornecido via query parameter.",
    responses={"200": ListStockSchema}
)
def search_stocks(query: StockSearchSchema):
    """
    Busca por ações com base no código fornecido.
    Exemplo de chamada: /stocks/search?code=PETR4
    """
    stock_code = query.code
    query_builder = db.select(Stock)
    if stock_code:
        query_builder = query_builder.where(Stock.stock_code == stock_code.upper())
    
    query_builder = query_builder.order_by(Stock.purchase_date.desc())
    stocks = db.session.execute(query_builder).scalars().all()
    
    if not stocks:
        return {"stocks": []}, 200
    return present_stocks(stocks)


@api.get('/<int:stock_id>', summary="Retorna uma compra específica por ID", responses={"200": StockViewSchema, "404": ErrorSchema})
def get_stock_by_id(path: StockPathSchema):
    """ Retorna uma única compra de ação com base no seu ID. """
    stock = db.get_or_404(Stock, path.stock_id, description="Registro de compra não encontrado.")
    return stock.to_dict(), 200


@api.delete('/<int:stock_id>', summary="Remove uma compra de ação", responses={"204": {}, "404": ErrorSchema})
def delete_stock(path: StockPathSchema):
    """ Remove um registro de compra de ação do banco de dados. """
    stock = db.get_or_404(Stock, path.stock_id, description="Registro de compra não encontrado para exclusão.")
    try:
        db.session.delete(stock)
        db.session.commit()
        return "", 204
    except Exception as e:
        db.session.rollback()
        return {"message": f"Erro ao remover o registro: {e}"}, 400

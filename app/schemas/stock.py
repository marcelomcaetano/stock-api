from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

# Schema base para a ação, sem o ID, usado para a criação de um novo registro.
class StockCreateSchema(BaseModel):
    average_price: float = Field(..., gt=0, description="Preço médio da ação na compra.")
    quantity: int = Field(..., gt=0, description="Quantidade de ações compradas.")
    stock_code: str = Field(..., min_length=4, max_length=10, description="Código da ação (ex: PETR4).")
    purchase_date: Optional[date] = Field(date.today(), description="Data da compra da ação.")

# Schema para a atualização de uma ação. Todos os campos são opcionais.
class StockUpdateSchema(BaseModel):
    average_price: Optional[float] = Field(None, gt=0, description="Novo preço médio da ação.")
    quantity: Optional[int] = Field(None, gt=0, description="Nova quantidade de ações.")
    stock_code: Optional[str] = Field(None, min_length=4, max_length=10, description="Novo código da ação.")
    purchase_date: Optional[date] = Field(None, description="Nova data da compra.")

# Schema para visualização de uma ação, inclui todos os campos do banco de dados.
class StockViewSchema(BaseModel):
    id: int = Field(..., description="ID único da operação de compra.")
    purchase_date: date = Field(..., description="Data da compra.")
    average_price: float = Field(..., description="Preço médio.")
    quantity: int = Field(..., description="Quantidade.")
    stock_code: str = Field(..., description="Código da ação.")

# Schema para listar todas as ações cadastradas.
class ListStockSchema(BaseModel):
    stocks: List[StockViewSchema]

# Schema para validação do parâmetro de busca (query parameter).
class StockSearchSchema(BaseModel):
    code: Optional[str] = Field(None, description="Código da ação a ser buscada.")

# Schema para validação de parâmetros de caminho (path parameters).
class StockPathSchema(BaseModel):
    stock_id: int = Field(..., description="ID da operação de compra.")

# Função auxiliar para apresentar as ações no formato correto.
def present_stocks(stocks: List['Stock']) -> dict:
    return {
        "stocks": [stock.to_dict() for stock in stocks]
    }

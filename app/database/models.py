# app/database/models.py

from app import db
from sqlalchemy import Integer, String, Float, Date
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

# Classe que representa a tabela 'stock' no banco de dados.
# Herda de db.Model, a classe base para todos os modelos do Flask-SQLAlchemy.
class Stock(db.Model):
    __tablename__ = 'stock'

    # Coluna 'id': Chave primária, inteira e autoincrementável.
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    # Coluna 'purchase_date': Data da compra da ação. Não pode ser nula.
    # O padrão é a data atual.
    purchase_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    
    # Coluna 'average_price': Preço médio da ação. Número de ponto flutuante.
    # Não pode ser nulo.
    average_price: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Coluna 'quantity': Quantidade de ações compradas. Inteiro e não pode ser nulo.
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    
    # Coluna 'stock_code': Código da ação (ex: 'PETR4'). String com no máximo 10 caracteres.
    # Não pode ser nulo.
    stock_code: Mapped[str] = mapped_column(String(10), nullable=False)

    def to_dict(self):
        """Converte o objeto Stock para um dicionário."""
        return {
            "id": self.id,
            "purchase_date": self.purchase_date.isoformat(),
            "average_price": self.average_price,
            "quantity": self.quantity,
            "stock_code": self.stock_code
        }
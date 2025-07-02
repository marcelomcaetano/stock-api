# app/schemas/error.py

from pydantic import BaseModel, Field

# Schema padrão para retornar mensagens de erro, como "Não encontrado" (404).
class ErrorSchema(BaseModel):
    message: str = Field(..., description="Descrição do erro.")
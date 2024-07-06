from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

from schemas import ComentarioSchema


class ProdutoSchema(BaseModel):
    """ Define a estrutura de um novo produto a ser inserido """
    nome: str = "Banana Prata"
    quantidade: Optional[int] = 12
    valor: float = 12.50


class ProdutoBuscaSchema(BaseModel):
    """ Define a estrutura de busca baseada no nome do produto """
    nome: str = "Teste"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada """
    produtos: List[ProdutoSchema]


class ProdutoViewSchema(BaseModel):
    """ Define a estrutura de retorno detalhado de um produto """
    id: int = 1
    nome: str = "Banana Prata"
    quantidade: Optional[int] = 12
    valor: float = 12.50
    total_comentarios: int = 1
    comentarios: List[ComentarioSchema]


class ProdutoDelSchema(BaseModel):
    """ Define a estrutura de retorno após uma requisição de remoção """
    message: str
    nome: str

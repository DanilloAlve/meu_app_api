from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base, Comentario


class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    quantidade = Column(Integer)
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    # Relacionamento entre o produto e os comentários associados a ele
    comentarios = relationship("Comentario")

    def __init__(self, nome: str, quantidade: int, valor: float,
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            nome: Nome do produto.
            quantidade: Quantidade esperada para o produto.
            valor: Valor esperado para o produto.
            data_insercao: Data de quando o produto foi inserido na base.
        """
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario: Comentario):
        """ Adiciona um novo comentário ao Produto """
        self.comentarios.append(comentario)

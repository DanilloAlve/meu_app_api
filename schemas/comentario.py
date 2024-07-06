from pydantic import BaseModel


class ComentarioSchema(BaseModel):
    """ Define a estrutura de um novo comentário a ser inserido """
    produto_id: int = 1
    texto: str = "Só comprar se o preço realmente estiver bom!"

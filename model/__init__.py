from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# Importando os elementos definidos no modelo
from model.base import Base
from model.comentario import Comentario
from model.produto import Produto

# Path para o diretório do banco de dados
db_path = "database/"
if not os.path.exists(db_path):
    os.makedirs(db_path)

# URL de acesso ao banco de dados SQLite local
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# Cria a engine de conexão com o banco de dados
engine = create_engine(db_url, echo=False)

# Instancia um criador de sessão para a conexão com o banco
Session = sessionmaker(bind=engine)

# Cria o banco de dados se ele não existir
if not database_exists(engine.url):
    create_database(engine.url) 

# Cria as tabelas do banco de dados se elas não existirem
Base.metadata.create_all(engine)

# Configurar o alembic

# Instalar a biblioteca
# pip install sqlalchemy alembic

# No terminal inicie o alembic
# python -m alembic init alembic

# Configurando a conexão com o db
# ---------------------------------

# Abra o arquivo alembic.ini
# e procure a linha com essa informação (provavelmente na linha 89):
# sqlalchemy.url = driver://user:pass@localhost/dbname

# Conectando o alembic ao sqlalchemy
# ----------------------------------

# Abre o arquivo:
# alembic/env.py

# Importe a Base no arquivo env.py
# from models import Base
# Encontre a linha com:
# target_metadata = None
# e altere para:
# target_metadata = Base.metadata
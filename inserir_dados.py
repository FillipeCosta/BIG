import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Definir os dados de conexão com o banco de dados (PostgreSQL como exemplo)
DATABASE_URL = 'postgresql://postgres:admin@localhost/BIGDATA'

# Criar engine de conexão
engine = create_engine(DATABASE_URL)

# Criar sessão
Session = sessionmaker(bind=engine)
session = Session()

# Passo 1: Ler o arquivo CSV
# dtype={'Quantidade': 'int64', 'Valor Total': 'int64', 'Percentual': 'int64'}
df = pd.read_csv('storage/JunhoRosa.csv') 

# Passo 2: Inserir os dados no banco de dados usando SQLAlchemy
df.to_sql('produtos_vendas', con=engine, if_exists='append', index=False)

# Confirmar a inserção
session.commit()

# Fechar a sessão
session.close()

print("Dados inseridos com sucesso no banco de dados!")

import psycopg2
import pandas as pd

# Caminho para o arquivo CSV
csv_file_path = 'storage/sua_planilha_sem_acento.csv'

# Ler o CSV com pandas usando 'latin-1' para evitar erros de codificação
df = pd.read_csv(csv_file_path,  encoding="utf-8", sep = ',')

print(df.head())

# Conectar ao PostgreSQL
try:
    # Criando a conexão
    conn = psycopg2.connect(
        host="localhost",      # Ou IP do servidor PostgreSQL
        database="BIGDATA",  # Nome do banco de dados
        user="postgres",    # Nome de usuário
        password="admin",# Senha do usuário
        port="5432"            # Porta padrão do PostgreSQL
    )
    
    cursor = conn.cursor()
    print("Conexão ao banco de dados estabelecida com sucesso.")

    # Inserir os dados do DataFrame no banco de dados
    for index, row in df.iterrows():
        cursor.execute('''
            INSERT INTO produtos_vendas (item, quantidade, valor_total, percentual)
            VALUES (%s, %s, %s, %s);
        ''', (row['Itens'], row['Quantidade'], row['Valor Total'], row['Percentual']))

    # Fazer commit das inserções
    conn.commit()
    print(f"{len(df)} registros inseridos no banco de dados.")

    # Fechar cursor e conexão
    cursor.close()
    conn.close()
    print("Conexão fechada.")

except Exception as error:
    print(f"Erro ao conectar ou inserir dados: {error}")
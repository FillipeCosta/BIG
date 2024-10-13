import psycopg2
from psycopg2 import sql

# Definindo os parâmetros de conexão
conexao = None
try:
    # Criando a conexão
    conexao = psycopg2.connect(
        host="localhost",      # Ou IP do servidor PostgreSQL
        database="BIGDATA",  # Nome do banco de dados
        user="postgres",    # Nome de usuário
        password="admin",# Senha do usuário
        port="5432"            # Porta padrão do PostgreSQL
    )

    # Criando um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Criando uma tabela chamada 'exemplo'
    cursor.execute('''    
        CREATE TABLE IF NOT EXISTS produtos_vendas (
            id SERIAL PRIMARY KEY,
            item VARCHAR(255),
            quantidade INT,
            valor_total DECIMAL(10, 2),
            percentual DECIMAL(5, 2)
        );
    ''')

    print("Tabela 'produtos_vendas' criada com sucesso.")

    # Inserindo um registro na tabela
    # cursor.execute('''
    #     INSERT INTO exemplo (nome, idade) VALUES (%s, %s);
    # ''', ("Maria", 30))

    # # Fazer commit das mudanças
    conexao.commit()

    # print("Dados inseridos com sucesso.")

    # Consultando os dados da tabela
    # cursor.execute('SELECT * FROM exemplo;')
    # rows = cursor.fetchall()

    # print("Dados da tabela 'exemplo':")
    # for row in rows:
    #     print(row)

    # Fechando o cursor
    cursor.close()

except Exception as error:
    print(f"Erro ao conectar ou executar operações: {error}")

finally:
    # Fechar a conexão com o banco de dados
    if conexao is not None:
        conexao.close()
        print("Conexão fechada.")

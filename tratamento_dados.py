import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Conectando ao banco de dados
engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/BIGDATA')

df = pd.read_sql_query("SELECT * FROM produtos_vendas", engine)

# Ver primeiras linhas
print(df.head())

# Estatísticas descritivas
print(df.describe())

# Verificar por valores faltantes
print(df.isnull().sum())

# Tratar valores faltantes
df.fillna(method='ffill', inplace=True)  # Preencher com o último valor válido

# Codificar variáveis categóricas
df['categoria'] = df['categoria'].astype('category').cat.codes

from sklearn.model_selection import train_test_split

X = df.drop('coluna_objetivo', axis=1)
y = df['coluna_objetivo']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error

predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("MSE:", mse)

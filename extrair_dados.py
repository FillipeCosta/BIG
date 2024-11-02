import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/BIGDATA')

df = pd.read_sql_query("SELECT * FROM produtos_vendas", engine)

# Exemplo: gráfico de vendas ao longo do tempo

df.groupby('item')['quantidade'].sum().plot(kind='line')
plt.title('Vendas ao longo do tempo')
# plt.show()

# Gráfico de valor total por mês
df.groupby('mes')['valor_total'].sum().plot(kind='line')
plt.title('Valor Total por Mês')
# plt.show()

# One-hot encoding para variáveis categóricas
df_encoded = pd.get_dummies(df, columns=['item', 'mes'])

# Verificando o resultado
# print(df_encoded.head())



# Definindo variáveis de entrada (features) e saída (target)
X = df_encoded.drop(columns=['quantidade'])  # Todas as colunas exceto 'quantidade'
y = df_encoded['quantidade']  # Alvo

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando o modelo Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliação do erro do modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
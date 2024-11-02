from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

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

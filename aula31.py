#➡️Nós importamos a função LinearRegression da biblioteca sklearn, criamos um objeto chamado model apartir dessa função. E então enviando os parâmetros de treino na função fit (assim: model.fit(X_train_scaled, y_train)) nós conseguimos treinar o modelo. 

#➡️Usando a função predict e enviando como parâmetro o conjunto de teste (X_test_scaled) a gente conseguiu fazer as predições desse conjunto. 

#➡️E então partimos para uma parte muito importante de qualquer modelo de machine learning que é a avaliação do modelo, para saber se está bom ou ruim (ou mais ou menos, ou médio, ou excelente, ou … enfim, vocês entenderam, certo?😂) Focamos em três métricas principais para avaliação de modelos de regressão: 

#MSE (Mean Squared Error), MAE (Mean Absolute Error) e R² (R-squared). Com os resultados nós concluímos que para um modelo real de produção nosso modelo não seria aceitável. 



## primeiro importar a biblioteca
from sklearn.linear_model import LinearRegression

from aula30 import X_test_scaled

model = LinearRegression()

## treinar o modelo
model.fit(X_train_scaled, y_train)
## fazer as predições
y_pred = model.predict(X_test_scaled)
## avaliar o modelo
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'MSE: {mse}')
print(f'MAE: {mae}')
print(f'R²: {r2}')


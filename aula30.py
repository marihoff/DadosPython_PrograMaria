dados [['idade', 'genero', 'nao branca', 'tempo de experiencia', 'numero de funcionarios', 'nivel de ensino', 'insatisfacao']].head()

dados.columns

dados = pd.get_dummies(dados, columns = ['genero', 'setor', 'novo nivel', 'regiao onde mora'], drop_first = True)

## teste e treino
X = dados.drop(['salario'], axis = 1)
y = dados['salario']

## import

from sklearn.model_selection import train_test_split    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

## vai normalizar os dados para o modelo de regressão linear
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scalar.fit_transform(X_train)
X_train_scaled = scaler.transform(X_train)

X_test_scaled = scaler.transform(X_test)




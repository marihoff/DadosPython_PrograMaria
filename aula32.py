#E pra finalizar🤩

#➡️Plotamos um gráfico dos valores reais versus os valores preditos pelo modelo e conseguimos perceber que até certo valor de salário, os valores preditos e os reais tem uma certa sintonia. Porém para valores muito altos de salários, as predições são muito distantes. 

#➡️Para conseguir analisar melhor o modelo, nós pegamos os coeficientes (pesos) de cada atributo, assim a gente conseguiu avaliar quais atributos tiveram mais peso positivo ou negativo para o resultado do modelo. Fizemos um gráfico bem bonito pra deixar mais visual essa questão dos coeficientes e conseguimos observar quais atributos pesaram mais para o negativo e quais pesaram mais para o positivo. 

#➡️Para finalizar, nós fizemos uma reflexão de que o modelo que nós treinamos foi utilizado para análise. Buscando entender no mundo real de hoje o que influencia o salário, olhamos os coeficientes e o que pesa para negativo e positivo. 

#💭Se um modelo para estimar o salário de uma pessoa, para ser usado na vida real, por exemplo, o salário da equipe da programaria vai ser estimado por um modelo, a gente teria que ter muito cuidado com ética para não reproduzir os vieses do mundo real.


from xml.parsers.expat import model

import matplotlib.pyplot as plt

from aula30 import X_train
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel('Valores Reais')
plt.ylabel('Valores Preditos')
plt.title('Valores Reais vs Valores Preditos')
plt.plot([y.min(y_test), y.max(y_test)], [y.min(y_pred), y.max(y_pred)], 'r--')  # Linha de referência
plt.show()

nomes_atributos = X_train.columns

pd.dataframe(model.coef_, index=nomes_atributos, columns=['Coeficiente']).sort_values(by='Coeficiente', ascending=False).plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Importância dos Atributos (Coeficientes)')
plt.xlabel('Atributos')
plt.ylabel('Valor do Coeficiente')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



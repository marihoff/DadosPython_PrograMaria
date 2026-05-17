import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

plt.figure()
sns.countplot(data = dados, x = 'genero', palette = 'pastel')
plt.title('Contagem de Gênero')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.show()



salario_por_idade = dados.groupby('idade')['salario'].mean().reset_index()
plt.figure()
sns.lineplot(data = salario_por_idade, x = 'idade', y = 'salario', marker = 'o')
plt.title('Salário Médio por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário Médio')
plt.grid()
plt.show()





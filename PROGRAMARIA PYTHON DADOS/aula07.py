## Valores discrepantes (outliers)

lista_idades = [20, 22, 21, 19, 23, 120, 18, 21]
media = np.mean(lista_idades) # média é afetada por valores discrepantes

##calcular desvio padrão

desvio_padrao = np.std(lista_idades) # desvio padrão é afetado por valores discrepantes

media + 3*desvio_padrao #limite superior para identificar outliers

media - 3*desvio_padrao #limite inferior para identificar outliers

##quartis divide o dado em quatro partes iguais

import matplotlib.pyplot as plt

plt.boxplot(lista_idades) #boxplot para visualizar os outliers

plt.bloxplot(dados['idade']) #boxplot para visualizar os outliers na coluna de idade do dataframe   

Q1 = dados['idade'].quantile(0.25) #primeiro quartil

Q3 = dados['idade'].quantile(0.75) #terceiro quartil

IQR = Q3 - Q1 #intervalo interquartil

limite_inferior = Q1 - 1.5*IQR #limite inferior para identificar outliers

limite_superior = Q3 + 1.5*IQR #limite superior para identificar outliers

outliers = dados[(dados['idade'] < limite_inferior) | (dados['idade'] > limite_superior)] #identificar outliers


## remover os dados discrepantes

dados_sem_outliers = dados[(dados['idade'] >= limite_inferior) & (dados['idade'] <= limite_superior)] #remover outliers da coluna de idade






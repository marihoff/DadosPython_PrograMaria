#Analise estatistica de dados > biblioteca numpy

import numpy as np

lista_dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

np.sum(lista_dados) #soma dos dados

len(lista_dados) #quantidade de dados   

np.mean(lista_dados) #media dos dados

np.sum(lista_dados) / len(lista_dados) #media dos dados

media=np.mean(lista_dados)
print("media aritmedica:", media)


#mediana = valor central
np.median(lista_dados) #mediana dos dados


lista_dados.sort() #ordenar os dados
np.median(lista_dados) #mediana dos dados

#moda = valor mais frequente
lista_dados['idade'].mode() #moda dos dados

#desvio padrao = medida de dispersao dos dados
lista_dados['idade'].std() #desvio padrao dos dados

lista_dados['idade'].min() #valor minimo dos dados

lista_dados[lista_dados['genero'] == 'masculino']['idade'].max() #valor maximo dos dados para homens  



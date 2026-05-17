# Uso da biblioteca pandas
##Para instalar no terminal > pip install pandas openpyxl
import pandas as pd  

#ler excel
df = pd.read_excel('D:\PROGRAMARIA PYTHON DADOS\planilha_modulo3.xlsx')

#ver 5 linhas da tabela, se colocar numero 10 dentro do parentes olha 10 linhas primeiras
df.head()

df.info() #mostra o tipo de dado de cada coluna 

df.describe() #mostra a média, desvio padrão, min, max e os quartis das colunas numéricas   

df.tail() #mostra as últimas 5 linhas da tabela, se colocar numero 10 dentro do parentes olha 10 linhas últimas

df.shape #mostra o número de linhas e colunas da tabela

len(df) #mostra o número de linhas da tabela

df.columns #mostra o nome das colunas da tabela

df.info() #mostra o tipo de dado de cada coluna e se tem valores nulos

##Documentação do pandas: https://pandas.pydata.org/docs/user_guide/cookbook.html


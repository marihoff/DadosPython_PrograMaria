## Correlação, diferentes funções para dados discretos e contínuos

## Se quanto mais a pessoa envelhece, mais ela ganha, isso é uma correlação positiva
## Se quanto mais a pessoa envelhece, menos ela ganha, isso é uma correlação negativa
## Se não há relação entre idade e salário, isso é uma correlação nula
## Correlação de Pearson para dados contínuos
import numpy as np
import pandas as pd
dados = pd.read_csv('dados.csv') #carregar os dados de um arquivo CSV
correlacao_pearson = dados['idade'].corr(dados['salario'], method='pearson') #calcular a correlação de Pearson entre idade e salário
## Correlação de Spearman para dados discretos
correlacao_spearman = dados['nivel'].corr(dados['salario'], method='spearman') #calcular a correlação de Spearman entre nível e salário
## Correlação de Kendall para dados discretos
correlacao_kendall = dados['nivel'].corr(dados['salario'], method
='kendall') #calcular a correlação de Kendall entre nível e salário



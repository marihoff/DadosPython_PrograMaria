import pandas as pd
dados = pd.read_csv('analise_dados_mod7_dados.csv') ##importar a tabela
dados.head()

dados.columns
dados['qual situação atual de trabalho?'].value_counts()

dados = dados[dados['qual situação atual de trabalho?'] == 'Empregado (CLT)']

dados['cor/raca/etnia'].value_counts()

## retirar os números com dados pequenos como outra, indígena, prefiro não informar, etc.
lista_retirar = ['Outra', 'Indígena', 'Prefiro não informar', 'Não sei informar', 'Parda']

dados[dados['cor/raca/etnia'].isin(lista_retirar)]['cor/raca/etnia'].value_counts()

dados['nao branca'] = dados['cor/raca/etnia'].apply(lambda x: 1 if x!= 'Branca' else 0)

##ver coluna de tempo de experiencia
dados['quanto tempo de experiencia na area de dados voce tem?'].value_counts()
dados['Tempo de experiencia'] = dados['quanto tempo de experiencia na area de dados voce tem?'].str.extract(r'(\d+)')

dados['tempo de experiencia'].value_counts()

## ver a coluna de numero de funcionarios

dados['numero de funcionarios'].value_counts()

## tirar remover o . depois do numero e transformar em numero inteiro

dados['numero de funcionarios'] = dados['quantos funcionarios tem a empresa onde voce trabalha?'].str.replace('.', '').astype(int)  

## repetir o comando para ver se o ponto saiu

dados['numero de funcionarios'].value_counts()

dados['numero de funcionarios'] = dados['numero de funcionarios'].str.extract(r'(\d+)')

dados['numero de funcionarios'].value_counts(dropna=False)

dados['tempo de experiencia'].value_counts(dropna=False)

## tirar os que não tem experiencia e transformar em numero inteiro

dados['tempo de experiencia'] = dados['tempo de experiencia'].fillna(0)












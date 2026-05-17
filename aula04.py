dados.groupby('coluna')['outra_coluna'].nunique() #mostra os valores únicos da coluna agrupados por outra coluna

dados.groupby('genero', dropna=False)['cor'].nunique() #mostra os valores únicos da coluna 'cor' agrupados por 'genero', mesmo que o valor seja nulo

dados['genero'].value_counts(dropna=False) #mostra a contagem de cada valor da coluna 'genero', mesmo que o valor seja nulo

dados[dados['idade']>30]['nivel'].value_counts() #mostra a contagem de cada valor da coluna 'nivel' para as linhas onde a coluna 'idade' tem valor maior que 30, mesmo que o valor seja nulo                    

dados[(dados['idade']>30) & (dados['genero']=='feminino')]['nivel'].value_counts()


pd.pivot_table(dados, index='genero', columns='nivel', values='idade', aggfunc='mean') #mostra a média da coluna 'idade' para cada combinação de 'genero' e 'nivel' em formato de tabela pivô






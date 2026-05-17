#valores faltantes / valores nulos 

dados.info() #verificar se existem valores faltantes

### trabalhando coluna de gênero

dados.groupby('genero')['idade'].mean() #media de idade por genero  

dados['genero'].fillna('desconecido', inplace=True) #preencher valores faltantes com 'desconecido'

dados['idade'].isnull()
##Para verificar quantos nulos são
dados['idade'].isnull().value_counts() #contar quantos valores nulos existem


dados.colums #verificar as colunas do dataframe


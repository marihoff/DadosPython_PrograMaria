#analise excel

dados[dados['coluna'] == 'valor'] #filtra a tabela mostrando apenas as linhas onde a coluna tem o valor especificado

#ex dados[dados['nome'] == 'João'] #mostra as linhas onde a coluna 'nome' tem o valor 'João'

dados.columns #mostra o nome das colunas da tabela

dados[dados['coluna'].str.contains('texto', na=False)] #filtra a tabela mostrando apenas as linhas onde a coluna contém o texto especificado

dados[dados['idade'] > 30] #filtra a tabela mostrando apenas as linhas onde a coluna 'idade' tem valor maior que 30

dados[dados['idade'] < 18] #filtra a tabela mostrando apenas as linhas onde a coluna 'idade' tem valor menor que 18

dados[dados['idade'].between(18, 30)] #filtra a tabela mostrando apenas as linhas onde a coluna 'idade' tem valor entre 18 e 30

dados[dados['idade']>30 & (dados['genero'] == 'feminino')] #filtra a tabela mostrando apenas as linhas onde a coluna tem valor maior que 30 e a coluna2 tem o valor especificado   


##exemplo

dados[dados['idade']<40 & (dados['cor'] == 'amarela')]


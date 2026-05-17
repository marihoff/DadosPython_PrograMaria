##Seguindo com Feature Engineering dos dados🖥️ 

##➡️Desta vez nós criamos uma coluna chamada “INSATISFACAO”, que a partir da coluna existente 'Qual o principal motivo da sua insatisfação com a empresa atual?' colocava o valor igual a 1 para toda frase que continha a palavra “Salário”. 

##➡️Depois disso, nós substituímos cada categoria da coluna de ‘NIVEL DE ENSINO’ por um valor. Na ordem crescente de escolaridade, por exemplo: 0 para “Não tenho graduação formal”, 1 para “Estudante de Graduação”, 2 para “Graduação-Bacharelado”, e assim por diante. 

dados['qual o principal motivo da sua insatisfação com a empresa atual?'].value_counts()

dados['insatisfacao'] = 0'


dados.loc[dados['qual o principal motivo da sua insatisfação com a empresa atual?'].notnull(), 'insatisfacao'] = dados.loc[dados['qual o principal motivo da sua insatisfação com a empresa atual?'].notnull(), 'qual o principal motivo da sua insatisfação com a empresa atual?'].apply(lambda x: 1 if 'Salário' in x else 0)


dados.loc[dados['qual o principal motivo da sua insatisfação com a empresa atual?'].notnull(), 'insatisfacao'] = dados.loc[dados['qual o principal motivo da sua insatisfação com a empresa atual?'].notnull(), 'qual o principal motivo da sua insatisfação com a empresa atual?'].apply(lambda x: 1 if 'Salário' in x else 0)

## confere novamente

dados['insatisfacao'] = 0'

dados['nivel de ensino'].value_counts()

dados['nivel de ensino'].apply(lambda x: 0 if x == 'Não tenho graduação formal' else 
                                (1 if x == 'Estudante de Graduação' else (2 if x == 'Graduação-Bacharelado' else 
                                (3 if x == 'Graduação-Licenciatura' else 
                                (4 if x == 'Pós-graduação-MBA' else 
                                (5 if x == 'Pós-graduação-Mestrado' else 
                                (6 if x == 'Pós-graduação-Doutorado' else None)))))))




## ➡️Para o SQL entender que estamos passando valores vindos de fora, precisamos concatenar interrogações (?) no lugar onde ficariam os nossos estados. 

# ➡️Entendida essa parte, a consulta SQL foi armazenada em uma string e, em seguida, executada no banco de dados usando o método read_sql() do pandas e, a cláusula WHERE com o operador IN foi utilizada para filtrar os registros. Algo mais ou menos assim:

# query = “““SELECT ……….WHERE municipios_brasileiros.Estado IN ({}) GROUP BY municipios_brasileiros.Estado”””.format(', '.join(['?' for _ in lista_estados]))

# estados_renda = pd.read_sql(query, con=conexao, params=lista_estados)

# ➡️Depois disso fizemos o merge com a nossa tabela original. Lembrando que o how do merge precisa respeitar as mesmas regras de left, right, inner que o JOIN em SQL. Nosso merge ficou assim:

# dados = dados.merge(estados_renda, left_on=’UF ONDE MORA’, right_on='Estado', how='left')
# ➡️Por fim, analisamos a correlação entre o salário e o índice de renda média do Estado utilizando a função corr(). Descobrimos que a correlação é positiva, quando maior o índice, maior o salário, porém baixa, mostrando que só esse índice não causa um impacto tão grande para o salário, precisamos analisar juntando outras variáveis de importância.
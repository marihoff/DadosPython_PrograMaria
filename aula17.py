# Vamos iniciar o primeiro passo?

# ➡️Para fazer a  conexão com o banco de dados SQLite, utilizamos a biblioteca sqlite3, então fizemos o import dela: import sqlite3

# ➡️A função connect() do sqlite3 foi utilizada para estabelecer a conexão, passando o caminho do arquivo do banco de dados como parâmetro.

# Documentação w3 schools 

## Conectando SQL com pandas

import sqlite3
sql conection = sqlite3.connect('C:/Users/Usuario/Desktop/SQL/SQL_para_analistas_de_dados/SQL_para_analistas_de_dados.db')
## dentro dos parentes o caminho da pasta, para conectar com o banco de dados

query = "SELECT * FROM municipios_brasileiros"
## aqui criamos a query, para selecionar tudo da tabela municipios_brasileiros

pd.read_sql_query(query, sql_conection)
## aqui usamos a função read_sql_query do pandas, para ler a query e a conexão com o banco de dados, e assim trazer os dados para o pandas



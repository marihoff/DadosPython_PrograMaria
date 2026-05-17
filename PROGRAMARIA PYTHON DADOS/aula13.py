#➡️O que é SQL?

#SQL (Structured Query Language) é a linguagem padrão para gerenciar e manipular dados em bancos de dados relacionais.

#Imagine o SQL como um tradutor mágico que permite conversar com o banco de dados, extraindo e organizando informações.

#➡️Tipos de comandos SQL:

#DDL (Data Definition Language): Linguagem de Definição - Cria, modifica e exclui tabelas no banco de dados.

#Ex: CREATE TABLE, ALTER TABLE, DROP TABLE

#DML (Data Manipulation Language): Linguagem de Manipulação - Insere, atualiza, consulta e remove dados das tabelas.

#Ex: SELECT, INSERT, UPDATE, DELETE

#DCL (Data Control Language): Linguagem de Controle - Controla permissões de acesso e segurança no banco de dados.

#Ex: GRANT, REVOKE

#📌Nas próximas aulas focaremos em DML, pois ele  é essencial para o dia a dia do analista de dados, pois permite extrair informações relevantes para análises. O comando SELECT é o principal para realizar consultas no banco de dados. Mas nesta aula vimos um pouco de DDL, para aprender o básico de criação de tabelas.

#Exemplo prático: Utilizamos o DBeaver, que é uma ferramenta visual de banco de dados, para criar tabelas de análise de municípios brasileiros:

#Criamos as tabelas Municipios_Brasileiros, Municipio_Status e Gerencia_Regiao com seus respectivos relacionamentos.

#Pararelembrar a estrutura básica para criar tabelas é:

#CREATE TABLE <NOME DA TABELA> (

    #<NOME DO CAMPO> <TIPO DE CAMPO> <RESTRICOES>,

            #…

#);



#▶️O nome da tabela é de livre escolha, mas evitamos usar caracteres especiais, o mesmo vale para o nome do campo e podemos criar tantos campos quantos forem necessários. 



#▶️Vimos na aula os campos do tipo: Integer, Varchar e Blob, mas existem vários outros tipos que podemos utilizar. 



#▶️As restrições vimos a NOT NULL, que diz que o campo não pode ser nulo, ou seja, sempre que for criado um registro novo é preciso passar algum valor para esse campo. 



#▶️Também vimos como definir a chave primária, utilizando as palavras PRIMARY KEY na frente da linha do campo definido, depois do not null. 



#▶️Também vimos como utilizar o comando AUTOINCREMENT, que define que o campo não precisa ser preenchido, mas receberá um valor incremental a cada novo registro. 



#▶️Por fim, aprendemos a definir a chave estrangeira na tabela. Adicionando antes de fechar o parenteses do CREATE TABLE o seguinte:

#CONSTRAINT <nome_da_restricao> FOREIGN KEY (<COLUNA NA TABELA ATUAL>) REFERENCES <TABELA ESTRANGEIRA> (<COLUNA NA TABELA ESTRANGEIRA>)

## o que é uma query
#Query é uma consulta feita ao banco de dados para extrair informações específicas. É como fazer uma pergunta ao banco de dados e receber uma resposta com os dados relevantes.
#Exemplo de query: SELECT nome, idade FROM clientes WHERE cidade = 'São Paulo';

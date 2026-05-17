## ➡️JOIN: Serve para juntar tabelas nos nossos dados, podemos usar ele várias vezes nas nossas consultas, juntando várias tabelas de uma vez. Porém temos que nos atentar sobre quais registros queremos trazer de cada tabela, entendendo bem os tipos de join existentes:

#INNER JOIN: Combina linhas com correspondências em ambas as tabelas.

#RIGHT JOIN: Retorna todos os registros da direita e os da esquerda com correspondência.

#LEFT JOIN: Retorna todos os registros da esquerda e os da direita com correspondência.

#FULL JOIN: Retorna todos os registros de ambas as tabelas, com ou sem correspondência.

#➡️GROUP BY: Serve para agrupa linhas por uma coluna específica, resumindo os dados. Perfeito para contagem, soma e média por grupos.

#➡️ORDER BY: Ordena os resultados da consulta em ordem crescente ou decrescente. Ideal para visualizar os maiores ou menores valores.

#Vamos lembrar duas queries que fizemos em aula com esses comandos:

#📌Exemplo Prático:

#Desvendando a População por Cidade:

#Selecionamos as colunas Cidade e populacao_residente.

#Juntamos as tabelas municipios_brasileiros e Municipios_Status usando INNER JOIN.

#A query ficou assim:

#SELECT municipios_brasileiros.Cidade, Municipios_Status.populacao_residente 

#FROM municipios_brasileiros  INNER JOIN Municipios_Status ON municipios_brasileiros.municipio_ID = Municipios_Status.municipio_ID 

#Vendo os Estados com mais cidades:

#Selecionamos as colunas Estado e cidade, porém usamos o agregador de COUNT na coluna cidade.

#Agrupamos por Estado usando GROUP BY.

#Ordenamos por COUNT(Cidade) em ordem decrescente com ORDER BY.

#A query ficou assim:

#SELECT Estado, COUNT(Cidade) 

#FROM municipios_brasileiros  

#GROUP BY Estado 

#ORDER BY 2 DESC ;

#E com isso descobrimos que o estado com mais cidades é Minas Gerais! 

#📌Dicas Extras:

#Explore os diferentes tipos de JOIN para escolher o ideal para sua necessidade.

#Use funções de agregação como COUNT(), SUM(), AVG() e MAX() para resumir dados agrupados.

#Combine ORDER BY com funções de agregação para visualizar os maiores ou menores valores em cada grupo.

#Pratique bastante para se tornar um mestre em JOIN, GROUP BY e ORDER BY!


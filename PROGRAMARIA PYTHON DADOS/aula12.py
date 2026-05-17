# ➡️O que são relacionamentos entre tabelas?

#A forma como as tabelas se conectam e "conversam" em um banco de dados.

#Imagine um armário digital onde as caixas (tabelas) estão interligadas, permitindo encontrar informações com mais facilidade e rapidez.

#➡️Tipos de relacionamentos:

#1 para 1 (1:1): Cada uma das duas entidades envolvidas referenciam obrigatoriamente apenas uma unidade da outra.

#Ex: Cada pessoa tem apenas uma carteira de identidade.

#1 para muitos (1:N) ou Muitos para 1 (N:1): Uma das entidades envolvidas pode referenciar várias unidades da outra, porém, do outro lado cada uma das várias unidades referenciadas só pode estar ligada uma unidade da outra entidade

#Ex: Um álbum pode ter várias músicas, mas cada música pertence a apenas um álbum (1:N) ou Várias músicas podem pertencer a um único álbum (N:1).

#Muitos para muitos (N:N): Neste tipo de relacionamento cada entidade, de ambos os lados, podem referenciar múltiplas unidades da outra

#Ex: Um cliente pode comprar vários álbuns, e um álbum pode ser comprado por vários clientes.

#➡️Diagrama Entidade e Relacionamento:

#É uma representação gráfica das relações entre as tabelas, facilita muito a compreender o que tem no banco e como essas entidades estão se relacionando.

#Representado por retângulos (tabelas) e linhas que as conectam (relacionamentos).

#Símbolos especiais indicam o tipo de relacionamento (1:1, 1:N, N:1, N:N).

#➡️Chave primária e chave estrangeira:

#As chaves indicam quais os campos que representam e conectam as tabelas.

#Chave primária: O "RG" da tabela, um identificador único para cada linha.

#Chave estrangeira: Campo que identifica qual o registro de uma tabela terceira está sendo associado naquela tabela. É o que permite que você conecte as informações de diferentes tabelas em um banco de dados relacional. Isso facilita a busca e organização dos dados.

#➡️Exemplo prático com o DBeaver:

#Exploramos um banco de dados real chamado "Chinook", usando o software DBeaver.

#Visualizamos as tabelas, seus dados e o diagrama ER para entender as relações.

#Analisamos a chave primária e a chave estrangeira em ação.


### Instalação do DBeaver
#1. Acesse o site oficial do DBeaver: https://dbeaver.io/download/
#2. Escolha a versão adequada para o seu sistema operacional (Windows, macOS ou Linux) e clique no link de download.
#3. Siga as instruções de instalação fornecidas pelo instalador do DBeaver  

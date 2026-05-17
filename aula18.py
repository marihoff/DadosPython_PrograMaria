# conceitos de string, como o format.

# O método format() é uma maneira de formatar strings em Python. Ele permite inserir valores em uma string de forma organizada e legível. Você pode usar chaves {} como marcadores de posição para os valores que deseja inserir, e depois chamar o método format() para preencher esses marcadores com os valores desejados.

# Exemplo de uso do format():
nome = "Alice"
idade = 30
mensagem = "Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem)
# Saída: Olá, meu nome é Alice e eu tenho 30 anos.
# Você também pode usar índices para especificar a ordem dos valores:
mensagem = "Olá, meu nome é {0} e eu tenho {1} anos. {0} é um nome bonito.".format(nome, idade)
print(mensagem)
# Saída: Olá, meu nome é Alice e eu tenho 30 anos. Alice é um nome bonito.


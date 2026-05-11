Create table Municipios_Status (
    status_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    populacao INTEGER NOT NULL,
    IDM_rank INTEGER NOT NULL,
    educacao INTEGER NOT NULL,
    renda_per_capita INTEGER NOT NULL,
    municipio_id INTEGER NOT NULL,
    CONSTRAINT fk_municipio FOREIGN KEY (municipio_id) REFERENCES Municipios_Brasileiros (municipio_id) ##Cria uma restrição de chave estrangeira, onde o campo municipio_id da tabela Municipios_Status referencia o campo municipio_id da tabela Municipios_Brasileiros

)
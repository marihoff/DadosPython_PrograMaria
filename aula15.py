ALTER TABLE Muncipios_brasileiros ADD COLUMN pais;

UPDATE Municipios_brasileiros SET pais = 'Brasil';

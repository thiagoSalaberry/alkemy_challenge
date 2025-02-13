-- CREATE TABLE
CREATE TABLE IF NOT EXISTS normalized(
    id SERIAL PRIMARY KEY,
    cod_localidad INT NOT NULL,
    id_provincia INT NOT NULL,
    id_departamento INT NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    provincia VARCHAR(255) NOT NULL,
    localidad VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    domicilio VARCHAR(255),
    codigo_postal VARCHAR(255),
    numero_de_telefono VARCHAR(255),
    mail VARCHAR(255),
    web VARCHAR(255),
    updated_at TIMESTAMP
);

-- DROP TABLE
DROP TABLE IF EXISTS normalized;
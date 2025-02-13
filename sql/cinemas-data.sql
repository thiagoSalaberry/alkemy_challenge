-- CREATE TABLE
CREATE TABLE IF NOT EXISTS cinemas(
    id SERIAL PRIMARY KEY,
    Provincia VARCHAR(255) NOT NULL,
    Cantidad_de_pantallas INT NOT NULL,
    Cantidad_de_butacas INT NOT NULL,
    Cantidad_de_espacios_INCAA INT NOT NULL,
    updated_at TIMESTAMP
);

-- DROP TABLE
DROP TABLE IF EXISTS cinemas;
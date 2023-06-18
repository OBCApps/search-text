-- (1) Creación de la tabla con dos atributos textuales, uno sin indexar y el otro indexado. 
CREATE EXTENSION pg_trgm;

CREATE TABLE index_postgresql (
    id text,
    text text
);

-- Create Index
CREATE INDEX id ON index_postgresql USING gin (text gin_trgm_ops);


-- (2) Inserción de datos aleatorios
INSERT INTO articles SELECT md5(random()::text), md5(random()::text) from ( SELECT * FROM generate_series(1,100000) AS id) AS x;

-- (3) Consultas
-- Consulta: Sin indexar
EXPLAIN ANALYZE SELECT count(*) FROM articles WHERE body ILIKE '%abc%';

-- Consulta: Indexado
EXPLAIN ANALYZE SELECT count(*) FROM articles WHERE body_indexed ILIKE '%abc%';

-- Eliminación la data para la nueva prueba de una nueva cantidad de datos
DELETE FROM articles;
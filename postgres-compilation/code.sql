-- (1) Creación de la tabla con dos atributos textuales, uno sin indexar y el otro indexado. 
CREATE EXTENSION pg_trgm;

CREATE TABLE prueba_index2 (
    id BIGINT,
    date VARCHAR(255),
    text TEXT,
    user_id BIGINT,
    user_name VARCHAR(255),
    location JSONB,
    retweeted BOOLEAN,
    RT_text TEXT,
    RT_user_id BIGINT,
    RT_user_name VARCHAR(255)
);


-- Create Index
CREATE INDEX id ON index_postgresql USING gin (text gin_trgm_ops);


-- (2) Inserción de datos aleatorios
INSERT INTO index_postgresql SELECT md5(random()::text), md5(random()::text) from ( SELECT * FROM generate_series(1,1663*59) AS id) AS x;

-- (3) Consultas
-- Consulta: Sin indexar
EXPLAIN ANALYZE SELECT count(*) FROM articles WHERE body ILIKE '%abc%';

-- Consulta: Indexado
EXPLAIN ANALYZE SELECT count(*) FROM articles WHERE body_indexed ILIKE '%abc%';

-- Eliminación la data para la nueva prueba de una nueva cantidad de datos
DELETE FROM articles;
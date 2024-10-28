-- Criando view para pesquisar os livros --

CREATE OR REPLACE VIEW livros_view AS
SELECT
    livro.id AS id,
    livro.titulo AS livro_titulo,
    autor.nome AS autor_nome,
    editora.nome AS editora_nome,
    genero.nome AS genero_nome,
    GROUP_CONCAT(tag.nome) AS tags_nomes
FROM
    livros AS livro
LEFT JOIN autores AS autor ON livro.autor_id = autor.id
LEFT JOIN editoras AS editora ON livro.editora_id = editora.id
LEFT JOIN generos AS genero ON livro.genero_id = genero.id
LEFT JOIN livros_tags AS livro_tag ON livro.id = livro_tag.livro_id
LEFT JOIN tags AS tag ON livro_tag.tag_id = tag.id
GROUP BY
    livro.id;
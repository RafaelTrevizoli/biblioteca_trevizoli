-- View criada para listar os usuários e emprestimos que cada usuário tem

CREATE VIEW emprestimos_usuario AS
SELECT u.username AS usuario,
       l.titulo AS livro,
       e.data_emprestimo AS data
FROM emprestimos e
JOIN auth_user u ON e.usuario_id = u.id
JOIN livros l ON e.livro_id = l.id;


-- Função criada para contar o número total de empréstimos associados a um livro específico.

CREATE FUNCTION contar_emprestimos_livro(livro_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;

    -- Conta quantos empréstimos estão associados a um livro específico
    SELECT COUNT(*) INTO total
    FROM emprestimos
    WHERE livro_id = livro_id;

    RETURN total;
END;


-- Procidure criada para encapsular a pesquisa top 3 e utilizar facilmente

CREATE PROCEDURE top_3_livros_mais_emprestados()
BEGIN
    SELECT l.id, l.titulo, COUNT(e.id) AS total_emprestimos
    FROM livros l
    LEFT JOIN emprestimos e ON l.id = e.livro_id
    GROUP BY l.id
    ORDER BY total_emprestimos DESC
    LIMIT 3;
END;







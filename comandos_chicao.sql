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

-- Trigger criada para listar os logs dos usuários que realizaram emprestimos.

CREATE TRIGGER log_emprestimo
AFTER INSERT ON emprestimos
FOR EACH ROW
BEGIN
    INSERT INTO logs (usuario_id, livro_id, acao, data)
    VALUES (NEW.usuario_id, NEW.livro_id, 'Empréstimo realizado', NOW());
END;





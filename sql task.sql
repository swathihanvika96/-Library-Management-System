CREATE DATABASE library_db;

USE library_db;

CREATE TABLE books1 (
    id INTEGER PRIMARY KEY ,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    available_copies INTEGER NOT NULL
);

INSERT INTO books1 (title, author, category, available_copies) VALUES
('The Alchemist', 'Paulo Coelho', 'Adventure', 9),
('The Lord of the Rings', 'JRR Tolkien', 'High Fantacy', 4);

CREATE TABLE members1 (
    id INTEGER PRIMARY KEY ,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(10) NOT NULL
);

INSERT INTO members1 (name, email, phone)
VALUES
('Yash', 'yash@gmail.com', '2345678910'),
('Swathi', 'swathi@gmail.com', '7896543210');

CREATE TABLE borrow1 (
    id INTEGER NOT NULL ,
    member_id INT,
    book_id INT,
    returned TINYINT,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO borrow1 (id,member_id, book_id, returned)
VALUES
(1,1,1,0),
(2,2,2,0);

SELECT
b.title,
COUNT(br.book_id) total_borrowed
FROM books1 b
JOIN borrow1 br
ON b.id = br.book_id
GROUP BY b.title
ORDER BY total_borrowed DESC;

SELECT
m.name,
COUNT(br.member_id) total_books
FROM members1 m
JOIN borrow1 br
ON m.id = br.member_id
GROUP BY m.name
HAVING COUNT(br.member_id) > 3;

SELECT
category,
COUNT(*) total_books
FROM books
GROUP BY category;

SELECT *
FROM borrow
WHERE returned = 0;

SELECT
SUM(available_copies)
AS total_available_books
FROM books;
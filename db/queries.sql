-- получить все курсы
SELECT * FROM courses;

-- получить первые 3 курса
SELECT * FROM courses LIMIT 3;

-- получить курсы отсортировав по названию

-- получить курсы отсортировав в обратном порядке

-- получить курс по id
SELECT * FROM courses WHERE id = 1;

-- получить курс по названию
SELECT * FROM courses WHERE name = 'Python';

-- получить курс по длительность
SELECT * FROM courses WHERE duration BETWEEN 4 AND 6;

-- Добавить таблицк с преподавателями
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course_id INTEGER,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Внести данные в таблицу преподавателей
INSERT INTO teachers (name, course_id) VALUES 
    ('Нурлан', 1),
    ('Алексей', 1),
    ('Бекболот', 1),
    ('Атай', 2),
    ('Игорь', 2);

-- получить всех преподавателей одного курса
SELECT * FROM teachers WHERE course_id = 1;

-- получить преподавателей с названием курса
SELECT t.name, c.name FROM teachers AS t
JOIN courses AS c ON t.course_id = c.id

-- получить преподавателей с названием курса, фильтр по id курса
SELECT t.name, c.name FROM courses AS t
JOIN teacher AS c ON t.course_id = c.id
WHERE c.id = 1;





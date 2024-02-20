import sqlite3
from pathlib import Path
from pprint import pprint


class DB:
    def __init__(self):
        '''Инициализация соединения с БД'''
        # .db, .db3, .sqlite, .sqlite3
        self.connection = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')
        self.cursor = self.connection.cursor()

    def create_tables(self):
        '''Создание таблиц'''
        self.cursor.execute('DROP TABLE IF EXISTS courses')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                duration INTEGER,
                image TEXT
            )
        ''')
        self.cursor.execute('DROP TABLE IF EXISTS teachers')
        self.cursor.execute('''
            CREATE TABLE teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                course_id INTEGER,
                FOREIGN KEY (course_id) REFERENCES courses(id)
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS free_lesson_registration (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                email TEXT,
                course TEXT,
                telegram_id INTEGER
            )
        ''')
        self.connection.commit()


    def populate_tables(self):
        '''Заполнение таблиц'''
        self.cursor.execute('''
            INSERT INTO courses (name, description, duration, image) VALUES 
            ("Backend", "Бекенд - это ...", 5, "images/backend.jpg"),
            ("Frontend", "Фронтенд - это ...", 5, "images/frontend.jpg"),
            ("Android", "Android - это ...", 6, "images/android.jpg"),
            ("IOs", "IOs - это ...", 6, "images/ios.jpg"),
            ("Тестирование", "Тестирование - это ...", 4, "images/testing.jpg")
        ''')
        self.cursor.execute('''
            INSERT INTO teachers (name, course_id) VALUES 
                ('Нурлан', 1),
                ('Алексей', 1),
                ('Бекболот', 1),
                ('Атай', 2),
                ('Игорь', 2)
        ''')
        self.connection.commit()

    def get_courses(self):
        '''Получение курсов'''
        # пропустить пераы 2 курса и показать следующие 2
        self.cursor.execute('SELECT id, name FROM courses LIMIT 2 OFFSET 2')
        # self.cursor.execute('SELECT id, name FROM courses')
        return self.cursor.fetchall()
        # return self.cursor.fetchone()
    
    def get_course_by_id(self, course_id):
        # course_id = "1; DROP DATABASE test;"
        '''Получение курса по ID'''
        self.cursor.execute(
            'SELECT * FROM courses WHERE id = :id', 
            {'id': course_id}
        )
        return self.cursor.fetchone()

    def get_course_by_name(self, course_name):
        '''Получение курса по названию'''
        self.cursor.execute(
            'SELECT * FROM courses WHERE name = :name', 
            {'name': course_name}
        )
        return self.cursor.fetchone()

    def get_teachers_by_course_id(self):
        '''Получение преподавателей'''
        self.cursor.execute(
            'SELECT * FROM teachers WHERE course_id = 1'
        )
        return self.cursor.fetchall()
    
    def get_all_teacher_with_courses(self):
        '''Получение преподавателей с названиями курсов'''
        self.cursor.execute('''
            SELECT t.name, c.name FROM teachers AS t
            JOIN courses AS c ON t.course_id = c.id
        ''')
        return self.cursor.fetchall()

    def get_teachers_by_course_name(self, course_name):
        '''Получение преподавателей с названиями курсов'''
        self.cursor.execute('''
            SELECT t.name, c.name FROM teachers AS t
            JOIN courses AS c ON t.course_id = c.id
            WHERE c.name = :name
        ''',
        {'name': course_name}
        )
        return self.cursor.fetchall()

    def save_free_lesson_data(self, data: dict, tg_id: int):
        name = 'igor'
        '''Сохранение данных о записи на бесплатный урок'''
        print(data)
        self.cursor.execute('''
            INSERT INTO free_lesson_registration (name, age, email, course, telegram_id) 
            VALUES (:name, :age, :email, :course, :telegram_id);
            ''',
            {
                'name': data['name'],
                'age': int(data['age']),
                'email': data['email'],
                'course': data['course'],
                'telegram_id': tg_id
            }
        )
        self.connection.commit()

if __name__ == "__main__":
    db = DB()
    db.create_tables()
    db.populate_tables()
    # pprint(db.get_courses())
    # pprint(db.get_course_by_id(3))
    # pprint(db.get_course_by_name('Frontend'))
    # pprint(db.get_teachers_by_course_id())
    # pprint(db.get_all_teacher_with_courses())
    pprint(db.get_teachers_by_course_name("Backend"))

# СУБД - Система Управления Базами Данных
# MySQL, PostgreSQL, SQLite, Oracle, MsSQL
# PRIMARY KEY - первичный ключ

# Реляционные БД - realtional - связи

# Курс
# id, name, description, duration, image
# 1, "Backend", "Бекенд - это ...", 5, "images/backend.jpg"
# 2, "Frontend", "Фронтенд - это ...", 5, "images/frontend.jpg"
# 3, "Android", "Android - это ...", 6, "images/android.jpg"

# Преподаватель
# id, name, course_id
# 1, "Нурлан", 1
# 2, "Алексей", 1
# 3, "Игорь", 2
# 4, "Бекболот", 1
# 5, "Атай", 2

# FOREIGN KEY - внешние ключи
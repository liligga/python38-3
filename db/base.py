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
        self.connection.commit()

    def get_courses(self):
        '''Получение курсов'''
        self.cursor.execute('SELECT * FROM courses')
        return self.cursor.fetchall()
        # return self.cursor.fetchone()
    

if __name__ == "__main__":
    db = DB()
    db.create_tables()
    db.populate_tables()
    pprint(db.get_courses())

# СУБД - Система Управления Базами Данных
# MySQL, PostgreSQL, SQLite, Oracle, MsSQL
# PRIMARY KEY - первичный ключ
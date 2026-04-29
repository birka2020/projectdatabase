import sqlite3
import csv

connection = sqlite3.connect("Readme.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("DROP TABLE IF EXISTS borrowings")
cursor.execute("DROP TABLE IF EXISTS buyers")
cursor.execute("DROP TABLE IF EXISTS cars")
cursor.execute("DROP TABLE IF EXISTS model")

cursor.execute("""
    CREATE TABLE buyers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")

cursor.execute(""" 
    CREATE TABLE cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        colors TEXT NOT NULL,
        country TEXT NOT NULL,
        year TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE model (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        name TEXT NOT NULL,
        money INTEGER NOT NULL,
        power INTEGER NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE borrowings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        buyers_id INTEGER NOT NULL,
        model_id INTEGER NOT NULL,
        cars_id INTEGER NOT NULL,
        date_borrowed TEXT NOT NULL,
        date_returned TEXT,
        FOREIGN KEY (buyers_id) REFERENCES buyers(id),
        FOREIGN KEY (model_id) REFERENCES model(id) 
    )
""")


buyers_array = [
    ("Артём", 25), ("Маргарита", 22), ("Сергей", 31), ("Елена", 29), ("Дмитрий", 19),
    ("Анна", 24), ("Владимир", 35), ("Ольга", 28), ("Александр", 20), ("Екатерина", 23),
    ("Иван", 33), ("Наталья", 26), ("Павел", 21), ("Софья", 20), ("Андрей", 30),
    ("Ксения", 27), ("Николай", 18), ("Виктория", 25), ("Максим", 22), ("Анастасия", 29),
    ("Роман", 34), ("Мария", 21), ("Денис", 20), ("Полина", 19), ("Евгений", 32),
    ("Алина", 28), ("Арсений", 26), ("Вероника", 24), ("Григорий", 30), ("Юлия", 23)
]

cursor.executemany("""
    INSERT INTO buyers (name, age)
    VALUES (?, ?)
""", buyers_array)

cars_array = [
    ("BMW_M5", "Красный", "Германия", "2026"),
    ("BMW_M5", "Синий", "Германия", "2025"),
    ("BMW_M5", "Черный", "Германия", "2024"),
    ("BMW_M5", "Белый", "Германия", "2023"),
    ("BMW_M5", "Серебристый", "Германия", "2022"),
    ("BMW_M5", "Зеленый", "Германия", "2021"),
    ("BMW_M5", "Желтый", "Германия", "2020"),
    ("BMW_M5", "Оранжевый", "Германия", "2019"),
    ("BMW_M5", "Фиолетовый", "Германия", "2018"),
    ("BMW_M5", "Розовый", "Германия", "2017"),
    ("BMW_M5", "Коричневый", "Германия", "2016"),
    ("BMW_M5", "Серый", "Германия", "2015"),
    ("BMW_M5", "Бежевый", "Германия", "2014"),
    ("BMW_M5", "Золотистый", "Германия", "2013"),
    ("BMW_M5", "Бронзовый", "Германия", "2012"),
    ("BMW_M5", "Темно-синий", "Германия", "2011"),
    ("BMW_M5", "Темно-зеленый", "Германия", "2010"),
    ("BMW_M5", "Вишневый", "Германия", "2009"),
    ("BMW_M5", "Мятный", "Германия", "2008"),
    ("BMW_M5", "Бирюзовый", "Германия", "2007"),
    ("BMW_M5", "Лазурный", "Германия", "2006"),
    ("BMW_M5", "Графитовый", "Германия", "2005"),
    ("BMW_M5", "Перламутровый", "Германия", "2004"),
    ("BMW_M5", "Хаки", "Германия", "2003"),
    ("BMW_M5", "Морской волны", "Германия", "2002"),
    ("BMW_M5", "Лимонный", "Германия", "2001"),
    ("BMW_M5", "Алый", "Германия", "2000"),
    ("BMW_M5", "Индиго", "Германия", "1999"),
    ("BMW_M5", "Маджента", "Германия", "1998"),
    ("BMW_M5", "Циан", "Германия", "1997")
]


cursor.executemany ("""
    INSERT INTO cars (name, colors, country, year)
    VALUES (?, ?, ?, ?)
""", cars_array)

model_array = [
    ("BMW M5 VI", 3000000, 625),
    ("BMW M5 V", 2800000, 560),
    ("BMW M5 IV", 2500000, 507),
    ("BMW M5 III", 2200000, 400),
    ("BMW M5 II", 1800000, 340),
    ("BMW M5 I", 1500000, 286),
    ("BMW M3 G80", 2800000, 510),
    ("BMW M3 F80", 2400000, 450),
    ("BMW M3 E92", 2000000, 420),
    ("BMW M3 E46", 1600000, 343),
    ("Mercedes E63 AMG W213", 3200000, 612),
    ("Mercedes E63 AMG W212", 2800000, 585),
    ("Mercedes C63 AMG W205", 2700000, 510),
    ("Mercedes C63 AMG W204", 2300000, 487),
    ("Mercedes AMG GT 63", 4500000, 639),
    ("Mercedes S63 AMG", 5000000, 612),
    ("Mercedes CLS63 AMG", 3100000, 585),
    ("Mercedes GLE63 AMG", 3800000, 603),
    ("Audi RS6 C8", 3400000, 600),
    ("Audi RS6 C7", 2900000, 560),
    ("Audi RS6 C6", 2500000, 580),
    ("Audi RS7 C8", 3500000, 600),
    ("Audi RS7 C7", 3000000, 560),
    ("Audi RS3 8Y", 2200000, 400),
    ("Audi RS3 8V", 1900000, 400),
    ("Audi RS5 B9", 2600000, 450),
    ("Audi RS5 B8", 2300000, 450),
    ("Audi RS4 B9", 2500000, 450),
    ("Audi RS4 B8", 2200000, 450),
    ("Audi RS Q8", 4200000, 600)
]

cursor.executemany ("""
INSERT INTO model (name, money, power)
VALUES (?, ?, ?)
""", model_array)

connection.commit()
connection.close()
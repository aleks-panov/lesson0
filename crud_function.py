import sqlite3


def initiate_db():
    connection = sqlite3.connect('telegram_bot.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL);
    ''')

    a = 1
    for i in range(4):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                    (f'Продукт {a}', f'Описание {a}', f'{a * 100}'))
        a += 1

    connection.commit()
    connection.close()


def get_all_products():

    connection = sqlite3.connect("telegram_bot.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    connection.commit()
    connection.close()
    return products

ini = initiate_db()
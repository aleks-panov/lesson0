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
    connection.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL);
        ''')
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


def add_user(username, email, age):
    connection = sqlite3.connect("telegram_bot.db")
    cursor = connection.cursor()

    cursor.execute(f'''
    SELECT COUNT(*) FROM Users
    ''')
    all_user = cursor.fetchone()[0] + 1

    cursor.execute(f'''
    INSERT INTO Users VALUES("{all_user}", "{username}", "{email}", "{age}", "1000")
    ''')

    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect("telegram_bot.db")
    cursor = connection.cursor()

    user0 = True
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone() is None:
        user0 = False
    return user0


    connection.commit()
    connection.close()

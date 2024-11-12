import sqlite3

connection = sqlite3.connect('not_telegram.dp')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

#for i in range(1, 11):
    #cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@.com", f"{10*i}", f"{1000}"))
#for i in range(1, 11,2):
    #cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))
#for i in range(1, 11,3):
    #cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))

#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
cursor.execute("SELECT SUM(balance) FROM Users")
cursor.execute("SELECT AVG(balance) FROM Users")
users = cursor.fetchall()
for user in users:
    print(user)
connection.commit()
connection.close()

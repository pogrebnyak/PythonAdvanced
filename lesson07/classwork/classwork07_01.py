import sqlite3

conn = sqlite3.connect('shop')
cursor = conn.cursor()
result = cursor.execute('SELECT * FROM products')
print(result)
print(result.fetchall())
print(result.fetchone())
for i in result:
    print(i)

conn.close()
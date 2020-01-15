import sqlite3


class DataConnect:

    def __init__(self, db_name, permission='r'):
        self.db_name = db_name
        self.permission = permission

    def __enter__(self):
        self.connect = sqlite3.connect(self.db_name)
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.permission is 'w':
            self.connect.commit()
        self.connect.close()
        if exc_val:
            raise

if __name__ == '__main__':
    db = 'test.db'

    with DataConnect(db, 'w') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products VALUES (null,'lamp',20,2)")

    with DataConnect(db) as connection:
        cursor = connection.cursor()
        result = cursor.execute('SELECT * FROM products')
        print(result.fetchall())

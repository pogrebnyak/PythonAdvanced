import sqlite3 as sqlite


class Dbconnect:

    def __init__(self, db_name, permission='r'):
        self.db_name = db_name
        self.permission = permission

    def __enter__(self):
        self.connect = sqlite.connect(self.db_name)
        return self.connect.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.permission is 'w':
            self.connect.commit()
        elif self.permission is 'r':
            pass
        else:
            raise KeyError
        self.connect.close()
        if exc_val:
            raise

if __name__ == '__main__':
    db = 'test.db'

    with Dbconnect(db, 'w') as conn:
        conn.execute("INSERT INTO products VALUES (null,'lamp',20,2)")

    with Dbconnect(db) as conn:
        result = conn.execute('SELECT * FROM products')
        print(result.fetchall())
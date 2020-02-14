import sqlite3



class Dbconn:

    def __init__(self, db_name, permission='r'):
        self.db_name = db_name
        self.permission = permission

    def __enter__(self):
        self.connect = sqlite3.connect(self.db_name)
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
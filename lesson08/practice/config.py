import workdb

db = 'db_shop.db'

def good(name):
    with workdb.Dbconnect(db) as conn:
        good_list = []
        conn.execute("SELECT goods.name,goods.cost,goods.amount,categories.title FROM goods INNER JOIN \
            categories ON categories.id = goods.categories WHERE goods.name=?", (name,))
        good_list = conn.fetchall()[0]
        return good_list


def clist():
    with workdb.Dbconnect(db) as conn:
        conn.execute("SELECT title FROM categories ORDER BY title")
        categories_list = []
        for row in conn.fetchall():
            categories_list.append(row[0])
        return categories_list

def categories_input(value):
    if value:
        with workdb.Dbconnect(db,'w') as conn:
            conn.execute("SELECT title FROM categories WHERE title=?", (value,))
            if conn.fetchall():
                return 'Такая категория уже существует'
            else:
                conn.execute("INSERT INTO categories VALUES(null, ?)", (value,))
    else:
        return 'Не ввели данные'

def good_input(value_name, value_cost, value_amount, value_categories):
    if all((value_name, value_cost, value_amount, value_categories)):
        with workdb.Dbconnect(db,'w') as conn:
            conn.execute("SELECT name FROM goods WHERE name=?", (value_name,))
            if conn.fetchall():
                conn.execute("UPDATE goods SET cost=?, amount=?, categories = (SELECT id FROM categories WHERE title=?) \
                	WHERE name=?", (value_cost, value_amount, value_categories, value_name))
            else: 
                conn.execute("INSERT INTO goods VALUES(null, ?, ?, ?, (SELECT id FROM categories WHERE title=?))", (value_name, value_cost, value_amount, value_categories))


def glist(id_categ):
    with workdb.Dbconnect(db) as conn:
        goods_list = []
        conn.execute("SELECT goods.id, goods.name, goods.cost, goods.amount \
            FROM goods, categories \
            WHERE categories.id = goods.categories and categories.title = (?) and goods.amount <> 0 ORDER BY goods.name", (id_categ,))
        for row in conn.fetchall():
            goods_list.append(row)
        return goods_list

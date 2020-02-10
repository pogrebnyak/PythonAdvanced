import sqlite3

dbase = 'db_shop.db'

def base_open():
    global cursor, conn
    conn = sqlite3.connect(dbase)
    cursor = conn.cursor()

def good(name):
    base_open()
    good_list = []
    cursor.execute("SELECT goods.name,goods.cost,goods.amount,categories.title FROM goods, categories WHERE categories.id = goods.categories and goods.name = ?", (name,))
    good_list = cursor.fetchall()[0]
    conn.close()
    return good_list


def clist():
    base_open()
    cursor.execute("SELECT title FROM categories ORDER BY title")
    categories_list = []
    for row in cursor.fetchall():
        categories_list.append(row[0])
    conn.close()
    return categories_list

def categories_input(value):
    if value:
        base_open()
        cursor.execute("SELECT title FROM categories WHERE title = ?", (value,))
        if cursor.fetchall():
            conn.close()
            return 'Такая категория уже существует'
        else:
            cursor.execute("INSERT INTO categories VALUES(null, ?)", (value,))
            conn.commit()
            conn.close()
    else:
        return 'Не ввели данные'

def good_input(value_name, value_cost, value_amount, value_categories):
    if all((value_name, value_cost, value_amount, value_categories)):
        base_open()
        cursor.execute("SELECT name FROM goods WHERE name = ?", (value_name,))
        if cursor.fetchall():
            cursor.execute("UPDATE goods SET cost = ?, amount = ?, categories = (SELECT id FROM categories WHERE title = ?) \
            	WHERE name = ?", (value_cost, value_amount, value_categories, value_name))
        else: 
            cursor.execute("INSERT INTO goods VALUES(null, ?, ?, ?, (SELECT id FROM categories WHERE title = ?))", (value_name, value_cost, value_amount, value_categories))
        conn.commit()
        conn.close()


def glist(id_categ):
    base_open()

    goods_list = []
    cursor.execute("SELECT goods.id, goods.name, goods.cost, goods.amount \
        FROM goods, categories \
        WHERE categories.id = goods.categories and categories.title = (?) and goods.amount <> 0 ORDER BY goods.name", (id_categ,))
    for row in cursor.fetchall():
        goods_list.append(row)
    conn.close()
    return goods_list

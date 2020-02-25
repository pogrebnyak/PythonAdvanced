import hashlib
import datetime
import shelve

FILEUSER = "user_dict.db"
FILEBASE = 'base_dict.db'


class Registration:

    def __init__(self, login, password, is_admin=False):
        self._login = login
        self._password = password
        self._is_admin = is_admin

    def add_user(self):
        registration_date = datetime.datetime.today().strftime('%Y%m%d %H:%M:%S')
        hash_pass = hashlib.md5(self._password.encode())
        with shelve.open(FILEUSER) as db:
            db[self._login] = (hash_pass.hexdigest(), self._is_admin, registration_date)


    def check_pass(self,in_password):
        if len(self._password) < 8:
            print('Длина пароля должна быть больше 8 символов')
            return False

        if not any(char.isdigit() for char in self._password):
            print('Пароль должен содержать одну цифру')
            return False

        if not any(char.isupper() for char in self._password):
            print('Пароль должен содержать одну заглвную букву')
            return False

        if not any(char.islower() for char in self._password):
            print('Пароль должен содержать одну маленькую букву')
            return False

        if in_password != self._password:
            print('Не совпадает подтверждение пароля')
            return False

        return True


    def __str__(self):
        with shelve.open(FILEUSER) as db:
            return str(db)



class Authorization(Registration):

    def __init__(self, login, password, is_admin=False):
        super().__init__(login, password, is_admin=False)
        self._login = login
        self._password = password
        self._is_admin = is_admin

    def check_pass(in_login, in_pass):
        hash_pass = hashlib.md5(in_pass.encode())
        with shelve.open(FILEUSER) as db:
            return True if db[in_login][0] == hash_pass.hexdigest() else False

class User:

    def check_is_admin(in_login):
        with shelve.open(FILEUSER) as db:
           return True if db[in_login][1] else False

    def check_user(check_login):
        with shelve.open(FILEUSER) as db:
            return True if db.get(check_login) else False

    def print_user():
        with shelve.open(FILEUSER) as db:
            for i,j in db.items():
                print(f'{i:10}{j[0]:50}{j[2]:20}')

class Article:

    def __init__(self, base_user, base_post):
        self._base_user = base_user
        self._base_post = base_post

    def add_post(self):
        post_date = datetime.datetime.today().strftime('%Y%m%d %H:%M:%S')
        with shelve.open(FILEBASE) as db:
            if not db.get(self._base_user):
                db[self._base_user] = []
            temp = db[self._base_user]
            temp.append((post_date, self._base_post))
            db[self._base_user] = temp

    def print_post_user(in_user):
        with shelve.open(FILEBASE) as db:
            posts = db[in_user]
            for i in posts:
                print(f'{i[0]:20}{i[1]:30}')

    def print_post_admin():
        with shelve.open(FILEBASE) as db:
            for i,j in db.items():
                for s in j:
                    print(f'{s[0]:20}{i:15}{s[1]:30}')

    def __str__(self):
        with shelve.open(FILEBASE) as db:
            return str(db)


#user = Registration('admin','12345',True)
# user2 = Registration('user','12345')
#Registration.add_user(user)
# Registration.add_user(user2)
#
# article = Article('admin','Мама мыла раму')
# Article.add_post(article)
# article = Article('admin','Мыло ело маму')
# Article.add_post(article)
# article = Article('user','Мыло ело маму2')
# Article.add_post(article)
# article = Article('user','Мыло ело маму2')
# Article.add_post(article)

while True:
    print('1.Авторизация')
    print('2.Регистрация')
    print('3.Выход')
    s = input('Выбор: ')
    if s == '1':
        in_login = input('Введите логин: ')
        in_password = input('Введите пароль: ')
        if User.check_user(in_login) and Authorization.check_pass(in_login, in_password):
            print(f'Вы авторизировались как {in_login}')
            if User.check_is_admin(in_login):
                while True:
                    print('1. Вывести всех пользователей')
                    print('2. Вывести все посты')
                    print('3. Выход')
                    str_admin = input('Выбор: ')
                    if str_admin == '1':
                        User.print_user()
                    if str_admin == '2':
                        Article.print_post_admin()
                    if str_admin == '3':
                        break

            else:
                while True:
                    print('1. Добавить пост')
                    print('2. Вывести мои посты')
                    print('3. Выход')
                    str_user = input('Выбор: ')
                    if str_user == '1':
                        in_post = input('Введите сообщение: ')
                        article = Article(in_login, in_post)
                        Article.add_post(article)
                    if str_user == '2':
                        Article.print_post_user(in_login)
                    if str_user == '3':
                        break

        else:
            print('Ошибка авторизации')
    if s == '2':
        in_login = input('Введите логин: ')
        if User.check_user(in_login):
            print('Такой пользователь уже существует')
            continue
        in_password = input('Введите пароль: ')
        in_password2 = input('Введите подтверждение пароля пароль: ')
        user = Registration(in_login, in_password)
        if Registration.check_pass(user, in_password2):
            Registration.add_user(user)
            print('Вы удачно зарегестрировались')
    if s == '3':
        break


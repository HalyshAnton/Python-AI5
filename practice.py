# sql ін'єкція
# SELECT *
# FROM TABLE
# WHERE PASSWORD = '{user_password}'
#
#
# user_password = 123' OR '2' = '2
#
# SELECT *
# FROM TABLE
# WHERE PASSWORD = '123' OR '2' = '2'


# import redis
#
# server = redis.Redis(host='localhost', port=6379,
#                      db=0, decode_responses=True
#                      )
#
# server.set('user:name', 'Антон')
#
# name = server.get('user:name')
# print(name)

#Завдання 1
# Реалізуйте консольний додаток «Кошик» для
# вебмагазину. Додаток має надавати функціональність
# для роботи з кошиком. Можливості додатку:
# ■ Вхід у кошик за логіном та паролем;
# ■ Додати товар у кошик;
# ■ Видаляти товар з кошика;
# ■ Змінити товар у кошику;
# ■ Повне очищення кошика;
# ■ Пошук даних у кошику;
# ■ Перегляд вмісту кошика.
# Зберігайте дані у базі даних NoSQL.
# Можете використовувати Redis в якості платформи

import redis


class RedisCart:
    def __init__(self):
        self.server = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )

        # користувач з яким зараз працюємо
        self.current_user = None

    def register_user(self, username, password):
        # перевірка чи зареєстрований юзер
        if self.server.hexists('users', username):
            print('Користувач уже зареєстрований')
            return

        # реєстрація нового юзера
        self.server.hset(
            'users',  # назва хеша(словника з логінами\паролями)
            username,
            password
        )

    # ■ Вхід у кошик за логіном та паролем;
    def login(self, username, password):
        # неправильний username
        if not self.server.hexists('users', username):
            print("Невірне ім'я користувача")
            return

        real_password = self.server.hget(
            "users", username
        )

        if real_password == password:
            print("Доступ надано")
            self.current_user = username
        else:
            print("Невірний пароль")

    # ■ Додати товар у кошик;
    def add_item(self, item_id, item_count):
        # carts:username = {
        #   "item_id": count
        # }

        # якщо користувач не залогінився
        if self.current_user is None:
            print('Потрібно залогінитись')
            return

        # словник для конкретного користувача
        key = f"carts:{self.current_user}"

        if self.server.hexists(key, item_id):
            old_count = self.server.hget(key, item_id)
            new_count = old_count + item_count
            self.server.hset(key, item_id, new_count)
        else:
            self.server.hset(key, item_id, item_count)

    # ■ Видаляти товар з кошика;


    # ■ Змінити товар у кошику;


    # ■ Повне очищення кошика;


    # ■ Пошук даних у кошику;


    # ■ Перегляд вмісту кошика.

# створити об'єкт класу
cart = RedisCart()

while True:
    print('0 -- вихід')
    print('1 -- реєстрація нового користувача')
    print('2 -- логін')

    command = input('Введіть номер команди: ')

    if command == '0':
        break

    elif command == '1':
        username = input("Ведіть ім'я користувача: ")
        password = input("Ведіть пароль: ")
        cart.register_user(username, password)

    elif command == '2':
        username = input("Ведіть ім'я користувача: ")
        password = input("Ведіть пароль: ")
        cart.login(username, password)

    else:
        print("Невірна команда")


# hset users = {
#   "login": password
# }
#
# users = {
#     'Anton': '123456',
#     "Jhon": "asd123",
#     ....
# }
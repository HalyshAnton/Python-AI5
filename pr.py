from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

# Створіть однотабличну базу даних People (ім’я, прізвище, місто, країна, дата народження) з однойменною
# таблицею. Напишіть програму, яка дозволяє користувачеві ввести запит і отримати результати роботи запиту.
# Підтримуйте лише SELECT як запит. Якщо ви спробуєте
# виконати інші запити, потрібно буде генерувати помилку.
with open('config.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data ['password']

    db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/itstep"
engine = create_engine(db_url)

Base = declarative_base()

class People(Base):
    __tablename__ = 'peole'
    id = Column(Integer, Sequence('user_id_seg'), primary_key=True)
    name = Column(String(20))
    surname = Column(String(20))
    city = Column(String(20))
    country = Column(String(20))
    date_dr = Column(Date)


    def __repr__(self):
        return (f"id = {self.id}, name = {self.name}, surname = {self.surname}, city = {self.city}, "
                f"country = {self.country}, date_dr = {self.date_dr} ")

Base.metadata.create_all(engine)

from datetime import date

people_list = [
    People(name="Олександр", surname="Шевченко", city="Київ", country="Україна", date_dr=date(1990, 5, 15)),
    People(name="Ірина", surname="Коваленко", city="Харків", country="Україна", date_dr=date(1985, 3, 10)),
    People(name="Андрій", surname="Мельник", city="Львів", country="Україна", date_dr=date(1993, 7, 8)),
    People(name="Світлана", surname="Іванова", city="Одеса", country="Україна", date_dr=date(1992, 1, 21)),
    People(name="Віктор", surname="Петренко", city="Дніпро", country="Україна", date_dr=date(1988, 9, 30)),
    People(name="Марія", surname="Гриценко", city="Запоріжжя", country="Україна", date_dr=date(1995, 11, 5)),
    People(name="Євген", surname="Сидоренко", city="Полтава", country="Україна", date_dr=date(1989, 6, 12)),
    People(name="Анна", surname="Ткаченко", city="Чернігів", country="Україна", date_dr=date(1991, 2, 28)),
    People(name="Дмитро", surname="Кузьменко", city="Вінниця", country="Україна", date_dr=date(1994, 4, 17)),
    People(name="Олена", surname="Литвин", city="Івано-Франківськ", country="Україна", date_dr=date(1987, 8, 23))
]

Session = sessionmaker(engine)
session = Session()
# session.add_all(people_list)
# session.commit()

def command1():
    user_inp = input('введіть запит: ')

    query_sql = text(user_inp)

    # виконуємо запит
    result = session.execute(query_sql)
    rows = result.fetchall()

    for row in rows:
        print(row)


def command2():
    user_city = input('введіть назву міста')

    query = f"""
    Select *
    from peole
    where city = '{user_city}'
    """

    query_sql = text(query)
    result = session.execute(query_sql)
    rows = result.fetchall()

    for row in rows:
        print(row)

while True:
    print('1 - виконати запит')
    command = input('введіть номер команди: ')

    if command == '1':
        command1()

    elif command == '2':
        command2()

    else:
        break
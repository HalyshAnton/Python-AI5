from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

# завантажуємо логін та пароль
with open('config.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']

# підключаємось до бд itstep
db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/itstep"
engine = create_engine(db_url)

# створення батьківського класу
Base = declarative_base()

# ствлорення класу для таблиці User
class User(Base):
    __tablename__ = 'users'

    # стовпчики
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(30))
    city = Column(String(50))

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, city={self.city})"

# добавляємо всі таблиці в базу даних
Base.metadata.create_all(engine)

# створюємо сесію
Session = sessionmaker(bind=engine)
session = Session()

# # створюємо юзерів
# user1 = User(name='Jhon', city='LA')
# user2 = User(name='Sophia', city='London')
#
# # добавити юзерів у базу даних
# users = [user1, user2]
# session.add_all(users)
#
# # внести всі зміни в базу даних
# session.commit()

# показати усі рядки таблиці(через session)
rows = session.query(User).all()

for row in rows:
    print(row)

# показати усі рядки таблиці(через SQL)
# запит як str
query = """
SELECT *
FROM USERS
"""

query_sql = text(query)

# виконуємо запит
result = session.execute(query_sql)
rows = result.fetchall()

for row in rows:
    print(type(row))
    print(row.name)
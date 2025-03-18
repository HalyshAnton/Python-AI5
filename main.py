#data = 'Hello, world'


# with open('data.txt', 'w') as file:
#     file.write(data)
#     #print(data, file=file)

# with open('data.txt', 'r') as file:
#     data = file.read()
#
#
# print(type(data))
# print(data)

import json


# data = {'number': 24}
# data = [1, 2, 'hello']
# bytes = json.dumps(data)  # переводить дані у серію байтів(серіалізація)
# print(type(bytes))
# print(bytes)
#
# new_data = json.loads(bytes)  # переводить байти назад в об'єкт(десеріалізація)
# print(type(new_data))
# print(new_data)

# файли

# зберегти дані у файл json
# data = {"number": 25, "text": "Hello"}
#
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)
#
# # завантажити дані з файли
# with open('data.json', 'r') as file:
#     new_data = json.load(file)
#
# print(new_data)


# Користувач водить текстові повідомлення, зберегти
# їх у список і у файл. За потреба заіантажити історію спілкування

# завантажити історію
# with open("history.json", 'r') as file:
#     history = json.load(file)
#
# # головний цикл
# while True:
#     text = input("Введіть повідомлення: ")
#
#     if text == "":  # якщо порожньо, то кінець програми
#         # перед завершенням зберегти історію
#         with open("history.json", 'w') as file:
#             json.dump(history, file)
#         break
#
#     elif text == "show": # показати історію
#         print("History")
#         for message in history:
#             print(f"\t {message}")
#
#     else:
#         # просто повідомлення добавити в історію
#         history.append(text)


# збереждення об'єктів класів

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        print(f"{self.name} святкує день народження")
        self.age += 1

    def state_dict(self): # словник з атрибутами
        data = {
            'name': self.name,
            'age': self.age
        }

        return data

    def load(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        self.name = data['name']
        self.age = data['age']


person = Person('', '')
person.load('data.json')
person.celebrate_birthday()

# person = Person("John", 30)
# person.celebrate_birthday()
# person.celebrate_birthday()
#
# with open('data.json', 'w') as file:
#     json.dump(person.state_dict(), file) # збереження словника з атрибутами
#
#
# # завантаження даних
# with open('data.json', 'r') as file:
#     data = json.load(file)
#
# new_person = Person(data['name'], data['age'])




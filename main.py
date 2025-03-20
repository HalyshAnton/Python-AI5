import json


data = [1, 2, 3, 4]

# JSON
# збереження у файл
# filename = 'data.json'
# with open(filename, 'w') as file:
#     json.dump(data, file)
#
#
# # завантаження з файла
# with open(filename, 'r') as file:
#     new_data = json.load(file)
#
#
# print(new_data)

#Pickle
import pickle


data = [1, 2, 3, 4]

# encoded = pickle.dumps(data)
# print(encoded)

# збереження у файл
# w -- відкрити для запису
# b -- відкрити як двійковий файл(файл з байтами)

# with open('data.pkl', 'wb') as file:
#    pickle.dump(data, file)
#     #file.write('data')

#
# # завантаження з файла
# with open('data.pkl', 'rb') as file:
#     new_data = pickle.load(file)
#
# print(new_data)

# dump -- робота з файлом
# dumps -- робота без файла


# класи

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.name}, {self.age} років")

    def __repr__(self):
        return f"{self.name}, {self.age} років"


# person1 = Person('Mary', 27)
# person2 = Person("John", 34)
# person3 = Person('Jack', 42)
#
# persons = [person1, person2, person3]
#
# with open('data.pkl', 'wb') as file:
#     pickle.dump(persons, file)
#
#
# with open("data.pkl", 'rb') as file:
#     data = pickle.load(file)
#
#
# print(data)
# jack = data[2]
#
#jack.print_info()



# gzip
import gzip


data = [1, 2, 3, 4]

with gzip.open('data.zip', 'wb') as file:
    # кодуємо дані у байти
    encoded_data = pickle.dumps(data)

    # зберігаємо закодовані дані у файл
    file.write(encoded_data)


with gzip.open('data.zip', 'rb') as file:
    # читаємо закодовані дані
    encoded_data = file.read()

    # розшифровуємо дані
    new_data = pickle.loads(encoded_data)


print(encoded_data)
print(new_data)

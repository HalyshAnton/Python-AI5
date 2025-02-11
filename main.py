# class Dog

# опис класу, шаблон
class Dog:
    # конструктор для створення об'єктів класу
    def __init__(self, name, age, weight):
        # self -- обєкт класу(конкретний пес)
        if age < 0:
            raise ValueError("вік пса неможе бути від'ємні")

        self.name = name
        self.age = age
        self.weight = weight

    # можливість гавкати
    # метод
    def make_sound(self):
        print("Гав")


    def print_info(self):
        # вивід інформації про песика
        print(self.name, self.age, self.weight)

    def rename(self, new_name):
        # зміна імені песика
        self.name = new_name


# конкретні песики
# dog1 = Dog()  # об'єкт клас Dog
#
# print(dog1.name)
# print(dog1.age)
# print(dog1.weight)
#
# dog2 = Dog()
#
# dog2.name = 'Lev' # зміна
#
# print(dog2.name)
# print(dog2.age)
# print(dog2.weight)
#
# # використання метода
# dog1.make_sound()


# dog1 = Dog(name='Lev', age=3, weight=7)
# print(dog1.name)
#
# dog2 = Dog(name='Carl', age=5, weight=10)
# print(dog2.name)
#
#
# dog1.print_info()  # self = dog1
# dog2.print_info()  # self = dog2

dog = Dog('Carl', 5, 10)
dog.print_info()

dog.rename("Петро")  # self = dog,  new_name = "Петро"
dog.print_info()

# line.replace(',', ' ')
#
# def replace(self, old, new):

self.items.append("Стіл")
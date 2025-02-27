# # наслідування
#
# # переведення числа в діапазон [0, 100]
#
# value = -10
#
# # варіант через if
# # if value > 100:
# #     value = 100
# # elif value < 0:
# #     value = 0
#
# # через min max
#
# value = -10
# new_value = min(value, 100)
# new_value = max(new_value, 0)
#
# new_value = max(0, min(100, value))  # clip
#
# print(new_value)

# використання методів батьківського класу
from abc import ABC, abstractmethod

class Animal(ABC):  # абстрактний клас(не можна створити об'єкт)
    @abstractmethod
    def __init__(self, name, age):
        self._check_name(name)
        self._check_age(age)
        self.name = name
        self.age = age

    def _check_name(self, name):
        # перевірка чи тип даних str
        if not isinstance(name, str):
            raise ValueError(f"Ім'я має бути рядком, отримано тип {type(name)}")

        # лише літери та символи ' ' '-'
        for sym in name:
            if not(sym.isalpha() or sym in ' -'):
                raise ValueError("Ім'я має складатися лише з літер та ' -'")

    def _check_age(self, age):
        # перевірка чи тип даних int float
        if not isinstance(age, (int, float)):
            raise ValueError(f"Вік має бути числом, отримано тип {type(age)}")

        if age <= 0 or age >= 20:
            raise ValueError(f"Вік має бути в діапазоні [0, 20]")


    def info(self):
        print(f"Ім'я: {self.name}, {self.age} років")


class Cat(Animal): # name, age, is_vaccinated
    def __init__(self, name, age, is_vaccinated=True):
        super().__init__(name, age)
        self.is_vaccinated = is_vaccinated

    def catch_mouse(self):
        print("Ловить мишу")

    def info(self):  # додатково писало що це кіт
        print("Кіт")
        # super() # super -- батьківський клас
        super().info() # info з класу Animal

        if self.is_vaccinated:
            print("Вакцинований")
        else:
            print("Потрібно вакцинувати")


# cat1 = Cat('Tom', 5)
# cat1.info()
# #cat1.catch_mouse()
# print()
#
# cat = Animal('Roger', 10)
# cat.info()

# приховані атрибути\методи

class Cat(Animal): # name, age, is_vaccinated
    def __init__(self, name, age, is_vaccinated=True):
        super().__init__(name, age)
        self._is_vaccinated = is_vaccinated  # прихований атрибут

    def catch_mouse(self):
        print("Ловить мишу")

    def info(self):  # додатково писало що це кіт
        print("Кіт")
        # super() # super -- батьківський клас
        super().info() # info з класу Animal

        if self._is_vaccinated:
            print("Вакцинований")
        else:
            print("Потрібно вакцинувати")

    def vaccinate(self):
        self._is_vaccinated = True

    def unvaccinate(self):
        self._is_vaccinated = False


class Kitten(Cat):
    pass


cat1 = Cat('Tom', 2.5)

cat1.info()

cat1.unvaccinate()

cat1.info()

# print(cat1._Cat__is_vaccinated)

kitten = Kitten("Murchyck", 1)
kitten.info()

# Завдання 1
# Створіть наступні класи:
#  Rectangle – атрибути width, height
#  Circle – атрибути radius
#  Triangle – атрибути a, b, c

# Методи:
#  get_perimeter()
#  display_info()

# Напишіть функцію create_figure() яка запитує у користувача
# тип фігури та потрібні атрибути і повертає об’єкт.
# Створіть декілька фігур, добавте їх у список та для кожної
# викличте відповідні методи.
from math import pi
#import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def display_info(self):
        perim = self.get_perimeter()
        print(f"Прямокутник")
        print(f"ширина: {self.width} "
              f"висота: {self.height} "
              f"периметр: {perim} ")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        # return 2 * math.pi * self.radius
        return 2 * pi * self.radius

    def display_info(self):
        perim = self.get_perimeter()
        print(f"Коло")
        print(f"радіус: {self.radius} "
              f"периметр: {perim} ")









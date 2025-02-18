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











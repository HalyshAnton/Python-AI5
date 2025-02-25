# наслідування

# class Parent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"клас Parent")
#         print(f'{self.name}, {self.age} років')
#
#
# class Child(Parent):
#     def play(self):   # новий метод
#         print('клас Child')
#         print(f'{self.name} грається')
#
#     def show_info(self):  # перевизначений метод
#         print(f"клас Child")
#         print(f'{self.name}, {self.age} років')
#
#
# class Daughter(Parent):
#     def __init__(self, name, age, dream):
#         self.name = name
#         self.age = age
#         self.dream = dream
#
#
# # mother = Parent('Marry', 36)
# # mother.show_info()
# #
# # print()
# #
# # child = Child('Rony', 8)
# # child.show_info()
# # child.play()
#
# # daughter = Daughter("Linda", 10, 'became a doctor')
# # daughter.show_info()
#
# # код з класом Parent
# mother = Parent('Marry', 36)
# mother.show_info()

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



# класи для Транспортні засоби

class Vehicle:
    def __init__(self, owner,  # власник
                 max_fuel_level,  # максимальний рівень пального
                 milliage  # км / 1 літр пального
                 ):
        self.owner = owner
        self.max_fuel_level = max_fuel_level
        self.fuel_level = max_fuel_level # бак повний
        self.milliage = milliage

    def move(self, speed, distance):
        need_fuel = distance / self.milliage

        if self.fuel_level < need_fuel: # не хватає пального
            print('не хватає пального')
        else:
            self.fuel_level -= need_fuel
            time = distance / speed

            print(f"Проїхали {distance}км за {time}год")


    def add_fuel(self, fuel):
        self.fuel_level += fuel

class Car(Vehicle):
    pass


class Bicycle(Vehicle):
    def __init__(self, owner, max_fuel_level, milliage):
        self.owner = owner
        self.max_fuel_level = max_fuel_level
        self.fuel_level = max_fuel_level  # бак повний
        self.milliage = milliage

        self.used_motor = False # мотор виключений


    def move(self, speed, distance):  # теж рухається але не трабе пального
        if not self.used_motor:
            time = distance / speed
            print("Без пального")
            print(f"Проїхали {distance}км за {time}год")
            return

        # мотор вклюсений(код з Vehicle.move)

        need_fuel = distance / self.milliage

        if self.fuel_level < need_fuel:  # не хватає пального
            print('не хватає пального')
        else:
            self.fuel_level -= need_fuel
            time = distance / speed

            print("З пальним")
            print(f"Проїхали {distance}км за {time}год")

    def turn_on(self):
        self.used_motor = True

    def turn_off(self):
        self.used_motor = False


class Plane(Vehicle):
    pass



bike = Bicycle('John', 100, 50)
bike.move(20, # швидкість
         15  # кілометри
         )

bike.turn_on()

bike.move(40,
          100)


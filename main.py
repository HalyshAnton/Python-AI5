# class Dog

# опис класу, шаблон
class Dog:
    # атрибути
    name = 'Monty'
    age = 2
    weight = 5

    # можливість гавкати
    # метод
    def make_sound(self):
        print("Гав")


# конкретні песики
dog1 = Dog()

print(dog1.name)
print(dog1.age)
print(dog1.weight)

dog2 = Dog()

dog2.name = 'Lev' # зміна

print(dog2.name)
print(dog2.age)
print(dog2.weight)

# використання метода
dog1.make_sound()



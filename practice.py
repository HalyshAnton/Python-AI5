# TASK 1
class FastFoodQueue:
    pass


# Тестування
fast_food = FastFoodQueue()
fast_food.add("Олег")
fast_food.add("Анна")
fast_food.add("Марія")
fast_food.add("Сергій")

fast_food.serve(0)
fast_food.serve(1)

time.sleep(2)
fast_food.make_order()
time.sleep(3)
fast_food.make_order()

fast_food.show_statistics()


# TASK 2
class Passenger:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class Zone:
    pass


class Airport:
    pass


# Тестування
airport = Airport()
passengers = [
    Passenger("Олег", 3),
    Passenger("Анна", 1),
    Passenger("Марія", 4),
    Passenger("Сергій", 2)
]

for p in passengers:
    airport.add(p)

airport.serve_registration()
airport.serve_registration()
airport.serve_security_control()
airport.serve_boarding()

airport.show_statistics()


# TASK3
class Passenger:
    def __init__(self, name, priority, baggage=None):
        if baggage is None:
            baggage = []
        self.name = name
        self.priority = priority
        self.baggage = baggage


# Використання
passenger1 = Passenger("Alice", 2, ["ticket", "phone"])
passenger2 = Passenger("Bob", 1, ["ticket", "knife"])
passenger3 = Passenger("Charlie", 3, ["ticket"])
passenger4 = Passenger("David", 4, ["ticket", "laptop"])
passenger5 = Passenger("Eva", 2, ["bottle", "knife"])
passenger6 = Passenger("Frank", 3, ["book"])
passenger7 = Passenger("Grace", 1, ["ticket", "explosives"])
passenger8 = Passenger("Hannah", 5, ["phone", "tablet"])
passenger9 = Passenger("Ivy", 2, ["ticket", "earphones"])
passenger10 = Passenger("Jack", 1, ["ticket", "gun"])

# Створюємо аеропорт
airport = Airport()

# Додаємо пасажирів до реєстрації
airport.add(passenger1)
airport.add(passenger2)
airport.add(passenger3)
airport.add(passenger4)
airport.add(passenger5)
airport.add(passenger6)
airport.add(passenger7)
airport.add(passenger8)
airport.add(passenger9)
airport.add(passenger10)

# Проходимо етапи для кожного пасажира
for _ in range(10):
    airport.serve_registration()
    airport.serve_security_control()
    airport.serve_boarding()

# Показуємо статистику
airport.show_statistics()
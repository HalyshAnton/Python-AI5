import time
from collections import deque

import heapq


class Passenger:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority  # Чим вище число, тим вищий пріоритет

    def __lt__(self, other):
        return self.priority > other.priority  # Інверсія для правильної роботи пріоритетної черги


class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = []  # Пріоритетна черга

    def add(self, passenger):
        heapq.heappush(self.passengers, passenger)
        print(f"{passenger.name} доданий до зони {self.name} (Пріоритет: {passenger.priority})")

    def serve_passenger(self):
        if self.passengers:
            return heapq.heappop(self.passengers)
        return None


class Airport:
    def __init__(self):
        self.zones = {
            "Реєстрація": Zone("Реєстрація"),
            "Контроль безпеки": Zone("Контроль безпеки"),
            "Посадка": Zone("Посадка")
        }
        self.passengers = []  # Пасажири, які пройшли всі етапи

    def add(self, passenger):
        self.zones["Реєстрація"].add(passenger)

    def serve_registration(self):
        passenger = self.zones["Реєстрація"].serve_passenger()
        if passenger:
            self.zones["Контроль безпеки"].add(passenger)
            print(f"{passenger.name} перейшов до зони Контроль безпеки")

    def serve_security_control(self):
        passenger = self.zones["Контроль безпеки"].serve_passenger()
        if passenger:
            self.zones["Посадка"].add(passenger)
            print(f"{passenger.name} перейшов до зони Посадка")

    def serve_boarding(self):
        passenger = self.zones["Посадка"].serve_passenger()
        if passenger:
            self.passengers.append(passenger)
            print(f"{passenger.name} успішно пройшов всі етапи та готовий до польоту!")

    def show_statistics(self):
        print("Статистика аеропорту:")
        for name, zone in self.zones.items():
            print(f"{name}: {len(zone.passengers)} пасажирів у черзі")
        print(f"Успішно пройшли всі зони: {len(self.passengers)} пасажирів")


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

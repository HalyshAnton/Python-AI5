class Department:
    # YOUR CODE
    pass


class Hospital:
    # YOUR CODE
    pass


# Створення відділень
cardiology = Department("Кардіологія")
surgery = Department("Хірургія")
therapy = Department("Терапія")
neurology = Department("Неврологія")

# Ініціалізація лікарні з переданими відділеннями
hospital = Hospital([cardiology, surgery, therapy, neurology])

hospital.add("Іван", 2, "Кардіологія")
hospital.add("Анна", 4, "Хірургія")
hospital.add("Марія", 3, "Терапія")
hospital.add("Олег", 1, "Неврологія")
hospital.add("Сергій", 4, "Кардіологія")

cardiology.treat_next()  # лікує Сергія
surgery.treat_next()  # лікує Анну

hospital.show_statistics()
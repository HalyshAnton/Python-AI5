# Завдання 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису


class Project:
    def __init__(self, name, budget, tasks):
        self.name = name
        self.budget = budget
        self.tasks = tasks

        self.expenses = 0
        self.is_finished = False
        self.spent_time = 0  # місяці

    def display_info(self):
        print(f"Проєкт {self.name}")
        print(f'Час виконання {self.spent_time} місяців')
        print(f'Витрачено {self.expenses}/{self.budget}$')
        print(f'Залишилось {self.budget - self.expenses}$')

        if self.is_finished: # якщо проект завершений
            print("Стан проекту: завершений")
        else:
            print("Стан проекту: незавершений")

            print('Задачі що залишились:')
            for task in self.tasks:
                print(f'   - {task}')

    def add_task(self, task):
        self.tasks.append(task)


project = Project(name='Ігрушка',
                  budget=10_000,
                  tasks=['Знайти інвесторів',
                         'Придумати загальну ідею'])

project.display_info()




















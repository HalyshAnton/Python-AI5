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
        print()
        print()

    def add_task(self, task):
        self.tasks.append(task)

    def divide_task(self, task, subtasks):
        if task not in self.tasks:
            print(f'Немає такої задачі {task}')
            return

        # задача є в списку задач self.tasks
        self.tasks.remove(task)

        self.tasks += subtasks

    def do_task(self, task, duration, price):
        # чи є така задача
        if task not in self.tasks:
            print(f'Немає такої задачі {task}')
            return

        # чи вистачає бюджету
        free_money = self.budget - self.expenses
        if price > free_money:
            print("Недостатньо коштів")
            return

        # виконуємо задачу
        self.expenses += price
        self.tasks.remove(task)
        self.spent_time += duration

        # чи завершений проект
        if len(self.tasks) == 0:
            self.is_finished = True

    def update_budget(self, amount):
        self.budget += amount



project = Project(name='Ігрушка',
                  budget=10_000,
                  tasks=['Знайти інвесторів',
                         'Придумати загальну ідею'])

project.display_info()

project.add_task('Вибрати ПЗ для гри')

project.display_info()

project.divide_task('Організувати бенкет',
                    ['витратити бюджет']
                    )

project.divide_task('Придумати загальну ідею',
                    ['Обрати між 2D та 3D',
                     'Придумати сюжет',
                     'Прописати персонажів']
                    )

project.display_info()

project.do_task('Придумати сюжет', 6, 1000)
project.do_task('Обрати між 2D та 3D', 3, 200)
project.do_task('Прописати персонажів', 15, 6000)

project.update_budget(2500)

project.do_task('Знайти інвесторів', 10, 3000)
project.do_task('Вибрати ПЗ для гри', 5, 1800)

project.display_info()

















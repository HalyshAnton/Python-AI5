# Як було раніше

# def func1():
#     print('Hello from func1')
#
#
# def func2():
#     print('Hello from func2')
#
#
# func1()  # виконується код з func1
# func2()  # чекає поки завершиться попередній код, тоді починає роботу
# func2()
# func1()

# створення потоків
import threading
import time

# def func1():
#     for i in range(1000_000):
#         if i % 100_000 == 0:  # виводити раз на 100_000
#             print('Hello from func1\n', end='')
#
#
# def func2():
#     for i in range(1000_000):
#         if i % 100_000 == 0:
#             print('Hello from func2\n', end='')
#
#
# # потік для виконання функції func1
# thread1 = threading.Thread(target=func1)
#
# # потік для виконання функції func2
# thread2 = threading.Thread(target=func2)
#
#
# # запускаємо потоки
# thread1.start()
# thread2.start()
#
# print('hello before join')  # може запуститись коли потоки ще працюють
#
# # момент коли потоки закінчили роботу
# thread1.join()
# thread2.join()
#
# print('END')  # запуститься коли потоки закінчили роботу

# функції з параметрами

# def greeting(name, age):
#     for i in range(1000_000):
#         if i % 100_000 == 0:
#             print(f'Привіт {name}, {age} років\n', end='')
#
#
# def summa(nums):
#     for i in range(1000_000):
#         if i % 100_000 == 0:
#             print(f'Сума чисел {nums} = {sum(nums)}\n', end='')
#
#
# nums = [1, 2, 3, 4]
#
# # thread1 = threading.Thread(target=greeting, args=('John',), kwargs={"age": 35})
# thread1 = threading.Thread(target=greeting, args=('John', 35))
# thread2 = threading.Thread(target=summa, args=(nums,))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()


# спільна ділянка пам'яті

nums = [1, 2, 3, 4]
lock = threading.Lock()


def append():
    # дістати nums зі спільної області пам'яті
    global nums, lock

    for num in range(1000):
        # працює зі спільною ділянкою пам'яті
        # інші потоки зупиняються поки цей не завершить роботу
        lock.acquire()

        nums.append(num)

        lock.release()  # роботу завершено, інші потоки можуть працювати

def remove():
    global nums, lock

    for _ in range(1000):
        lock.acquire()
        nums.pop(0)
        lock.release()


thread1 = threading.Thread(target=append)
thread2 = threading.Thread(target=remove)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(nums)


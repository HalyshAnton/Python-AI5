# rate1 = Banking.exchange_rates[from_currency]
# rate2 = Banking.exchange_rates[to_currency]
# return amount * rate1 / rate2

import time
import datetime

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:
    """
    Клас двозв'язного списку.
    """

    def __init__(self):
        """
        Ініціалізація порожнього списку.
        """
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def push_end(self, data):
        """
        Додає елемент у кінець списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data):
        """
        Додає елемент на початок списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_end(self):
        """
        Видаляє останній елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """
        if not self.tail:
            return None

        data = self.tail.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return data

    def pop_start(self):
        """
        Видаляє перший елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """

        if not self.head:
            return None

        data = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def is_empty(self):
        """
        Чи є порожній
        :return: True якщо порожній
        """
        return self.head is None

    def peek(self):
        """
        Повертає останній елемент, не видаляючи його
        :return: останній елемент
        """
        return self.tail.data


class Message:
    def __init__(self, text):
        self.text = text
        #self.time = time.time()  # кількість секунд  1970 року
        self.time = datetime.datetime.now().time()  # нинішній чис

    def __str__(self):
        return f"[{self.time}] {self.text}"


# клас для обробки повідомлень
class Messenger:
    def __init__(self):
        self.messages = DoubleLinkedList()

    def add_message(self, text):
        # добавити в кінець черги
        message = Message(text)

        self.messages.push_end(message)

    def read_next_message(self):
        if self.messages.is_empty():
            print('Повідомлень немає')
            return

        # дістає найдавніше повідемлення
        message = self.messages.pop_start()

        print(f"Читаємо повідомлення: {message}")


# m = Messenger()
#
# m.add_message('Hello')
# time.sleep(1) # чекає 1 секунду
# m.add_message("What`s up")
# time.sleep(2) # чекає 2 секунди
# m.add_message("I`m fine")
#
#
# m.read_next_message()
# time.sleep(1)
# m.read_next_message()
# time.sleep(1)
# m.read_next_message()


# list1 = [1, 2, 3, 4]
# list2 = ['a', 'hello']
# list3 = [[1, 2, 3], Node(), ]


# пріоритетна черга
from queue import PriorityQueue


# створення пріоритетної черги
queue = PriorityQueue()

# добавити елемент
symtom = 'болить голова'
priority = 3

data = (priority, symtom)

queue.put(data)

# одним рядком
# queue.put((3, 'болить голова'))
# queue.put((priority, symtom))

queue.put((3, 'болить горло'))
queue.put((1, 'струс мозку'))
queue.put((2, 'просто спитати'))

# дістати елемент

data = queue.get()  # отримуєте пару пріоритет, дані
print(data)

data = queue.get()  # отримуєте пару пріоритет, дані
print(data)

data = queue.get()  # отримуєте пару пріоритет, дані
print(data)

priority, symtom = queue.get()  # отримуєте пару пріоритет, дані
print(symtom)

print(queue.empty())

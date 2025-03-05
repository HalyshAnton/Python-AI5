# OOP

# def move(self, destination, distance):
#     leaving_passengers = []
#     left_passengers = []
#
#     for p in self.passengers:
#         if p.destination == destination:
#             leaving_passengers.append(p)
#         else:
#             left_passengers.append(p)
#
#     self.passengers = left_passengers
#
# a + b  # __add__
# a > b  # __gt__
# num in nums  # __contains__

# структури даних

# нотація O

# n = 10
# a = 2 + 3  # швидкість не залежить від n. O(1)
#
#
# for i in range(n):  # кількість операцій залежить від n. O(n)
#     print(i)
#
#
# for i in range(n):     # O(n^2)
#     for j in range(n):
#         print(i+j)
#
# for i in range(n):     # O(n^2)
#     for j in range(n):
#         print(i+j)

# import math
#
# N = 10**12
# print(math.log(N))


# зв'язний список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # вузол який йде наступним

    def __str__(self):
        return f"{self.data} -> {self.next}"


# node1 = Node(4)
# node2 = Node('abc')
# node3 = Node(5)
#
# node1.next = node2
# node2.next = node3
#
# print(node1)


# class LinkedList:
#     def __init__(self):
#         self.head = None  # перший вузол, поки що список порожній
#
#     def append(self, data):
#         node = Node(data)
#
#         # якщо список пустий
#         if self.head is None:
#             self.head = node
#             return  # кінець
#
#         # знайти останній вузол
#         end = self.head
#
#         while end.next is not None:  # поки можна рухатись далі
#             end = end.next
#
#         end.next = node
#
#     def __str__(self):
#         return str(self.head)
#
#
# class LinkedList1:
#     def __init__(self):
#         self.head = None  # перший вузол, поки що список порожній
#         self.tail = None  # останній вузол, поки що список порожній
#
#     def append(self, data):
#         node = Node(data)
#
#         # якщо список пустий
#         if self.head is None:
#             self.head = node
#             self.tail = node
#             return  # кінець
#
#         # добавити в кінець вузол
#         self.tail.next = node
#         self.tail = node
#
#     def __str__(self):
#         return str(self.head)
#
#
# list1 = LinkedList1()
#
# list1.append(2)
# list1.append(5)
# list1.append(1)
# list1.append(4)
#
# print(list1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def push_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_end(self):
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


list1 = DoubleLinkedList()

list1.push_end(2)
list1.push_start(5)
list1.push_end(1)
list1.push_start(4)

print(list1)

print(list1.pop_end())
print(list1)
print(list1.pop_start())
print(list1.pop_start())
list1.push_end(1)
print(list1)




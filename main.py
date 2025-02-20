# nums = [1, 4, 5, 2]
# a = 1
# b = 2
#
# a == b
# a.__eq__(b)
#
# a + b
# a.__add__(b)
#
# a > b
# a.__gt__(b)
#
# 3 in nums
# nums.__contains__(3)
#
# nums[2]
# nums.__getitem__(2)
#
# nums.append
#
# min max sort

#  Створіть клас Cart з атрибутами
#  items – список товарів
#  total – загальна ціна товарів
# методи:
#  __str__(self) – повертає рядок зі списком товарів
#  __len__(self) – повертає кількість товарів
#  __add__(self, other) – об’єднує 2 кошики та повертає
# новий кошик
# Створіть два кошики. Виведіть кількість товарів в кожному
# з них. Виведіть самі кошики. Об’єднайте їх та виведіть
# кількість товарів в новому кошику та товари в ньом


class Cart:
    def __init__(self, items, total):
        self.items = items
        self.total = total

    def __str__(self):
        text = ''
        for item in self.items:
            text += str(item) + ', '

        text = text[:-2]
        return f"{text}. Загальна ціна {self.total}$"

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_items = self.items + other.items
        new_total = self.total + other.total
        new_cart = Cart(new_items, new_total)
        return new_cart

    def __gt__(self, other):  # self > other
        return len(self) > len(other)

    def __lt__(self, other): # self < other
        return not (self > other)

    def __eq__(self, other): # self == other
        return (set(self.items), self.total) == (set(other.items), other.total)
        #return  self.items == other.items and self.total == other.total

    def __contains__(self, item): # item in self
        return item in self.items

    def __getitem__(self, idx): # self[idx]
        return self.items[idx]

    def __iter__(self):  # for item in self
        #return iter(self.items)
        for item in self.items:
            yield item

    def add_item(self, item, price):
        self.items.append(item)
        self.total += price

# генератор квадратів чисел

# def square_range(finish):
#     for num in range(finish):
#         yield num**2
#
#
# for num in square_range(5):  # yield
#     print(num)
#
# num = square_range(5)  # return
# a = 1
# b = 2
#
# c = a + b
#

cart1 = Cart(['TV', 'laptop'], 170)
cart2 = Cart(['phone'], 65)

cart3 = Cart(['laptop', 'TV'], 170)

print(cart1 == cart3)

#
# print(cart1)
# text = str(cart2)
# print(text)
#
# print(f"Кошик1: кількість товарів: {len(cart1)}")
#
# cart3 = cart1 + cart2
# print(cart3)
# print(f"Кошик3: кількість товарів: {len(cart3)}")
#
# if cart3 > cart2:
#     print('Кошик 3 більший')
#
#
# max_cart = max(cart1, cart2)
# print(max_cart)
#
#
# carts = [cart3, cart2, cart1]
# print()
# print()
# print('кошики до сортування')
# for cart in carts:
#     print(cart)
#
# carts.sort()
# print()
# print()
# print('кошики після сортування')
# for cart in carts:
#     print(cart)
#
# print()
# print()
#
# print("Apple" in cart1)
# print("TV" in cart1)
# print("Apple" not in cart1)
#
# print()
# print()
#
# second_item = cart3[1]
# print(second_item)
#
# print()
# print()
#
# for item in cart3:  # iter(cart3)
#     print(item)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def add(self, data):
#         node = Node(data)
#
#         if self.root is None:
#             self.root = node
#             return
#
#         self._recursive_add(self.root, node)
#
#     def _recursive_add(self, tree_node, added_node):
#         if added_node.data < tree_node.data:
#             # рухаємося наліво
#
#             # перевіряємо чи пусто зліва
#             if tree_node.left is None:
#                 tree_node.left = added_node
#                 return  # рекурсія(цикл) закінчується
#
#             # якщо не пусто
#             self._recursive_add(tree_node.left, added_node)
#         else:
#             # рухаємося направо
#
#             # перевіряємо чи пусто справа
#             if tree_node.right is None:
#                 tree_node.right = added_node
#                 return  # рекурсія(цикл) закінчується
#
#             # якщо не пусто
#             self._recursive_add(tree_node.right, added_node)
#
#     def display(self):
#         nodes_to_display = [self.root]
#
#         while len(nodes_to_display) != 0:
#             # відображаємо все що є в nodes_to_display
#             for node in nodes_to_display:
#                 print(node.data, end=' ')
#             print()
#
#             # отримуємо наступні вузли
#             new_nodes = []
#             for node in nodes_to_display:
#                 if node.left is not None:
#                     new_nodes.append(node.left)
#
#                 if node.right is not None:
#                     new_nodes.append(node.right)
#
#             # замінюємо nodes_to_display на нові вузли
#             nodes_to_display = new_nodes
#
#     def get_min(self):
#         # отримати найменший елемент
#
#         node = self.root
#
#         while node.left is not None:
#             node = node.left
#
#         return node.data
#
#     def find(self, num):
#         # якщо num в корені
#         if self.root.data == num:
#             return True
#
#         return self._recursive_find(self.root, num)
#
#     def _recursive_find(self, tree_node, num):
#         # числа нема
#         if tree_node is None:
#             return False
#
#         # число знайдене
#         if tree_node.data == num:
#             return True
#
#         if num < tree_node.data:
#             return self._recursive_find(tree_node.left, num)
#         else:
#             return self._recursive_find(tree_node.right, num)
#
#
# tree = BinaryTree()
# tree.add(5)
# tree.add(4)
# tree.add(6)
# tree.add(3)
# tree.add(2)
# tree.add(1)
# tree.add(0)
# # tree.display()
# print(tree.get_min())
# print(tree.find(1))
# print(tree.find(10))

import bintrees

class Node:
    def __init__(self, data):
        self.key = data  # вирішуємо наліво чи направо
        self.value = None # додаткова інформація
        self.left = None
        self.right = None


tree = bintrees.AVLTree()

tree.insert(key=10, value='apple')
tree.insert(key=11, value='orange')
tree.insert(key=5, value='pear')
tree.insert(key=9, value='melon')
tree.insert(key=20, value='banana')


# дістати елемент з id 5
print(tree[5])

# ключі str

tree = bintrees.AVLTree()

tree.insert(key='apple', value='sweet juicy apple ')
tree.insert(key='orange', value='orange')
tree.insert(key='pear', value='pear')
tree.insert(key='melon', value='melon')
tree.insert(key='banana', value='banana')

print(tree['apple'])



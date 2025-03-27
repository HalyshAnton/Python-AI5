# Сервер, підключає клієнтів та відповідає
# на їхні запити

# import socket
#
#
# server = socket.socket(socket.AF_INET, # спосіб передачі даних(Інтернет)
#                        socket.SOCK_STREAM # протокол передачі(TCP)
#                        )
#
# # вказуємо де знаходиться сервер
# server.bind(('127.0.0.1', 8080))
#
# # очікуємо підключення клієнтів
# server.listen(1) # чекаємо на одного клієнта
#
# print('Чекаємо на підключення...')
#
# # клієнт заходить з певної адреси на сервер
# client, adress = server.accept()
#
# print(f'Підключився клієнт з адреси {adress}')
#
# # якщо клієнтів 2
# # client1, adress1 = server.accept()
# # client2, adress2 = server.accept()
#
# # спілкування з клієнтом
# while True:
#     # отримуєсо дані від клієнта
#     # повідомлення максиму 1024 байта
#     message = client.recv(1024)
#
#     message_str = message.decode()
#
#     # чи зупиняти з'єднання з клієнтом
#     if message_str == '':
#         break
#
#     # відповідь сервера
#     print(f'Клієнт: {message_str}')
#
#     response = input("Ваша відповідь: ")
#     response_bytes = response.encode()
#
#     # надсилаємо відповідь
#     # надсилаємо те саме повідомлення
#     client.send(response_bytes)
#
# # розриваємо зв'язок з клієнтом
# client.close()
# server.close()


#------------------------------------------------------
# повідомлення не str

import socket
import json


server = socket.socket(socket.AF_INET, # спосіб передачі даних(Інтернет)
                       socket.SOCK_STREAM # протокол передачі(TCP)
                       )

# вказуємо де знаходиться сервер
server.bind(('127.0.0.1', 8080))

# очікуємо підключення клієнтів
server.listen(1) # чекаємо на одного клієнта

print('Чекаємо на підключення...')

# клієнт заходить з певної адреси на сервер
client, adress = server.accept()

print(f'Підключився клієнт з адреси {adress}')

# якщо клієнтів 2
# client1, adress1 = server.accept()
# client2, adress2 = server.accept()

# спілкування з клієнтом
while True:
    # отримуєсо дані від клієнта
    # повідомлення максиму 1024 байта
    data = client.recv(1024)

    # декодування
    data = data.decode()
    data = json.loads(data)

    user_name = data['user_name']
    message_str = data['message']

    # чи зупиняти з'єднання з клієнтом
    if message_str == '':
        break

    # відповідь сервера
    print(f'{user_name}: {message_str}')

    response = input("Ваша відповідь: ")
    response_bytes = response.encode()

    # надсилаємо відповідь
    # надсилаємо те саме повідомлення
    client.send(response_bytes)

# розриваємо зв'язок з клієнтом
client.close()
server.close()

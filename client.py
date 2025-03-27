# клієнт, надсилає запит на сервер
# та отримує від нього відповідь

# import socket
#
# client = socket.socket(socket.AF_INET, # спосіб передачі даних(Інтернет)
#                        socket.SOCK_STREAM # протокол передачі(TCP)
#                        )
#
# # підключаємося до сервера
# client.connect(("127.0.0.1", 8080))
#
# # спілкування з сервером
# while True:
#     message = input('Ваше повідомлення: ')
#
#     # переводимо повідомлення в байти
#     message_bytes = message.encode()
#
#     # надсилаємо повідомлення на сервер
#     client.send(message_bytes)
#
#     # чи зупиняти з'єднання з сервером
#     if message == '':
#         break
#
#     # отримуємо відповідь
#     response = client.recv(1024)
#
#     # перевести байти в str
#     response_str = response.decode()
#
#     print(f'Сервер: {response_str}')
#
# client.close()



#--------------------------------------------------
# повідомлення не str

import socket
import json

client = socket.socket(socket.AF_INET, # спосіб передачі даних(Інтернет)
                       socket.SOCK_STREAM # протокол передачі(TCP)
                       )

# підключаємося до сервера
client.connect(("127.0.0.1", 8080))

user_name = input("Ведіть ваше ім'я: ")

# спілкування з сервером
while True:
    message = input('Ваше повідомлення: ')

    # словник з даними на відправлення
    data = {'user_name': user_name,
            'message': message
            }

    # кодуємо повідомлення через json
    data_json = json.dumps(data)

    # переводимо повідомлення в байти
    message_bytes = data_json.encode()

    # надсилаємо повідомлення на сервер
    client.send(message_bytes)

    # чи зупиняти з'єднання з сервером
    if message == '':
        break

    # отримуємо відповідь
    response = client.recv(1024)

    # перевести байти в str
    response_str = response.decode()

    print(f'Сервер: {response_str}')

client.close()

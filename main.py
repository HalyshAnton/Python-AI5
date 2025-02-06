def func():
    print('hello')


filename = 'password.txt'

with open(filename, 'r') as file:
    lines = file.readlines()


line1 = lines[0]
name, password = line1.split()

print(password)
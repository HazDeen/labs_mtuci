#1
with open('example.txt','r') as file:
    content = file.read()
    print(content)

with open('example.txt','r') as file:
    for line in file:
        print(line)

#2
text = input('Введите текст:')
with open('user_input.txt','a') as file2:
    file2.write(text)

#3
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Файл не найден')

try:
    with open('ВИИТ3.txt', 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print('Файл не найден')
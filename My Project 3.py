def count_words(s):
    words = s.split()
    return len(words)

sentence = "Владимир Жириновский, был прав!"
print(f"Количество слов в строке: {count_words(sentence)}")


def count_words(s):
    words = s.split()
    return len(words)

sentence = "Я смотрю фильмы в формате IMAX!"
print(f"Количество слов в строке: {count_words(sentence)}")


def count_words(s):
    words = s.split()
    return len(words)

sentence = "Моя мама - самая красивая, умная!"
print(f"Количество слов в строке: {count_words(sentence)}")


def count_words(s):
    words = s.split()
    return len(words)

sentence = "Владислав - самый лучший старшак с Турксибского района!"
print(f"Количество слов в строке: {count_words(sentence)}")



str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")



if sorted(str1) == sorted(str2):

    print("Строки являются анаграммами")
else:
    print("Строки не являются анаграммами")



str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")



if sorted(str1) == sorted(str2):

    print("Строки являются анаграммами")
else:
    print("Строки являются анаграммами")



num = int(input("Введите число: "))
for i in range(1, 20):
    print(f"{num} x {i} = {num * i}")


n = int(input("Введите количество чисел Фибоначчи: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print(f"НОД чисел {num1} и {num2}: {gcd(num1, num2)}")



numbers = [1933, 2005, 1912, 1990, 1953, 2012, 1953, 1941, 2024, 2010]
numbers.sort()
print("Отсортированный список:", numbers)



rows = int(input("Please Enter the total Number of Rows: "))

print("Inverted Right Triangle Pattern of Numbers")
i = rows
while(i >= 1):
    j = 1
    while(j <= i):
        print('%d ' %i, end = ' ')
        j = j + 1
    i = i - 1
    print()



 import csv

data = [
    ["Имя", "Возраст", "Город"],
    ["Виктория", 18, "Астана"],
    ["Елизавета", 17, "Алматы"],
    ["Павел", 24, "Костанай"]
]

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV-документ создан!")



import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

cursor.execute("INSERT INTO users (name, age) VALUES ('Виктория', 18)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Елизавета', 17)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Павел', 24)")

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()




from collections import Counter
import string

text = input("Введите текст: ")

text = text.translate(str.maketrans('', '', string.punctuation)).lower()

words = text.split()

word_count = Counter(words)

print("Количество вхождений каждого слова:")
for word, count in word_count.items():
    print(f"'{word}': {count}")




def is_number_palindrome(n):

    n_str = str(n)
    return n_str == n_str[::-1]

number = int(input("Введите число: "))

if is_number_palindrome(number):
    print("Число является палиндромом.")
else:
    print("Число не является палиндромом.")


def is_number_palindrome(n):

    n_str = str(n)
    return n_str == n_str[::-1]

number = int(input("Введите число: "))

if is_number_palindrome(number):
    print("Число является палиндромом.")
else:
    print("Число является палиндромом.")



schedule = {
    "Понедельник": ["8:00 - 9:30 - Комп. графика", "9:40 - 10:50 - Экономика", "11:05 - 12:55 - Основы права"],
    "Вторник": ["8:00 - 9:30 - Физкультура", "9:40 - 10:50 - ИКТ", "11:05 - 12:55 - Охрана труда"],
    "Среда": ["8:00 - 9:30 - Физкультура", "9:40 - 10:50 - Экономика", "11:05 - 12:55 - Электроника"],
    "Четверг": ["8:00 - 9:30 - Основы программирования", "9:40 - 10:50 - Политология", "11:05 - 12:55 - Этика и общения"],
    "Пятница": ["8:00 - 9:30 - Культурология", "9:40 - 10:50 - Робототехника", "11:05 - 12:55 - Электротехника"]
}

def print_schedule(schedule):
    for day, lessons in schedule.items():
        print(f"{day}:")
        for lesson in lessons:
            print(f"  - {lesson}")
        print()

print_schedule(schedule)






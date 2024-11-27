from fractions import Fraction

def solve_fraction_problem():
    a = input("Введите первую дробь (в формате a/b): ")
    b = input("Введите вторую дробь (в формате a/b): ")

    frac_a = Fraction(a)
    frac_b = Fraction(b)

    sum_result = frac_a + frac_b
    diff_result = frac_a - frac_b
    prod_result = frac_a * frac_b
    div_result = frac_a / frac_b

    print(f"Сумма: {sum_result}")
    print(f"Разность: {diff_result}")
    print(f"Произведение: {prod_result}")
    print(f"Частное: {div_result}")

solve_fraction_problem()


import threading

def start_timer(seconds):
    print(f"Таймер запущен на {seconds} секунд...")
    threading.Timer(seconds, time_is_up).start()

def time_is_up():
    print("Время вышло!")

start_timer(50)


import threading

def start_timer(minutes):
    print(f"Таймер запущен на {minutes} минута...")
    threading.Timer(minutes, time_is_up).start()

def time_is_up():
    print("Время вышло!")

start_timer(5)


def calculate_current(voltage, resistance):
    """Вычисление тока по закону Ома: I = V / R"""
    return voltage / resistance

def calculate_voltage(current, resistance):
    """Вычисление напряжения по закону Ома: v = I * R"""
    return current * resistance

def calculate_resistance(voltage, current):
    """Вычисление сопротивления по закону Ома: R = V / I"""
    return voltage / current

V = 3.5
R = 5

I = calculate_current(V, R)
print(f"Сила тока: {I} А")

calculate_voltage = calculate_voltage(I, R)
print(f"Напряжение: {calculated_voltage} В")

calculated_resistance = calculate_resistance(V, I)
print(f"Сопротивление: {calculated_resistance} Ом")


def calculate_current(voltage, resistance):
    """Вычисление тока по закону Ома: I = V / R"""
    return voltage / resistance

def calculate_voltage(current, resistance):
    """Вычисление напряжения по закону Ома: v = I * R"""
    return current * resistance

def calculate_resistance(voltage, current):
    """Вычисление сопротивления по закону Ома: R = V / I"""
    return voltage / current

V = 4.5
R = 5

I = calculate_current(V, R)
print(f"Сила тока: {I} А")

calculate_voltage = calculate_voltage(I, R)
print(f"Напряжение: {calculated_voltage} В")

calculated_resistance = calculate_resistance(V, I)
print(f"Сопротивление: {calculated_resistance} Ом")


def calculate_current(voltage, resistance):
    """Вычисление тока по закону Ома: I = V / R"""
    return voltage / resistance

def calculate_voltage(current, resistance):
    """Вычисление напряжения по закону Ома: v = I * R"""
    return current * resistance

def calculate_resistance(voltage, current):
    """Вычисление сопротивления по закону Ома: R = V / I"""
    return voltage / current

V = 4.5
R = 9


I = calculate_current(V, R)
print(f"Сила тока: {I} А")

calculate_voltage = calculate_voltage(I, R)
print(f"Напряжение: {calculated_voltage} В")

calculated_resistance = calculate_resistance(V, I)
print(f"Сопротивление: {calculated_resistance} Ом")

import math

def binomial_theorem(a, b, n):
    """Вычисление разложения (a+b)^n по формуле Бинома Ньютона"""
    result = 0

    for k in range(n+1):

        binomial_coeff = math.comb(n, k)

        term = binomial_coeff * (a*(n - k)) * (b*k)
        result += term
        print(f"Член {k}: {binomial_coeff} * ({a}^{n - k}) * ({b}^{k}) = {term}")

a = 3
b = 4
n = 5

result = binomial_theorem(a, b, n)
print(f"\nРазложение (a + b)^n: {result}")


import math

def binomial_theorem(a, b, n):
    """Вычисление разложения (a+b)^n по формуле Бинома Ньютона"""
    result = 0

    for k in range(n+1):

        binomial_coeff = math.comb(n, k)

        term = binomial_coeff * (a*(n - k)) * (b*k)
        result += term
        print(f"Член {k}: {binomial_coeff} * ({a}^{n - k}) * ({b}^{k}) = {term}")

a = 8
b = 9
n = 10

result = binomial_theorem(a, b, n)
print(f"\nРазложение (a + b)^n: {result}")


import math

def binomial_theorem(a, b, n):
    """Вычисление разложения (a+b)^n по формуле Бинома Ньютона"""
    result = 0

    for k in range(n+1):

        binomial_coeff = math.comb(n, k)

        term = binomial_coeff * (a*(n - k)) * (b*k)
        result += term
        print(f"Член {k}: {binomial_coeff} * ({a}^{n - k}) * ({b}^{k}) = {term}")

a = 1
b = 2
n = 3

result = binomial_theorem(a, b, n)
print(f"\nРазложение (a + b)^n: {result}")


russian_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
print(russian_alphabet)


alphabet = list["abcdefghijklmnopqrstuvwxyz"]
print(alphabet)


data = [
    {"name": "Илья", "age": 20},
    {"name": "Дарья", "age": 18},
    {"name": "Виктория", "age": 19},
]

sorted_data = sorted(data, key=lambda x: x['age'])
print(f"Отсортированные данные (по возрасту): {sorted_data}")


data = [
    {"name": "Виктор", "age": 25},
    {"name": "Михаил", "age": 30},
    {"name": "Полина", "age": 21},
]

sorted_data = sorted(data, key=lambda x: x['age'])
print(f"Отсортированные данные (по возрасту): {sorted_data}")


data = [
    {"name": "Кирилл", "age": 26},
    {"name": "Анастасия", "age": 20},
    {"name": "Антон", "age": 28},
]

sorted_data = sorted(data, key=lambda x: x['age'])
print(f"Отсортированные данные (по возрасту): {sorted_data}")


import math

number = 33
base = 8
log_result = math.log(number, base)

print(f"Логарифм числа {number} по основанию {base}: {log_result}")


import math

number = 12
base = 7
log_result = math.log(number, base)

print(f"Логарифм числа {number} по основанию {base}: {log_result}")


import math

number = 100
base = 2
log_result = math.log(number, base)

print(f"Логарифм числа {number} по основанию {base}: {log_result}")


import math

number = 50
base = 4
log_result = math.log(number, base)

print(f"Логарифм числа {number} по основанию {base}: {log_result}")


def palindrome(s):
    return s[::-1] == s
while True:
    s = input("Enter a palindrome: ")
    print(f"{s} is palindrome!" if palindrome(s) else "not a palindrome")


age = int(input("Введите ваш возраст: "))
has_permission = input("У вас есть разрешение? (да/нет): ").strip().lower()

if age >= 18 and has_permission == "да":
    print("Вы можете войти.")
else:
    print("Доступ запрещен.")


class Book:
    def _init_(self, title, author, year, content):
        """Инициализация книги с нужными аттрибутами"""
        self.title = title
        self.author = author
        self.year = year
        self.content = content

    def display_info(self):
        """Выводит информацию о книге"""
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print(f"Содержание: {self.content[:3407]}...")

    def update_content(self, new_content):
        """Обновляет содержание книги"""
        self.content = new_content
        print("Содержание книги обновлено.")

my_book = Book(
    title="Гарри Поттер",
    author="Дж.К.Роулинг",
    year=1997,
    content="Представляет собой хронику приключений юного волшебника Гарри Поттера, ..."
)

my_book.display_info()

my_book.update_content("посвящён противостоянию Гарри и тёмного волшебника по имени лорд Волан-де-Морт,")
my_book.display_info()

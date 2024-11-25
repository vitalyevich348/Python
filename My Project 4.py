def common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

list1 = [50, 51, 52, 53, 54]
list2 = [52, 53, 54, 55, 56]

result = common_elements(list1, list2)
print(result)


def common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

list1 = [12, 13, 14, 15, 16]
list2 = [14, 15, 16, 17, 18]

result = common_elements(list1, list2)
print(result)


def common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

list1 = [23, 24, 25, 26, 27]
list2 = [25, 26, 27, 28, 29]

result = common_elements(list1, list2)
print(result)


s = "Хватит это терпеть!"
reversed_s = s[::-1]
print(reversed_s)


s = "Мое ощущение полная беспомощность"
reversed_s = s[::-1]
print(reversed_s)


s = "Расписание составлено неправильно"
reversed_s = s[::-1]
print(reversed_s)


s = "Оплата прошла успешно"
reversed_s = s[::-1]
print(reversed_s)


import math

def calculate_leg (c, a):
    return math.sqrt(c*2 - a*2)

c = 13
a = 5
b = calculate_leg(c, a)
print(f"Катет: {b}")


import math

def calculate_leg (c, a):
    return math.sqrt(c*2 - a*2)

c = 10
a = 6

b = calculate_leg(c, a)
print(f"Катет: {b:.2f}")


from pathlib import Path

folder_path = Path("new_folder")

if not folder_path.exists():
    folder_path.mkdir()
    print(f"Папка '{folder_path}' была успешно создана.")
else:
    print(f"Папка '{folder_path}' уже существует.")


numbers = [1330, 849, 120, 107, 871]
numbers.sort()
print("Отсортированный список:", numbers)


numbers = [140, 137, 1110, 250, 853]
numbers.sort()
print("Отсортированный список:", numbers)


numbers = [1370, 1400, 490, 2500, 23]
numbers.sort()
print("Отсортированный список:", numbers)


numbers = [220, 10, 219, 230, 49]
numbers.sort()
print("Отсортированный список:", numbers)


my_list = [14, 146, 180, 540, 40]

max_value = max(my_list)
print(max_value)


my_list = [16, 441, 140, 711, 40]

max_value = max(my_list)
print(max_value)


my_list = [195, 720, 314, 540, 403]

max_value = max(my_list)
print(max_value)


numbers_input = input("Введите числа через пробел:")

numbers = list(map(int, numbers_input.split()))

average = sum(numbers) / len(numbers)

print("Среднее арифметическое чисел:", average)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
result = gcd(a, b)
print(f"Наибольший общий делитель ({a}, {b}) = {result}")


N = int(input("Введите число N: "))

total_sum = sum(range(1, N + 1))

print(f"Сумма чисел от 1 до {N} равна {total_sum}")


headers = ["Название кинотеатра", "Дата открытия", "Место нахождения"]
data = [
    ["Kinopark 11 Esentai IMAX", 2012, "пр.Аль-Фараби 77/8"],
    ["Kinoplexx 7 Aport", 2019, "ул.Ташкентский тракт 117К"],
    ["Halyk IMAX Kinopark 16", 2023, "ул.Кульджинский тракт 106"],
    ["Kinopark 4 Globus", 2021, "пр.Абая 109В"]
]


def print_table(headers, data):
    print(f"{headers[0]:<10} {headers[1]:<10} {headers[2]:<15}")
    print("-" * 35)

    for row in data:
        print(f"{row[0]:<10} {row[1]:<10} {row[2]:<15}")


print_table(headers, data)


def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка: {e}"


def main():
    print("Простой калькулятор. Введите математическое выражение (например, 8 + 4) или 'выход' для завершения.")

    while True:
        expression = input("Введите пример: ")

        if expression.lower() == 'выход':
            print("Завершение работы программы.")
            break

        result = calculate(expression)

        print(f"Результат: {result}")


if _name_ == "_main_":
    main()


my_list = []

n = int(input("Введите количество элементов в списке: "))

for i in range(n):
    element = input(f"Введите элемент {i+1}: ")
    my_list.append(element)

print("Ваш список:", my_list)

index_to_change = int(input("Введите индекс элемента, который хотите изменить: "))
new_value = input("Введите новое значение для этого элемента: ")

if 0 <= index_to_change < len(my_list):
    my_list[index_to_change] = new_value
    print("Список после изменения:", my_list)
else:
    print("Некорректный индекс.")

index_to_remove = int(input("Введите индекс элемента для удаления: "))

if 0 <= index_to_remove < len(my_list):
    removed_element = my_list.pop(index_to_remove)
    print(f"Элемент {removed_element} был удален. Текущий список: {my_list}")
else:
    print("Некорректный индекс.")






    

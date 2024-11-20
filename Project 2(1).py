n = int(input())

suma = 0
mult = 1

while n > 0:
    digit = n % 10
    suma = suma + digit
    mult = mult * digit
    n = n // 10

print(suma)
print(mult)



def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

decimal_number = int(input())
binary_number = decimal_to_binary(decimal_number)
print(f"Двоичное представление: {binary_number}")


def fibonacci_recursive(n):

    if n <=1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


n = int(input("Введите номер числа Фибоначчи: "))


result = fibonacci_recursive(n)
print(f"Число Фибоначчи с индексом {n}: {result}")



def find_max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num

numbers = [5, 12, 19, 26, 4, 11, 18, 25]
max_num, min_num = find_max_min(numbers)
print(f"Максимум: {max_num}, Минимум: {min_num}")



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [56, 34, 34, 90, 123, 68, 45]
bubble_sort(arr)
print("Отсортированный массив:", arr)


import itertools

def generate_permutations(arr):
    return list(itertools.permutations(arr))

arr = [6, 10, 45]
permutations = generate_permutations(arr)
print("Перестановки:", permutations)



def recursive_search(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return recursive_search(arr, target, index + 1)

arr = [9, 17, 18, 1, 100]
target = 18
print(recursive_search(arr, target))



i = 0
while i < 26:
    i += 2
    print(i)
print("конец")


i = 0
while i < 10:
    i += 2
    print(i)
print("конец")


i = 0
while i < 52:
    i += 2
    print(i)
print("конец")

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

word = "racecar"
print(is_palindrome(word))



def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

word = "казак"
print(is_palindrome(word))



def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

word = "starshak"
print(is_palindrome(word))



def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

word = "oscar"
print(is_palindrome(word))




def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

word = "шалаш"
print(is_palindrome(word))



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(8))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(12))


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(10))



# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# n = input("Input number: ")
#
# s = 0
# for i in n:
#     s += int(i)
#
# m = 1
# for i in n:
#     m *= int(i)

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

# print(5 & 6)
# print(5 | 6)
# print(5 ^ 6)
# print(5 >> 2)
# print(5 << 2)

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

# x1 = float(input("Input x1: "))
# y1 = float(input("Input y1: "))
#
# x2 = float(input("Input x2: "))
# y2 = float(input("Input y2: "))

# # y1 - y2== kx1 - kx2

# k = (y1 - y2) / (x1 - x2)
# b = y1 - k * x1

# print(f"y={k}x+{b}")

# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
# import random

# begin = int(input("Input begin int: "))
# end = int(input("Input end int: "))

# print(random.randint(begin, end))

# begin = float(input("Input begin float: "))
# end = float(input("Input end float: "))

# print(random.uniform(begin, end))

# begin = input("Input begin symbol: ")
# end = input("Input end symbol: ")

# print(chr(random.randint(ord(begin), ord(end))))

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

# import string

# letter_one = input("Input letter 1: ").lower()
# letter_two = input("Input letter 2: ").lower()
#
# first = string.ascii_lowercase.index(letter_one)
# second = string.ascii_lowercase.index(letter_two)
# print(letter_one, first)
# print(letter_two, second)
#
# print("How many letters:",second - first - 1)

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# import string
#
# letter = input("Input letter 1: ")
#
# print(string.ascii_lowercase.index(letter) + 1)


# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

# a = int(input("Input a: "))
# b = int(input("Input b: "))
# c = int(input("Input c: "))
#
# if a + b + c >= 2 * max(a, b, c):
#     print("Triangle exists")
#
#     if a == b and b == c:
#         print("All sides are equal")
#     elif a == b or b == a or b == c:
#         print("Two sides are equal")
#     else:
#         print("No equal sides")
# else:
#     print("Triangle not exists")


# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

# year = int(input())
# if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
#     print("usual year")
# else:
#     print("intercalary year")

# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

middle = a

if a < b < c or c < b < a:
    middle = b
elif a < c < b or b < c < a:
    middle = c

print(middle)

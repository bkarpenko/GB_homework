﻿import random, string, re


#1 Найти сумму и произведение цифр трехзначного числа, которое вводит import random, string, re


#1 Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = input("введите 3-х значное число\n")
s = sum(map(int, n))
p = 1
for each in n:
    p *= int(each)
print("сумма чисел =", s, "\nпроизведение чисел =", p)


#4 Написать программу, которая генерирует в указанных пользователем границах: 

n = input("введите 3-х значное число\n")
s = sum(map(int, n))
p = 1
for each in n:
    p *= int(each)
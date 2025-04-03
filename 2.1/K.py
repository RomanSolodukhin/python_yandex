"""Итак, в этой задаче вы научитесь работать с числовыми данными и формировать числа при помощи математических операций.

Напишите программу для робота-няни, которая из числа вида abcd составляет число badc.

Формат ввода
Одно четырёхзначное число.

Формат вывода
Одно четырёхзначное число — результат перестановки."""
four_digit_number = int(input())
a_number = int(four_digit_number // 1000)
b_number = int(four_digit_number // 100 % 10)
c_number = int(four_digit_number // 10 % 10)
d_number = int(four_digit_number % 10)
"""abcd => badc"""
print(b_number, a_number, d_number, c_number, sep='')
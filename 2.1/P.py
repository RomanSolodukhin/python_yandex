"""Продуктовый склад и магазин находятся на одной дороге города Н.
Склад находится на отметке 
A
A км, а магазин — 
B
B км. Средняя скорость автомобиля, доставляющего товары, 
C
C км/ч.
За какое время продукты попадают со склада в магазин?

Формат ввода
Три натуральных числа 
A
A, 
B
B и 
C
C, каждое на отдельной строке.

Формат вывода
Одно рациональное число с точностью до сотых."""
point_A = int(input())
point_B = int(input())
speed = int(input())
distance = abs(point_A - point_B)
print(round(distance / speed, 2))
"""
Усложняем! На этот раз предлагаем научиться обрабатывать текстовые и числовые данные, выполнять арифметические операции и оформлять вывод в форматированном виде.

Для этого напишите программу, которая рассчитывает стоимость покупки и печатает чек в заданном формате. Итоговая стоимость вычисляется как произведение цены за килограмм и веса товара. Если денег у покупателя недостаточно, сдача равна 0.

Формат ввода
Четыре строки:

название товара (строка);
цена товара за килограмм (натуральное число);
вес товара (натуральное число);
количество денег у пользователя (натуральное число).
Формат вывода
Чек
<название товара> - <вес>кг - <цена>руб/кг
Итого: <итоговая стоимость>руб
Внесено: <количество денег от пользователя>руб
Сдача: <сдача>руб
"""
item_title = str(input())
price = int(input())
weight = int(input())
cash = int(input())
total = int(price * weight)
string_1 = f'{item_title} - {weight}кг - {price}руб/кг'
string_2 = f'Итого: {total}руб'
string_3 = f'Внесено: {cash}руб'
string_4 = f'Сдача: {cash - total}руб'
print('Чек', string_1, string_2, string_3, string_4, sep='\n')
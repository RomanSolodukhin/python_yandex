"""
Мы в середине пути. В этой задаче будем учиться работать с числовыми данными,
извлекать информацию из чисел и оформлять результат в заданном формате.

Напишите программу, которая формирует карточку для личного дела ребёнка. Карточка создаётся на основе имени ребёнка и трёхзначного номера шкафчика, который содержит:

Первую цифру — номер группы. Вторую цифру — номер кроватки. Третью цифру — порядковый номер ребёнка в списке группы.

Формат ввода
В первой строке записано имя ребенка.
Во второй строке записан номер шкафчика.

Формат вывода
Карточка в виде:

Группа №<номер группы>.  
<номер ребёнка в списке>. <имя ребенка>.  
Шкафчик: <номер шкафчика>.  
Кроватка: <номер кроватки>.
"""
kid_name = str(input())
locker_id = int(input())
group_id = locker_id // 100
bed_id = locker_id // 10 % 10
kid_id = locker_id % 10
print(f'Группа №{group_id}.', f'{kid_id}. {kid_name}.', f'Шкафчик: {locker_id}.', f'Кроватка: {bed_id}.', sep="\n")
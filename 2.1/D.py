"""""А вот и первая задача по математике! Как насчёт того, чтобы научиться использовать
арифметические операции?

Возьмём простую задачу из школьной математики. Покупатель купил 2.5 кг черешни по цене 38 руб/кг.
Сколько сдачи он получит? Вычислите стоимость покупки, а затем найдите разность между номиналом купюры и этой стоимостью.

Формат ввода
Одно натуральное число - номинал купюры пользователя (
≥
100
≥100).

Формат вывода
Одно натуральное число — размер сдачи.

Примечание
Используйте стандартные арифметические операции. Ответ всегда будет натуральным числом, так как номинал купюры больше стоимости покупки."""
cash = input()
charge = int(cash) - int(38 * 2.5)
print(int(charge))
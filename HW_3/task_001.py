# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X.

import random

n = int(input('Введите количество элементов в массиве: '))
list = []
for i in range(n):
  list.append(random.randint(-5, 5))
print(list)

k = int(input('Какое число искать: '))
count = 0
for i in range(len(list)):
  if list[i] == k:
    count += 1
print(f"Данное число встречается {count} раз")

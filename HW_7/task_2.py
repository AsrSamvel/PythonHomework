# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows, num_colums):
  for x in range(1, num_rows + 1):
    for y in range(1, num_colums + 1):
      if num_colums == y:
        print(operation(x, y))
      else:
        print(operation(x, y), '\t', end='')

rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))

print_operation_table(lambda x, y: x * y, rows, columns)

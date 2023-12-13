# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Пример

# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)

# На выходе:
# 1 2 3
# 2 4 6 
# 3 6 9




def print_operation_table(f, h=9, w=9):
  if h < 2:
    print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    return

  print(*(f(1, k) for k in range(1, w+1)))  
  
  for i in range(2, h+1):
    print(str(f(i,1))[0],end='')
    print(*(f(i, k) for k in range(2, w+1)))
    
#    print(*(f(i, k) for k in range(1, w+1)))

print_operation_table(lambda x, y: x / y, 4, 4)
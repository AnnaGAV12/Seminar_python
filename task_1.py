# Написать программу,которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого .

a = int (input ('a = '))
b = int (input ('b = '))
print ('Квадрат первого числа является вторым числом')

# Первый вариант
# if b==a**2:
#     print('да')
# elif a==b**2:
#     print('нет')
# else:
#     print('числа не являются квадратом друг друга')

# Второй вариант
if ( b == a * a ) or ( a == b * b ):
    print(' -> да')
else:
    print('-> нет')
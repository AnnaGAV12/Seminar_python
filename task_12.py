# Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.

# import time
# limit = int(input("Введите предел: "))
# rnd_number = str(time.time()) #текущее время в мили сек. и переводим в строку
# rnd_number = rnd_number.split(".") # через точку делим строку на левую и правую часть
# rnd_number = int(rnd_number[1]) # првую часть переводим в int
# def random_number(number: int, limit: int): # передаем число и предел в функцию
#     while True:
#         if number > limit:
#             number //= 10
#         else:
#            return number
# print(random_number(rnd_number, limit))


# Другой вариант
# the_set = set()
# for i in range(1000):
#     the_set.add(str(i))
# for e in the_set:
#     print(int(e))
#     break

# Еще вариант
# import datetime 
# def get_rand():
#     return datetime.datetime.now().microsecond%1000
# n = get_rand()
# print(n)
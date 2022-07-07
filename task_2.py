# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры: - 1, 4, 8, 7, 5 -> 8       - 78, 55, 36, 90, 2 -> 90

# a = []
# for i in range(5):
#     x = int (input ('-->'))
#     a.append (x)
# print(a)

# maxx = a[0]
# for i in range(1, len(a)):
#     if a[i] > maxx:
#         maxx = a[i]

# print(maxx)

ist = []
counter = 1
max = -1


while counter < 62:
    list.append(int(input(f'Enter positive number {counter}:')))
    counter += 1

for i in list:
    if i > max: max = i

print(f'Max value in list is {max}')


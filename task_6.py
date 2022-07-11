# for i in range(1, 5): 
#     print(i, end=" ") 
# else:
#     print('\nЦикл for закончен')

# a = [1, 123, 54, 123, 54, 123, 54]
# b = a[:]
# print(b)

def func(param_1: int, param_2: int, param_3: int, param_4: int=10) -> float:
    summ = param_1 + param_2 + param_3 + param_4
    return summ
    
print(func(1, 2, 3, 4))

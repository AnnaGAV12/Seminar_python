# Напишите программу,  которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 1, 2] -> [2]

in_list = [1, 1, 2]
# через фильтер
print(list(filter(lambda x: in_list.count(x) == 1, in_list)))
# через включение
# res =[x for x in in_list if in_list.count(x)==1]
#print(res)
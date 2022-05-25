# В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def search_result(List):
    max_number = 0
    min_number = 1
    result = 0
    for i in List:
        max_number = max(max_number, i % 1)
        min_number = min(min_number, (1 if i % 1 == 0 else i % 1))
        result = round(max_number - min_number, 5)
    return result



List = [1.1, 1.2, 3.1, 5, 10.01]
print(search_result(List))

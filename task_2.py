# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def number_mult(List):
    left_number = 0
    right_number = len(List) - 1
    result = 0
    List2 = []
    
    while left_number <= right_number:
        result = List[left_number] * List[right_number]
        List2.append(result)
        left_number += 1
        right_number -= 1
    return List2




List = [2, 3, 4, 5, 6]
print(number_mult(List))
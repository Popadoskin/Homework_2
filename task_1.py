# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

def Sum_of_numbers(List):
    List_odd_numbers = List[::2]
    summa = 0
    for i in List_odd_numbers:
            summa += i
    return summa 

List = [1, 2, 3, 4]
print('Сумма чисел на нечётной позиции = ', Sum_of_numbers(List))

# p.s. Как я понял из примера, позиция это не индекс =)
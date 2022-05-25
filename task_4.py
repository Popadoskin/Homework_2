# Написать программу преобразования десятичного числа в двоичное

def Transformation(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s

def Print(n):
    if n != 0:
        print('Ответ:', Transformation(n))   
    else: 
        print("Вы ввели 0")

print("Введите число:")
n = int(input())
Transformation(n)
Print(n)

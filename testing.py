import math as m

def legend(x, z, g):

    global y 
    if z == x:
        raise ZeroDivisionError("Деление на ноль! x и z не должны быть равны.")
    
    if (g - x) <= 0:
        raise ValueError("Выражение под логарифмом (g - x) должно быть строго больше нуля.")
    
    y = ((x**2 - g) / (z - x)) + m.log2(g - x)

    return y

while True:
    try:
        x = float(input("Введите значение x: "))
        z = float(input("Введите значение z: "))
        g = float(input("Введите значение g: "))
        break

    except ValueError:
        print('Введено строчное значение. Пожалуйста, введите цифры.\n')
   

def check():  
    try:
        legend(x, z, g)
        print(f"\nРезультат вычисления для ваших данных: {y}")

    except ValueError as ve:
        print(f"\nПроизошла ошибка: {ve}")

    except ZeroDivisionError as zde:
        print(f"\nПроизошла ошибка: {zde}")

check()
    
def check_need():
    try:
        print("\nТест 1 (нормальные данные): x=2, z=4, g=6")
        print("Результат:", legend(2, 4, 6), "\n")
    except Exception as e:
        print("Ошибка:", e, "\n")

    try:
        print("Тест 2 (деление на ноль): x=3, z=3, g=10")
        print("Результат:", legend(3, 3, 10), "\n")
    except Exception as e:
        print("Ошибка:", e, "\n")

    try:
        print("Тест 3 (отрицательный логарифм): x=5, z=2, g=4")
        print("Результат:", legend(5, 2, 4), "\n")
    except Exception as e:
        print("Ошибка:", e, "\n")

check_need()
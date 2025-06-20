import math as m
#тестируемая часть
def Equation(a, b, c):
    #Прооверка ввода
    if isinstance(a, str) is True:
        y = 'TypeError'
    elif isinstance(b, str) is True:
        y = 'TypeError'
    elif isinstance(c, str) is True:
        y = 'TypeError'
    #с не может быть меньше 0 т.к. корня из отрицательногоо числа
    elif c <= 0:
        y = "ValueError: Parameter c must be greater than 0"
    #косинус не может быть 0 т.к. на ноль не делится
    elif m.isclose(m.cos(b), 0.0, abs_tol=1e-9):
        y = "ValueError: b can't be 0"
    else:
        y = (m.sin (a))/(m.cos(b)) + m.sqrt(c)
    return y

 
def calculate_y(a, b, c):
    try:
        result = (m.sin (a))/(m.cos(b)) + m.sqrt(c)
        print("Значение функции y =", result)
    except ValueError as e:
        print(e)
    return result

calculate_y(0.5, 0.3, 4)

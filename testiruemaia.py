import math as m
#тестируемая часть
def Equation(a, b, c):
    if isinstance(a, str) is True:
        y = 'TypeError'
    elif isinstance(b, str) is True:
        y = 'TypeError'
    elif isinstance(c, str) is True:
        y = 'TypeError'
    elif c <= 0:
        y = "ValueError: c can't be less than positive"
    elif m.isclose(m.cos(b), 0.0, abs_tol=1e-9):
        y = "ValueError: b can't be 0"
    else:
        y = (m.sin (a))/(m.cos(b)) + m.sqrt(c)
    return y



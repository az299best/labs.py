'''основная функция для вычислений'''
def calculator(num1, num2, task):
    if task == '+':
        return num1 + num2
    elif task == '-':
        return num1 - num2
    elif task == '*':
        return num1 * num2
    elif task == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Я запрещаю делить на ноль"
    else:
        return "Неизвестная команда"



'''Блок с функциями теста
 --------------------------------------------------------------'''




def test_razn():
    assert calculator(2, 1, '-') == 1
    assert calculator(1, 2, '-') != 4
    assert calculator(0, 0, '-') == 0

def test_summa():
    assert calculator(1, 2, '+') == 3
    assert calculator(1, 2, '+') != 4
    assert calculator(0, 0, '+') == 0

def test_proizv():
    assert calculator(1, 2, '*') == 2
    assert calculator(1, 2, '*') != 4
    assert calculator(0, 0, '*') == 0

def test_delit():
    assert calculator(6, 2, '/') == 3
    assert calculator(1, 2, '/') != 4
    assert calculator(0, 5, '/') == 0
'''-----------------------------------------------'''




'''использование float  а не int позволяет работать с дробными числами 0.0'''
if __name__ == "__main__":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    task = input("Введите знак операции (+, -, *, /): ")
    test_razn()
    test_summa()
    test_proizv()
    test_delit()

    res = calculator(num1, num2, task)

    print(f" {res}")

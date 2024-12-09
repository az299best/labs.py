import logging
import math

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_operation(func):
    def inner_foo(x, y, task):
        logging.info(f"arg1: {x} arg2: {y} cmd: '{task}'")
        result = func(x, y, task)
        return result
    return inner_foo

def convert_precision(tolerance):
    if tolerance <= 0:
        raise ValueError("Толерантность должна быть больше 0")
    return int(abs(math.log10(tolerance)))

@log_operation
def calculator(num1, num2, task, tolerance=1e-6):

    precision = convert_precision(tolerance)
    result = None

    if task == '+':
        result = round(num1 + num2, precision)
    elif task == '-':
        result = round(num1 - num2, precision)
    elif task == '*':
        result = round(num1 * num2, precision)
    elif task == '/':
        if num2 != 0:
            result = round(num1 / num2, precision)
        else:
            result = "Я запрещаю делить на ноль"
    else:
        result = "Неизвестная команда"

    return result

if __name__ == "__main__":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    task = input("Введите знак операции (+, -, *, /): ")
    tolerance = input("Введите точность вычислений или оставьте значение по умолчанию (1е-6): ")

    if tolerance:
        tolerance = float(tolerance)
    else:
        tolerance = 1e-6

    res = calculator(num1, num2, task, tolerance = tolerance)

    print(f"{res}")
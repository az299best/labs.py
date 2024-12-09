import logging
import math
import statistics

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_operation(func):
    def inner_foo(*args, **kwargs):
        logging.info(f"args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return inner_foo

def convert_precision(tolerance):
    if tolerance <= 0:
        raise ValueError("Толерантность должна быть больше 0")
    return int(abs(math.log10(tolerance)))

@log_operation
def calculator(task, *args, tolerance=1e-6):
    precision = convert_precision(tolerance)
    result = None

    if task == '+':
        result = round(sum(args), precision)
    elif task == '-':
        result = round(args[0] - sum(args[1:]), precision)
    elif task == '*':
        result = round(math.prod(args), precision)
    elif task == '/':
        if 0 in args[1:]:
            result = "Я запрещаю делить на ноль"
        else:
            result = round(args[0] / math.prod(args[1:]), precision)
    elif task == "medium":
        result = round(statistics.mean(args), precision)
    elif task == "variance":
        if len(args) > 1:
            result = round(statistics.variance(args), precision)
        else:
            result = "Для вычисления дисперсии нужно более одного числа"
    elif task == "std_deviation":
        if len(args) > 1:
            result = round(statistics.stdev(args), precision)
        else:
            result = "Для вычисления стандартного отклонения нужно более одного числа"
    elif task in {"median", "q2"}:
        result = round(statistics.median(args), precision)
    elif task == "q3-q1":
        sorted_args = sorted(args)
        mid = len(sorted_args) // 2
        q1 = statistics.median(sorted_args[:mid])
        q3 = statistics.median(sorted_args[mid + (len(sorted_args) % 2):])
        result = round(q3 - q1, precision)
    else:
        result = "Неизвестная команда"

    return result

if __name__ == "__main__":
    numbers = input("Введите числа через пробел: ")
    numbers = list(map(float, numbers.split()))
    task = input("Введите знак операции (+, -, *, /, medium, variance, std_deviation, median, q3-q1): ")
    tolerance = input("Введите точность вычислений или оставьте значение по умолчанию (1e-6): ")

    if tolerance:
        tolerance = float(tolerance)
    else:
        tolerance = 1e-6

    res = calculator(task, *numbers, tolerance=tolerance)

    print(f"Результат: {res}")
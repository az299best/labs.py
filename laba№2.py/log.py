import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_operation(func):
    def inner_foo(x, y, task):
        logging.info(f"arg1: {x} arg2: {y} cmd: '{task}'")
        result = func(x, y, task)
        # logging.fatal(f"result={result}")
        return result
    return inner_foo


@log_operation
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


if __name__ == "__main__":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    task = input("Введите знак операции (+, -, *, /): ")

    res = calculator(num1, num2, task)

    print(f"{res}")
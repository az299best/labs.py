class BatchCalculatorContextManager:

    def init(self, file_path):

        self.file_path = file_path
        self.file = None

    def enter(self):

        try:
            self.file = open(self.file_path, "r")
            return self.file

        except FileNotFoundError:
            print("Файл не найден!")
            return None

    def exit(self, exc_type, exc_value, tb):

        if self.file:
            self.file.close()


class Calculator:
    @staticmethod
    def calculate(expression):
        try:
            result = eval(expression)
            return result
        except:
            print("Ошибка вычисления!")
            return None


def expression_generator(file):
    for line in file:
        yield line.strip()


file_path = "expressions.txt"

calculator = Calculator()

with BatchCalculatorContextManager(file_path) as file:
    if file:
        for expression in expression_generator(file):
            result = calculator.calculate(expression)
            if result is not None:
                print(f"Результат {expression} = {result}")
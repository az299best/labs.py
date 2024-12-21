import time


class Timer:
    def enter(self):
        self.start = time.perf_counter()
        return self

    def exit(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"Время выполнения: {self.elapsed:.2f} секунд")


def fibonacci_generator(n):
    num1, num2 = 0, 1
    for _ in range(n):
        yield num1
        num1, num2 = num2, num1 + num2


n = 1000

with Timer():
    fib_numbers = list(fibonacci_generator(n))

print(f"Последнее число Фибоначи: {fib_numbers[-1]}")
import functools
import itertools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res

def my_genn():
    """Сопрограмма"""

    number_of_fib_elem = yield
    while True:
        if number_of_fib_elem is None or number_of_fib_elem <=0:
            l=[]
        else:
            l = list(itertools.islice(fib_elem_gen(),number_of_fib_elem))
        number_of_fib_elem = yield l

def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


my_genn = fib_coroutine(my_genn)


class FibonacchiLst:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while   True:
            try:
                num=self.instance[self.idx]
            except IndexError:
                raise StopIteration
            self.idx += 1
            if self._is_number_fibonachi_(num):
                return num
            # проверка

    @staticmethod
    def _is_number_fibonachi_(num):
        if num<0 :
            return False
        a=0
        b=1
        while a<num:
            a,b=b,a+b
        return a==num
if __name__ == "__main__":
    l = [0, 1, 16, 21, 4, -10, 1, 1, 1, 7, 8, 9, 13, 134]
    new_list=list(FibonacchiLst(l))
    print(new_list)
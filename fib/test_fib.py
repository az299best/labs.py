from main import my_genn
from main import FibonacchiLst

def test_fib_1():
    gen = my_genn()
    assert gen.send(3) == [0, 1, 1]


def test_fib_2():
    gen = my_genn()
    assert gen.send(5) == [0, 1, 1, 2, 3]


def test_fib_3():
    gen = my_genn()
    assert gen.send(8) == [0, 1, 1, 2, 3,5,8,13]

def test_one():
    gen = my_genn()
    assert gen.send(1) ==[0]

def test_two():
    gen = my_genn()
    assert gen.send(2) == [0, 1]

def test_minus():
    gen = my_genn()
    assert gen.send(-10) == []

def test_zero():
    gen = my_genn()
    assert gen.send(0) == []

def test_large():
    gen = my_genn()
    res= gen.send(20)
    assert res[-1]==4181

def test_two_corutines():
    gen1 =my_genn()
    gen2 =my_genn()

    assert gen1.send(5) ==[0, 1, 1, 2, 3]
    assert gen2.send(5) ==[0, 1, 1, 2, 3]
    assert gen1.send(3) ==[0, 1, 1]
    assert gen2.send(2) ==[0, 1]

#-----------

def test_class_fib():
    l = [0, 1, 16, 21, 4, -10, 1, 1, 1, 7, 8, 9, 13, 134]
    new_list = list(FibonacchiLst(l))
    assert new_list==[0, 1, 21, 1, 1, 1, 8, 13]

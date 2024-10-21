def wrapper(x: int):
    def inner_foo(y: int):
        z = 1
        print(x, y, z)
    return inner_foo


closure = wrapper(10)
closure(5)
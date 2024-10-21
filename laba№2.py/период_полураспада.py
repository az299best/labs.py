def function(t_half: float, N0: float, t: float):
    return N0 * (0.5 ** (t/t_half))

def carried_func(t_half: float):
    def inner_foo(N0: float, t: float):
        return function(t_half, N0, t)
    return inner_foo

isotops = {
    "U-238": 4500000000,
    "U-235": 713000000,
    "Pa-231": 34300
}

N0 = 1000

if __name__ == "__main__":
    for isotop, t_half in isotops.items():
        carried_f = carried_func(t_half)

        t = 30000

        remained_amount = carried_f(N0, t)
        print(f"Изотоп: {isotop} оставшееся количество вещества: {remained_amount}")
import matplotlib.pyplot as plt


def foo1():
    y = []
    for i in range(10):
        y.append(i * (-2) - 2)
    return list(range(10)), y


def foo2():
    y = []
    for i in range(10):
        y.append(i / 2)
    return list(range(10)), y


def foo3():
    y = []
    for i in range(10):
        y.append(1 / (2 * (i+1)))
    return list(range(10)), y


plt.figure(1)
plt.plot(foo1()[0], foo1()[1], color='blue')
plt.plot(foo2()[0], foo2()[1], color='red')
plt.grid()

plt.figure(2)
plt.plot(foo3()[0], foo3()[1], color='green')
plt.grid()

plt.show()
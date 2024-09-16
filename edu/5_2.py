from math import ceil


def f(z, x):
    n = len(z)
    z = [0] + z
    x = [0] + x

    summa = 0
    for i in range(1, len(x)):
        summa += (x[i] - 83 * z[n + 1 - i] ** 3 - x[ceil(i / 2)] ** 2) ** 6
    return 48 * summa


result = f([0.9, -0.7, -0.22], [0.93, -0.1, 0.52])

print(result)

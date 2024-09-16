from math import ceil


def f(x, y, z):
    z = [0] + z
    x = [0] + x
    y = [0] + y

    summa = 0
    for i in range(1, len(x)):
        summa += 19 * x[i] + y[ceil(i / 2)] ** 2 + 78 * z[ceil(i / 4)] ** 3
    return summa


result = f(
    [0.94, -0.18, 0.87, 0.21], [-0.11, 0.84, 0.64, 0.29], [0.34, -0.95, -0.81, 0.62]
)

print(result)

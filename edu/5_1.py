from math import ceil


def f(z, x, y):
    z = [0] + z
    x = [0] + x
    y = [0] + y

    summa = 0
    for i in range(1, len(x)):
        summa += (24 * x[ceil(i / 4)] + z[ceil(i / 4)] ** 2 + 48 * y[i] ** 3) ** 7
    return summa


result = f(
    [0.6, -0.95, -0.52, 0.85, -0.92, 0.38, 0.02, 0.12],
    [-0.48, 0.41, 0.87, 0.05, 0.22, 0.13, -0.7, 0.72],
    [0.8, -0.95, -0.01, 0.75, 0.67, 0.7, 0.16, 0.84],
)

print(result)

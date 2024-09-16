from math import exp, ceil


def main(x, y, z):
    n = len(x)
    summa = 0
    for i in range(1, n + 1):
        summa += 41 * exp(x[n - ceil(i / 3)] ** 3 - z[n - i] - y[n - i] ** 2) ** 4
    return summa


print(
    main(
        [-0.91, 0.87, -0.63, -0.35, -0.09],
        [0.14, -1.0, -0.25, -0.96, 0.29],
        [-0.03, -0.61, 0.58, 0.36, -0.58],
    )
)

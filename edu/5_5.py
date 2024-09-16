from math import ceil


def main(x):
    x = [0] + x
    summa = 0
    for i in range(1, len(x)):
        summa += 97 * (83 - 99 * x[ceil(i / 2)] ** 2 - x[ceil(i / 2)] ** 3) ** 6
    return summa


print(main([-0.25, 0.67, -0.37]))

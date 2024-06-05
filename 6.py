from math import ceil


def decart_product_of_sets(a, b):
    ans = set()
    for x in a:
        for y in b:
            ans.add((x, y))
    return ans


def main(input_data):
    e = {(ceil(x / 4) - (x % 3)) for x in input_data}
    h = {(x**2) for x in input_data if x > -55}
    delta = {x**2 for x in h}
    big_lambda = e.union(h)

    summa = 0
    for small_lambda in big_lambda:
        summa += 3 * small_lambda

    diapason = decart_product_of_sets(big_lambda, delta)
    p = 1
    for small_lambda, small_delta in diapason:
        p *= small_lambda % 2 - small_delta % 3

    return summa + p

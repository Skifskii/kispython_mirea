from math import ceil, floor, prod


def main(B):
    Delta = {ceil(b / 2) + 8 * b for b in B if b > 4}
    X = {abs(b) for b in B}
    I = Delta.union(X)
    Z = {floor(x / 3) - i for x in X for i in I if x <= i}

    return len(I.union(Z)) + prod(c % 3 for c in Z)


print(main({32, 75, -50, 16, -79, 49, 22, 59, -68}))

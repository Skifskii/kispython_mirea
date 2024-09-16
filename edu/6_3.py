from math import ceil


def main(H):
    F = {ceil(h / 2) for h in H}
    O = {h**3 + h for h in H if (-16 < h <= 23)}
    X = F.union(O)

    return sum(6 * o for o in O) - sum(8 * x for x in X)


print(main({5, 38, 72, 42, -20, 82, -14, 20, -43, 58}))

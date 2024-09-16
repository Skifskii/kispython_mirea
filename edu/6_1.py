from math import ceil


def main(i):
    p = {3 * epsilon for epsilon in i}
    h = {abs(ro) for ro in p if -40 < ro}
    t = i.union(p)

    summa = sum(tao - ceil(nu / 7) for tao in t for nu in h)

    return len(t) - summa


print(main({33, -95, 42, -51, -47, 85, -74, -39, 60, -65}))

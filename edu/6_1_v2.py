from math import ceil


def main(i):
    P = {3 * eps for eps in i if (-55 < eps <= 72)}
    H = {abs(p) for p in P if (-40 < p)}
    T = i.union(P)

    summa = sum(t - ceil(h / 7) for t in T for h in H)
    return len(T) - summa


print(main({33, -95, 42, -51, -47, 85, -74, -39, 60, -65}))

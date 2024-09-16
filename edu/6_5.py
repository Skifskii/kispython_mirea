from math import ceil


def main(H):
    T = {h for h in H if h < 1}
    Delta = {t**3 - ceil(t / 2) for t in T if -76 < t <= 14}
    B = {h % 2 - t for h in H for t in T if h >= t}

    return sum(b**3 for b in B) + sum(abs(delta) for delta in Delta)


print(main({32, 35, -88, -54, -53, -20, 78, -49, 22, -40}))

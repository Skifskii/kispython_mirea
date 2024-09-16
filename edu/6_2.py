from math import ceil


def main(omega):
    big_k = {abs(w) for w in omega if (-53 <= w <= 18)}
    big_f = {ceil(w / 7) for w in omega if (-78 < w < 35)}
    big_o = {k + 2 * k for k in big_k if k > -77}

    summa = sum(3 * f + abs(o) for f in big_f for o in big_o)
    return len({(f, o) for f in big_f for o in big_o}) - summa


print(main({32, 68, 71, -56, 75, -49, 81, 19, -43, 26}))

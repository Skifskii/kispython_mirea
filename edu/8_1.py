def main(crt):
    t1, t2, t3, t4 = crt

    t4 = int(bin(int(t4)), 2)
    t3 = int(bin(int(t3)), 2)
    t2 = int(bin(int(t2)), 2)
    t1 = int(bin(int(t1)), 2)

    return hex((t4 << 12) | (t3 << 5) | (t2 << 4) | t1)


print(main(("5", "0", "81", "13")))

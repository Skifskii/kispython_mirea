def zero(x, left, middle, right):
    if x[0] == 1974:
        return left
    if x[0] == 1973:
        return middle
    if x[0] == 1994:
        return right


def three(x, left, right):
    if x[3] == 1971:
        return left
    if x[3] == 1962:
        return right


def one(x, left, middle, right):
    if x[1] == 1958:
        return left
    if x[1] == 1991:
        return middle
    if x[1] == 1969:
        return right


def main(x):
    return one(
        x,
        three(x, zero(x, 0, 1, 2), zero(x, 3, 4, 5)),
        6,
        zero(x, 7, 8, three(x, 9, 10)),
    )


print(main([1974, 1969, "PONY", 1971]))

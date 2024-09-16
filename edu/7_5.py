def two(x, left, middle, right):
    if x[2] == "HCL":
        return left
    if x[2] == "DIFF":
        return middle
    if x[2] == "JSX":
        return right


def one(x, left, middle, right):
    if x[1] == 1999:
        return left
    if x[1] == 1968:
        return middle
    if x[1] == 1996:
        return right


def three(x, left, right):
    if x[3] == "XSLT":
        return left
    if x[3] == "OPAL":
        return right


def zero(x, left, middle, right):
    if x[0] == "NINJA":
        return left
    if x[0] == "KIT":
        return middle
    if x[0] == "GENIE":
        return right


def four(x, left, right):
    if x[4] == 2004:
        return left
    if x[4] == 1980:
        return right


def main(x):
    return three(
        x,
        one(x, two(x, 0, 1, 2), 3, 4),
        zero(x, two(x, four(x, 5, 6), 7, 8), one(x, 9, 10, 11), 12),
    )


print(main(["KIT", 1968, "DIFF", "OPAL", 1980]))

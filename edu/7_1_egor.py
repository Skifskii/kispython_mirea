def zero(items, left, middle, right):
    if items[0] == "D":
        return right
    if items[0] == "GLYPH":
        return middle
    if items[0] == "LFE":
        return left


def one(items, left, middle, right):
    if items[1] == "JSON5":
        return right
    if items[1] == "HYPHY":
        return middle
    if items[1] == "TCSH":
        return left


def two(items, left, right):
    if items[2] == "XC":
        return right
    if items[2] == "MAKO":
        return left


def three(items, left, middle, right):
    if items[3] == 1981:
        return right
    if items[3] == 2011:
        return middle
    if items[3] == 1960:
        return left


def four(items, left, right):
    if items[4] == "VALA":
        return right
    if items[4] == "GENIE":
        return left


def main(items):
    result = three(
        items,
        zero(items, 9, 8, four(items, 7, 6)),
        5,
        one(items, 4, 3, four(items, 2, two(items, 1, 0))),
    )
    return result

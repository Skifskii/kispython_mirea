def compare(index, lst):
    if lst[0] == "NU":
        return index
    elif lst[0] == "PUG":
        return index + 1
    else:
        return index + 2


def main(x):
    if x[1] == "YAML":
        return 12
    else:
        if x[3] == "LESS":
            if x[4] == "HY":
                return 9
            elif x[4] == "D":
                return 10
            else:
                return 11
        else:
            if x[2] == "COBOL":
                return compare(6, x)
            elif x[2] == "MUF":
                return compare(3, x)
            else:
                return compare(0, x)

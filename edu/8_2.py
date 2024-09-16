def main(number):
    bin_string = bin(number)[2:]

    while len(bin_string) < 14:
        bin_string = "0" + bin_string

    bin_string = bin_string[::-1]

    f1 = bin_string[0:7][::-1]
    f2 = bin_string[7:10][::-1]
    f3 = bin_string[10]

    return [("F1", f1), ("F2", f2), ("F3", f3)]


main(405)

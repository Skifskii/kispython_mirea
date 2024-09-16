def main(hex_string):
    bin_string = bin(int(hex_string, 16))[2:]

    while len(bin_string) < 28:
        bin_string = "0" + bin_string

    bin_string = bin_string[::-1]

    q1 = int(bin_string[0:10][::-1], 2)
    q2 = int(bin_string[10:14][::-1], 2)
    q3 = int(bin_string[14][::-1], 2)
    q4 = 0
    q5 = int(bin_string[22:28][::-1], 2)

    return str((q3 << 27) | (q2 << 23) | (q5 << 17) | (q4 << 10) | q1)


print(main("0x21884d2"))

def main(hex_string):
    bin_string = bin(int(hex_string, 16))[2:]

    while len(bin_string) < 37:
        bin_string = "0" + bin_string

    bin_string = bin_string[::-1]

    b1 = 0
    b2 = int(bin_string[10:18][::-1], 2)
    b3 = int(bin_string[18:27][::-1], 2)
    b4 = int(bin_string[27:37][::-1], 2)

    return str((b4 << 27) | (b1 << 17) | (b2 << 9) | b3)


print(main("0x19129d602f"))

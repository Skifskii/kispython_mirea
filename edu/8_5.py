def main(dec_string):
    bin_string = bin(int(dec_string))[2:]

    while len(bin_string) < 23:
        bin_string = "0" + bin_string

    bin_string = bin_string[::-1]

    j1 = int(bin_string[0:5][::-1], 2)
    j2 = int(bin_string[5:11][::-1], 2)
    j3 = int(bin_string[11:21][::-1], 2)
    j4 = 0

    return (j4 << 21) | (j1 << 16) | (j2 << 10) | j3


print(main("821747"))

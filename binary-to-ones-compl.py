# from decimal-to-binary.py import decimal_to_binary()


"""Convert an unsigned binary number to one's complement representation."""

def main():
    # print(decimal_to_binary(10))
    print(10)


def bin_to_ones_compl(bin, neg: bool):
    """Converts unsigned to signed ones complement. Positive numbers are unchanged."""

    # NOTE: There exists a +0 and a -0.
    # If neg is false (leading bit is 0) then nothing is done.
    # If neg is true (leading bit is 1) then flip the bits
    # If there aren't enough bits, return an error

    # Maybe we should take in an array instead of a string
    # bin is a list of 1's and 0'ss

    if neg == True:
        if bin[0] == 0:
            bin[0] = 1
        else:
            print("Not enough bits to represent in one's complement binary.")
            return
    return bin

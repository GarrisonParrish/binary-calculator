"Used to test functions."

from decimal_conversions import *
from binary_conversions import *
from list_to_string import *

DEBUG_BIN = "10101010"
POS_DEC = 13
NEG_DEC = -7
DEBUG_BITS = 12


def main():
    # Convert a positive decimal number to binary unsigned
    unsigned_bin = dec_to_bin(POS_DEC)  # the lask of a designated type is really bugging me
    print(list_to_string(unsigned_bin, ' ', 4))

    """
    bits = dec_to_bin(POS_DEC, DEBUG_BITS)  # implicit definition (thanks Python)
    bits_str = list_to_string(bits)
    print(bits_str)
    # Nothing yet
    dec_result = bin_to_dec(DEBUG_BIN)
    print(dec_result)
    """

if __name__ == "__main__":
    main()
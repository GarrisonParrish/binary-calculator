"Used to test functions."

from decimal_conversions import *
from binary_conversions import *
from list_to_string import *

DEBUG_BIN = "10101010"
POS_DEC = 1
NEG_DEC = -7
DEBUG_BITS = 8


def main():
    # Convert a positive decimal number to binary unsigned
    unsigned_bin = dec_to_bin(POS_DEC, DEBUG_BITS)  # the lask of a designated type is really bugging me
    print(list_to_string(unsigned_bin, ' ', 4))

    # Convert the positive decimal to a negative twos complement representation
    twos_compl_bin = bin_to_twos_compl(unsigned_bin)
    print(list_to_string(twos_compl_bin, ' ', 4))

    # Convert both the unsigned binary and the twos complement respresentations back to decimal

    # Unsigned:
    unsigned_dec: int = bin_to_dec(unsigned_bin)
    # NOTE: somehow unsigned_bin is always a list of 1's, no matter the input. May have something to do with the lack of a type
    print(unsigned_dec)

    # Twos compl:
    # NOTE: expect this to be incorrect in its current form. Will need special functionality for twos complement conversions.
    twos_dec: int = bin_to_dec(twos_compl_bin)
    print(twos_dec)

    # NOTE: Need to throw exceptions for invalid cases. It's hard to tell where things are going wrong.


if __name__ == "__main__":
    main()
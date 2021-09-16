from dec_to_bin import *


"""Convert an unsigned binary number to one's complement representation."""


def bin_to_signed(bin, neg: bool):
    """Converts unsigned to signed magnitude representation. Positive numbers are unchanged."""

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


def bin_to_ones_compl(bin, neg: bool):
    """Converts unsigned to ones complement. Positive numbers are unchanged."""

    # NOTE: There exists a +0 and a -0.
    # If neg is false (leading bit is 0) then nothing is done.
    # If neg is true (leading bit is 1) then flip the bits
    # If there aren't enough bits, return an error

    # Maybe we should take in an array instead of a strings
    # bin is a list of 1's and 0'ss

    if neg == True:
        for bit in range(0, len(bin)):
            # Flip the bits
            if bin[bit] == 1:
                bin[bit] = 0
            else:
                bin[bit] = 1
    
    return bin

def dec_to_ones_compl(dec):
    """Converts a decimal to signed ones complement."""
    # NOTE: method overloading is not possible in Python

    # If dec is negative (below 0):
    # Take absolute value
    # Convert to unsigned magnitude binary
    # Convert to ones complement with neg = True
    
    # If dec is positive:
    # Convert to unsigned magnitude binary
    # Convert to ones complement with neg = False (changes nothing)

    neg: bool = False
    if dec < 0:
        neg = True
        dec = abs(dec)
    
    return bin_to_ones_compl(dec_to_bin(dec, 8), neg)
"""Handle conversions from binary (as lists) to other forms."""


def bin_to_dec(bin: str) -> int:
    """Convert binary number (as list) to decimal integer."""
    # Take string and parse it from right to left into an array of ints
    # All extra ints are left as 0's (do I need this step?)
    # Feed this array into the algorithm
    # Starting at rightmost bit ( i = N-1 ), add 2^(i) to the decimal result
    # When finished with the array, should have the result
     # probably not the most efficient way to do this but it counts down from the top and it works
    dec_result: int = 0
    j: int = 0  # counter for exponents (there has to be a better way to do this)
    for i in range(len(bin)-1, -1, -1):
        if bin[i] != '1' and bin[i] != '0':
            print("Invalid bit string: must contain only 1's or 0's")
            return -1  # NOTE: may need to find a better way to handle this error
        if bin[i] == '1':
            dec_result += 2**j
        j += 1

    return dec_result


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
    if neg == True:
        for bit in range(0, len(bin)):
            # Flip the bits
            if bin[bit] == 1:
                bin[bit] = 0
            else:
                bin[bit] = 1
    
    return bin


def bin_to_twos_compl(bin):
    """Converts binary (as array) to twos complement negative."""
    one_flag: bool = False
    for bit in range(len(bin)-1, -1, -1):
        # Reading from the right, flip all the bits except for the first 1 encountered
        if bin[bit] == 1 and one_flag == False:
            one_flag = True
        elif bin[bit] == 1:
            bin[bit] = 0
        else:
            bin[bit] = 1
    return bin
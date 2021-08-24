"""Take a string and parse it into an array of ints, then read it and convert to a decimal."""

DEBUG_BIN = "0"

# NOTE: The same issue exists here: it will not convert 0 0011 0101 -> 170 correctly. It says it's 53.
# It's fine with 0110 0000 0000 -> 1536 though.

def main():
    # Nothing yet
    dec_result = binary_to_decimal(DEBUG_BIN)
    print(dec_result)


def binary_to_decimal(bin: str) -> int:
    """Convert binary string to decimal integer."""
    bin_len: int = len(bin)

    # Take string and parse it from right to left into an array of ints
    # All extra ints are left as 0's (do I need this step?)
    # Feed this array into the algorithm
    # Starting at rightmost bit ( i = N-1 ), add 2^(i) to the decimal result
    # When finished with the array, should have the result

     # probably not the most efficient way to do this but it counts down from the top and it works

    dec_result: int = 0
    j: int = 0  # counter for exponents (there has to be a better way to do this)
    for i in range(bin_len-1, -1, -1):
        if bin[i] != '1' and bin[i] != '0':
            print("Invalid bit string: must contain only 1's or 0's")
            return -1  # NOTE: may need to find a better way to handle this error
        if bin[i] == '1':
            dec_result += 2**j
        j += 1

    return dec_result

if __name__ == "__main__":
    main()
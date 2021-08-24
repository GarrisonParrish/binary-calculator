"""Take a string and parse it into an array of ints, then read it and convert to a decimal."""

DEBUG_BIN = "01010"

def main():
    # Nothing yet
    binary_to_decimal(DEBUG_BIN)


def binary_to_decimal(bin: str) -> int:
    """Convert binary string to decimal integer."""
    bin_len: int = len(bin)

    # Take string and parse it from right to left into an array of ints
    # All extra ints are left as 0's (do I need this step?)
    # Feed this array into the algorithm
    # Starting at rightmost bit ( i = N-1 ), add 2^(i) to the decimal result
    # When finished with the array, should have the result

     # probably not the most efficient way to do this but it counts down from the top and it works
    for i in range(bin_len-1, -1, -1):
        print(bin[i] == '1')


    return 0

if __name__ == "__main__":
    main()
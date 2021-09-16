"""Take a decimal integer and a number of bits and convert to unsigned binary representation."""


def dec_to_bin(dec: int, N: int = 32):
    """Converts decimal integer to N-bit unsigned binary as a list. N defaults to 32 bits."""
    # take dec, use algorithm to display as a string of 1's and 0's in 16-bit binary
    # 0. Check if the decimal value exceeds the maximum alotted space (whatever that is)
    # 1. Make an array of size N with all ints 0
    # 2. Starting from leftmost bit (index bits-1):
    # 3. bit = dec % 2
    # 4. dec = dec / 2
    # 5. repeat
    # 6. If you run out of space early, terminate looping and leave the rest as 0
    if (dec > ( 2**N + ( 2**N - 1))):
        print(f"Cannot represent { dec } in { N } bits.")
        return ""  
        # NOTE: Now we will have to be able to handle a null string. 
        # Either this or we will have to throw an exception instead.

    bits: int[N] = [0] * N  # initializes list with N number of 0's
    # bits are either 1 or 0. Will read these into a string afterwards.

    dec_copy: int = dec
    i: int = N-1
    while dec_copy > 0:
        bits[i] = dec_copy % 2
        dec_copy = dec_copy // 2  # floor division
        i -= 1
    
    return bits
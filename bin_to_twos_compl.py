from bin_to_ones_compl import bin_to_ones_compl

def bin_to_twos_compl(bin, neg: bool):
    """Converts binary (as array) to twos complement."""

    if neg == True:
        for bit in range(0, len(bin)):
            # Flip the bits
            if bin[bit] == 1:
                bin[bit] = 0
            else:
                bin[bit] = 1
    
    return bin

    
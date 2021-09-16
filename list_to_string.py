"""Takes in a list of chars and converts to a string. Optional delimiter and interval arguments."""

def list_to_string(char_list, delimiter: str = '', interval: int = 1) -> str:
    """Takes in a list of chars and converts to a string. Optional delimiter and interval arguments."""
    return_str: str = ''
    # Start from right and move left
    i: int = len(char_list) - 1
    while i >= 0:
        return_str = str(char_list[i]) + return_str
        if i != 0 and i % interval == 0:
            return_str = delimiter + return_str
        i -= 1
    """
    for char in char_list:
        return_str = return_str + str(char)
        if i % interval == 0:
            return_str = return_str + delimiter
        i += 1
    """
    return return_str
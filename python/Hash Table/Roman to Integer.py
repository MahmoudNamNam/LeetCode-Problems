def romanToInt(s):
    """
    Convert a Roman numeral to an integer.

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.
    Symbol       Value
    I            1
    V            5
    X            10
    L            50
    C            100
    D            500
    M            1000

    To convert a Roman numeral to an integer, we iterate through the string from left to right,
    adding the value of each symbol to the result. If a symbol appears before a larger symbol, we
    subtract its value instead.

    Args:
        s (str): The Roman numeral string to convert.

    Returns:
        int: The integer representation of the Roman numeral string.
    """
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for char in s:
        value = roman_numerals[char]
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value
    
    return result

# Test cases
romanToInt("MCMXCIIV")


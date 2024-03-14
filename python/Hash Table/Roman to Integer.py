
def romanToInt(s):
        """
        :type s: str
        :rtype: int
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




class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647 
        if ((dividend<0 and divisor >0) or (dividend>0 and divisor <0)) and dividend % divisor != 0:
            return dividend//divisor +1
        return dividend//divisor 
    
    def divide2(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        if dividend == -2147483648 and divisor == -1:
            return 2147483647  # Special case to avoid overflow

        # Check if signs of dividend and divisor are different
        is_negative = (dividend < 0) ^ (divisor < 0)

        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        result = dividend_abs // divisor_abs

        if is_negative:
            result = -result

        return result
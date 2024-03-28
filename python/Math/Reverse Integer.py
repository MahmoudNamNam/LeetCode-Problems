class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        negative = x < 0
        x = abs(x)
        reversed_x = 0
        
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        
        if negative:
            reversed_x *= -1
        
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x

# Test cases
sol = Solution()
print(sol.reverse(123))   # Output: 321
print(sol.reverse(-123))  # Output: -321
print(sol.reverse(120))   # Output: 21

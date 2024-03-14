class Solution(object):
    def isHappy(self, n):
        """
        Determine if a number is happy.

        A happy number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits,
        and repeat the process until the number equals 1 (where it will stay), or it loops endlessly
        in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

        Args:
            n (int): The number to check for happiness.

        Returns:
            bool: True if the number is happy, False otherwise.
        """
        def get_next(num):
            sum_of_squares = 0
            while num > 0:
                digit = num % 10
                sum_of_squares += digit ** 2
                num //= 10
            return sum_of_squares

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1



# Another Solution
    

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums_set = set()
        while True:
            if n in nums_set:
                return False
            n = str(n)
            sum = 0
            for char in n:
                sum += int(char)**2
            if sum == 1:
                return True
            else:
                nums_set.add(int(n))
            n = sum
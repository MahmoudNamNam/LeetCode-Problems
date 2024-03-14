class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
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
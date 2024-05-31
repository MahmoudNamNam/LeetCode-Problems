class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # to convert base -2 array to decimal integer
        def baseNeg2ToInt(arr):
            result = 0
            for i in range(len(arr)):
                result += arr[i] * ((-2) ** (len(arr) - 1 - i))
            return result
        
        # to convert decimal integer to base -2 array
        def intToBaseNeg2(n):
            if n == 0:
                return [0]
            result = []
            while n != 0:
                remainder = n % -2
                n = n // -2
                if remainder < 0:
                    remainder += 2
                    n += 1
                result.append(remainder)
            result.reverse()
            return result
        
        # Convert both arrays from base -2 to decimal
        num1 = baseNeg2ToInt(arr1)
        num2 = baseNeg2ToInt(arr2)
        
        # Add the two decimal numbers
        sum_decimal = num1 + num2
        
        # Convert the sum back to base -2
        result = intToBaseNeg2(sum_decimal)
        
        return result

solution = Solution()
print(solution.addNegabinary([1, 1, 1, 1, 1], [1, 0, 1]))  # Output: [1, 0, 0, 0, 0]
print(solution.addNegabinary([0], [0]))  # Output: [0]
print(solution.addNegabinary([0], [1]))  # Output: [1]

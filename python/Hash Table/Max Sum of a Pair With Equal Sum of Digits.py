from typing import List


class Solution:
    def sumOfDigits(self, n):
        sumOfDigits = 0
        while n != 0:
            last = n % 10
            sumOfDigits += last
            n //= 10
        return sumOfDigits

    def maximumSum(self, nums: List[int]) -> int:
        numOfDigits = {}
        maxSum = -1
        for i in range(len(nums)):
            sumOfDigits = self.sumOfDigits(nums[i])
            if sumOfDigits in numOfDigits:
                maxSum = max(maxSum, numOfDigits[sumOfDigits] + nums[i])
                numOfDigits[sumOfDigits] = max(numOfDigits[sumOfDigits], nums[i])
            else:
                numOfDigits[sumOfDigits] = nums[i]
        return maxSum
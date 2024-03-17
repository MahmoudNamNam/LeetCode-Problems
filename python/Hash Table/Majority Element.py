from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        for k,i in counter.items():
            if i > len(nums)//2:
                return k
        return -1

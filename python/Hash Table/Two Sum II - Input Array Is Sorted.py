from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_sum={}
        for idx,val in enumerate(numbers):
            remaining = target - val
            if remaining in hash_sum.keys():
                return [hash_sum[remaining],idx+1]
            else:
                hash_sum[val]=idx+1
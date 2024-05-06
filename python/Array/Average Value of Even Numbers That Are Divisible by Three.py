from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sm = 0
        cnt = 0

        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                sm += i
                cnt += 1
        
        if cnt == 0:
            return 0 

        return sm // cnt


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        acc = [x for x in nums if x % 2 == 0 and x/3 == x//3]
        if acc == []:
            return 0
        else:
            return sum(acc) // len(acc)
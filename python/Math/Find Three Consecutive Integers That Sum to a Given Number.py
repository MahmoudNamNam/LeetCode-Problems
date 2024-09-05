from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 == 0:
            a = num//3
            return [a-1,a,a+1]
        else:
            return []
from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for i in arr:
            if i % 2 != 0:  
                cnt += 1
                if cnt == 3:  # If we find three consecutive odds
                    return True
            else:
                cnt = 0  # Reset count if we find an even number
        return False


sol =Solution()
print(sol.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(1,len(arr)-1):
            if arr[i]%2!=0 and arr[i-1]%2!=0 and arr[i+1]%2!=0:
                return True
        return False
from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        
        if k == 0: 
            return res
        
        if k > 0:
            for i in range(n):
                res[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            return res
        
        k = -k 
        for i in range(n):
            res[i] = sum(code[(i - j) % n] for j in range(1, k + 1))
        return res

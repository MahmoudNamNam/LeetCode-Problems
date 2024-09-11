class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor= start ^ goal
        bn_xor = bin(xor)
        res=0
        for i in range(2,len(bn_xor)):
            if bn_xor[i]=='1':
                res+=1
        return res
class Solution:
    def minimumSteps(self, s: str) -> int:
        ones=0
        res=0
        for c in s:
            if c=='1':
                ones+=1
            else:
                res+=ones
        return res
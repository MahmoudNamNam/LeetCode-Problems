class Solution:
    def makeFancyString(self, s: str) -> str:
        res =''
        cnt=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                cnt+=1
                if cnt>=3:
                    continue
            else:
                cnt=1
            res+=s[i]
        res+=s[-1]
        return res


sol= Solution()
s = "leeetcode"
print(sol.makeFancyString(s))
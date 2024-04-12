class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        if  sLen == 0: return True
        if sLen > tLen: return False
        j=0
        cnt=0
        for i in t:
            if i == s[j] and j<sLen:
                cnt+=1
                j +=1
            if cnt == sLen:
                return True
        return False



sol= Solution()
sol.isSubsequence(s = "abc", t = "ahbgdc")
print(sol.isSubsequence(s = "abc", t = "ahbgdc"))


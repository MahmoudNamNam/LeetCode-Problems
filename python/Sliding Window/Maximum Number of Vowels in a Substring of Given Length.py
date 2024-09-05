class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        if n<k or not s:
            return 0
        vowles = {'a', 'e', 'i', 'o','u'}
        cnt =0
        for i in range(k):
            if s[i] in vowles:
                cnt+=1
        current_len =cnt
        for i in range(k,len(s)):
            if s[i-k] in vowles:
                current_len-=1
            if s[i] in vowles:
                current_len+=1
            cnt = max(current_len,cnt)
        return cnt






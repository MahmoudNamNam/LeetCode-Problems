class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        rem ={'AB','CD'}
        for i in range(len(s)):
            if stack and stack[-1]+s[i] in rem:
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)

sol = Solution()
print(sol.minLength( "ABFCACDB"))
print(sol.minLength( "ACBBD"))
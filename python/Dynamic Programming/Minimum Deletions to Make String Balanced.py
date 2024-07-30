class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0  
        b_count = 0  

        for char in s:
            if char == 'b':
                b_count += 1
            else:  
                a_count = min(a_count + 1, b_count)

        return a_count

sol =Solution()

s = "aababbab"
print(sol.minimumDeletions(s))
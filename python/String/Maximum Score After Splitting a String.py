"""
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
"""

class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        left_zeros = 0
        max_score = 0

        for i in range(len(s) - 1): 
            if s[i] == '0':
                left_zeros += 1
            else:
                total_ones -= 1
            score = left_zeros + total_ones
            max_score = max(max_score, score)

        return max_score


sol = Solution()
s = "011101"
print(sol.maxScore(s))  # 5
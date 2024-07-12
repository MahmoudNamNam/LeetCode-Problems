class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s: str, sub: str, points: int) -> (str, int): # type: ignore
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] + char == sub:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score

        # Prioritize the removal
        if x >= y:
            # First remove "ab" to get maximum points from "ab"
            s, score_ab = remove_substring(s, "ab", x)
            # Then remove "ba" to get remaining points from "ba"
            s, score_ba = remove_substring(s, "ba", y)
        else:
            # First remove "ba" to get maximum points from "ba"
            s, score_ba = remove_substring(s, "ba", y)
            # Then remove "ab" to get remaining points from "ab"
            s, score_ab = remove_substring(s, "ab", x)
        
        return score_ab + score_ba

sol =Solution()

print(sol.maximumGain("cdbcbbaaabab", 4, 5))  # Output: 19
print(sol.maximumGain("aabbaaxybbaabb", 5, 4))  # Output: 20
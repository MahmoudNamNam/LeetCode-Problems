from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Define vowels for quick lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Create prefix sum array
        n = len(words)
        prefix_sum = [0] * (n + 1)
        
        # Populate the prefix sum array
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_sum[i + 1] += 1
        
        # Answer the queries using the prefix sum
        result = []
        for start, end in queries:
            result.append(prefix_sum[end + 1] - prefix_sum[start])
        
        return result


sol = Solution()

print(sol.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))
print(sol.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))
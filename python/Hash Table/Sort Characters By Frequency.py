from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        # Sort by frequency (descending) and then by character (descending)
        sorted_chars = sorted(s, key=lambda x: (-cnt[x], -ord(x)))

        return ''.join(sorted_chars)

# Test examples
solution = Solution()
print(solution.frequencySort("tree")) # Output: "eert" or "eetr"
print(solution.frequencySort("cccaaa")) # Output: "aaaccc"
print(solution.frequencySort("Aabb")) # Output: "bbAa"





class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        cnt = Counter(s)
        
        # Step 2: Sort characters by frequency (descending) and by character (descending)
        sorted_chars = sorted(cnt.items(), key=lambda x: (-x[1], -ord(x[0])))
        
        # Step 3: Reconstruct the sorted string
        result = ''.join([char * freq for char, freq in sorted_chars])
        
        return result

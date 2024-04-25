class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        max_lengths = [0] * 128
        for char in s:
            char_ascii = ord(char)
            max_lengths[char_ascii] = max(max_lengths[char_ascii - k : char_ascii + k + 1]) + 1
        return max(max_lengths)

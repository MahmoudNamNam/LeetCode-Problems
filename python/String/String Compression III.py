class Solution:
    def compressedString(self, word: str) -> str:
        result = ''
        i = 0
        while i < len(word):
            count = 1
            while i + count < len(word) and word[i + count] == word[i] and count < 9:
                count += 1
            result += str(count) + word[i]
            i += count
        return result

sol = Solution()
print(sol.compressedString("abcde"))         # Expected output: "1a1b1c1d1e"
print(sol.compressedString("aaaaaaaaaaaaaabb"))  # Expected output: "9a5a2b"
print(sol.compressedString("mrm"))           # Expected output: "1m1r1m"

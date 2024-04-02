class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alphabets = [0] * 26
        ans = None
        
        for char in t:
            alphabets[ord(char) - ord('a')] += 1
            
        for char in s:
            alphabets[ord(char) - ord('a')] -= 1
        
        for i in range(26):
            if alphabets[i] != 0:
                ans = chr(i + ord('a'))
                break
        
        return ans

# Example usage:
solution = Solution()
print(solution.findTheDifference("abcd", "abcde"))  # Output: 'e'
print(solution.findTheDifference("", "y"))         # Output: 'y'



# Another sol using **XOR**
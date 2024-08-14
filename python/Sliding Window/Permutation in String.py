from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get the lengths of both strings
        len_s1 = len(s1)
        len_s2 = len(s2)

        # If the length of s1 is greater than s2, it's impossible for s1's permutation to be a substring of s2
        if len_s1 > len_s2:
            return False

        # Count the frequency of characters in s1
        s1_count = Counter(s1)
        # Count the frequency of characters in the first window (of size len_s1) of s2
        window_count = Counter(s2[:len_s1])

        # Check if the initial window is a permutation of s1
        if s1_count == window_count:
            return True

        # Slide the window over the rest of s2
        for i in range(len_s1, len_s2):
            # The character that is leaving the window
            start_char = s2[i - len_s1]
            # The new character entering the window
            new_char = s2[i]
            
            # Update the count of the new character in the window
            window_count[new_char] += 1
            # Decrease the count of the character that is sliding out of the window
            window_count[start_char] -= 1

            # If the count of the character that is sliding out becomes 0, remove it from the Counter
            if window_count[start_char] == 0:
                del window_count[start_char]

            # Check if the current window is a permutation of s1
            if s1_count == window_count:
                return True

        # If no permutation of s1 is found in s2, return False
        return False



sol  =Solution()

s1 = "ab"
s2 = "eidbaooo"

print(sol.checkInclusion(s1,s2))

s1 = "ab"
s2 = "eidboaoo"
print(sol.checkInclusion(s1,s2)) 